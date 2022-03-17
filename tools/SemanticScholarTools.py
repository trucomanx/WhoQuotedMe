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
        driver.close();
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
        driver.close();
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
            
            driver.close();
            return dicdata;
    
    driver.close();
    return dicdata;
    

def SemanticScholarCited(path_of_chromedriver, article_title, timeout=20):
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
    
    if(len(hrefval)>5):
        # access Semantic Scholar main page
        driver2 = webdriver.Chrome(path_of_chromedriver, options=options);
        driver2.get(hrefval)
        
        # waits for the page to load,
        try:
            waitelement = WebDriverWait(driver2, timeout). \
                until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex-container flex-row flex-column-med flex-relative-pos']")))
        except:
            print("\nPROBLEMS LOADING REFERENCES IN:");
            ST.print_paper_data(dicdata);
            return dicdata,[];
            
        # dismiss the popup that asks to allow cookies, if it shows up
        try:
            driver2.find_element_by_xpath(
                "//div[@class='copyright-banner__dismiss-btn button button--secondary']").click()
        except:
            pass
        
        ## waitelement.screenshot('foo3b.png')
        ## driver2.save_screenshot('foo1.png')
        
        
            
        
        nn=0;
        while True:
            list_of_paper_data=[];
            print("page:",nn+1)
            
            # waits for the page to load,
            try:
                # Selecting the references
                bigstructure = WebDriverWait(driver2, timeout). \
                    until(EC.presence_of_element_located((By.XPATH,".//div[@id='references']")))
            except:
                print("\nDON'T HAVE MORE References:");
                return dicdata,list_of_dicdata;
            
            
            has_nextpage=False;
            try:
                bar = bigstructure.find_element_by_xpath(".//div[@class='citation-pagination flex-row-vcenter']");
                has_nextpage=True;
            except:
                pass;
                
            if(has_nextpage):
                while True:
                    try:
                        element = bigstructure.find_element_by_xpath(".//div[@data-curr-page-num='"+str(nn+1)+"']");
                        if(element.size!=0):
                            break;
                    except:
                        pass;
            #bigstructure.screenshot('foo_big'+str(nn+1)+'.png')
            
            # Getting the list of paper data
            list_of_paper_data = bigstructure.find_elements_by_xpath(".//div[@class='cl-paper-row citation-list__paper-row']")
            #print("len:",len(list_of_paper_data))
            
            if(len(list_of_paper_data)==0):
                break;
            #
            for paper in list_of_paper_data:
                # saves the article title as a string
                GS_RT = paper.find_element_by_xpath(".//div[@class='cl-paper-title']");
                title = GS_RT.text.lower().strip();
                
                print("title:",title)
                
                if (len(title)>0)and(title!=article_title):
                    # saves the link of article as a string
                    try:
                        GS_RT = paper.find_element_by_xpath(".//a[@data-heap-id='citation_title']");
                        hrefval=GS_RT.get_attribute('href');
                    except:
                        hrefval='';
                    
                    
                    # saves the authors as a list string
                    try:
                        authors_list = paper.find_elements_by_xpath(".//a[@class='cl-paper-authors__author-link']");
                        authors=[];
                        for dat in authors_list:
                            authors.append(dat.text);
                    except:
                        authors=[];
                        
                    
                    
                    # saves the date as a string
                    try:
                        dates=paper.find_element_by_xpath(".//span[@class='cl-paper-pubdates']").text;
                    except:
                        dates='';
                        
                    # Adding to list_of_dicdata
                    tmp={
                        "title":title, 
                        "authors":authors,
                        "href":hrefval,
                        "date":dates
                    };
                    list_of_dicdata.append(tmp);
            
            #break;
            # tries to go to the next page, if exists
            try:
                # waits for the page to load,
                
                
                button=bigstructure.find_element_by_xpath(".//div[@data-selenium-selector='next-page']")
                ##button.screenshot('foo1'+str(nn)+'.png')
                button.click();
                
            except:
                ## print("SUBJECT HAS NO MORE SEARCH PAGES!")
                break;
            nn=nn+1;
    
    return dicdata,list_of_dicdata;
