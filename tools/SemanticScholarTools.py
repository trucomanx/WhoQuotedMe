#
import tools.StringTools as ST

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re 

'''

'''
def SemanticScholarDataFromTitle(path_of_chromedriver, article_title):
    article_title=article_title.lower().strip();
    
    dicdata=None;
    
    options = Options();
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(path_of_chromedriver, options=options);

    # access Semantic Scholar main page
    SemanticsScholarSite='https://www.semanticscholar.org/';
    driver.get(SemanticsScholarSite);

    # waits for the page to load, searching for the Field of Study filter to be enabled
    try:
        waitelement = WebDriverWait(driver, 20). \
            until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search text']")))
    except:
        print("PROBLEMS LOADING:",SemanticsScholarSite);
        return None;

    # dismiss the popup that asks to allow cookies, if it shows up
    try:
        driver.find_element_by_xpath(
            "//div[@class='copyright-banner__dismiss-btn button button--secondary']").click()
    except:
        pass
    ## driver.save_screenshot('foo1.png')
    
    # input the desired search phrase in the input box and hits ENTER
    driver.find_element_by_name('q').send_keys(article_title)
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    
    # waits for the page to load, searching for the Field of Study filter to be enabled
    try:
        waitelement = WebDriverWait(driver, 20). \
            until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='dropdown-filters__result-count']")))
    except TimeoutError:
        print("PAGE DID NOT LOAD!")
        return None;
    
    ## driver.save_screenshot('foo2a.png')
    ## waitelement.screenshot("foo2b.png")
    
    list_articles_in_page = driver.find_elements_by_xpath("//div[@class='cl-paper-row serp-papers__paper-row paper-row-normal']")
    
    for item in list_articles_in_page:
        # saves the article title as a string
        GS_T = item.find_element_by_xpath(".//a[@data-selenium-selector='title-link']");
        title = GS_T.text.lower().strip();
        ## GS_T.screenshot("foo.png")
        
        if(re.sub("[^a-zA-Z]+", "",title)==re.sub("[^a-zA-Z]+", "",article_title)):
            # saves the link of article as a string
            hrefval=GS_T.get_attribute('href');
            
            # saves the authors as a list string
            list_authors_html_link = item.find_elements_by_xpath(".//a[@class='cl-paper-authors__author-link']");
            
            authors=[];
            for dat in list_authors_html_link:
                authors.append(dat.text);
            
            # saves the date as a string
            dates=item.find_element_by_xpath(".//span[@class='cl-paper-pubdates']").text;
            
            # Packaging
            dicdata={
                "title":title,
                "authors":authors,
                "href":hrefval,
                "date":dates
            };
            
            return dicdata;
            
    return dicdata;
    

def SemanticScholarCited(path_of_chromedriver, article_title):
    list_of_dicdata=[];
    
    dicdata=SemanticScholarDataFromTitle(path_of_chromedriver, article_title);
    if(dicdata==None):
        return None,[];
    
    options = Options();
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    
    hrefval=dicdata["href"];
    
    if(len(hrefval)!=0):
        # access Semantic Scholar main page
        driver2 = webdriver.Chrome(path_of_chromedriver, options=options);
        driver2.get(hrefval)
        
        # waits for the page to load, searching for the Field of Study filter to be enabled
        try:
            waitelement = WebDriverWait(driver2, 20). \
                until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex-container flex-row flex-column-med flex-relative-pos']")))
        except:
            print("\nPROBLEMS LOADING REFERENCES IN:");
            ST.print_paper_data(dicdata);
            return dicdata,[];
        
        ## waitelement.screenshot('foo3b.png')
        ## driver2.save_screenshot('foo3.png')
        
        # Selecting the references
        references=driver2.find_element_by_xpath("//div[@id='references']");
        
        # Getting the list of paper data
        list_of_paper_data = references.find_elements_by_xpath(".//div[@class='cl-paper-row citation-list__paper-row']")
        
        for paper in list_of_paper_data:
            # saves the article title as a string
            GS_RT = paper.find_element_by_xpath(".//a[@data-heap-id='citation_title']");
            title = GS_RT.text.lower().strip();
            
            if(title!=article_title):
                # saves the link of article as a string
                hrefval=GS_RT.get_attribute('href');
                
                # saves the authors as a list string
                authors_list = paper.find_elements_by_xpath(".//a[@class='cl-paper-authors__author-link']");
                
                authors=[];
                for dat in authors_list:
                    authors.append(dat.text);
                
                # saves the date as a string
                dates=paper.find_element_by_xpath(".//span[@class='cl-paper-pubdates']").text;
                
                # Adding to list_of_dicdata
                tmp={
                    "title":title, 
                    "authors":authors,
                    "href":hrefval,
                    "date":dates
                };
                list_of_dicdata.append(tmp);
    
    return dicdata,list_of_dicdata;
