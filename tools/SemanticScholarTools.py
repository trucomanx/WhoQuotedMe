#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import re 

def SemanticScholarCited(path_of_chromedriver, article_title,cited_text):
    article_title=article_title.lower().strip();
    #print(path_of_chromedriver);
    
    mycited=[];
    mydata=None;

    options = Options();
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')


    driver = webdriver.Chrome(path_of_chromedriver, options=options);

    # access Semantic Scholar main page
    driver.get('https://www.semanticscholar.org/')

    # waits for the page to load, searching for the Field of Study filter to be enabled
    try:
        waitelement = WebDriverWait(driver, 20). \
            until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search text']")))
    except TimeoutError:
        print("PAGE 1 DID NOT LOAD!")

    # dismiss the popup that asks to allow cookies, if it shows up
    try:
        driver.find_element_by_xpath(
            "//div[@class='copyright-banner__dismiss-btn button button--secondary']").click()
    except:
        pass
    
    #driver.save_screenshot('foo1.png')
    
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
    
    #driver.save_screenshot('foo2a.png')
    #waitelement.screenshot("foo2b.png")
    
    list_articles_in_page = driver.find_elements_by_xpath("//div[@class='cl-paper-row serp-papers__paper-row paper-row-normal']")


    for item in list_articles_in_page:
        # saves the article title as a string
        GS_T = item.find_element_by_xpath(".//a[@data-selenium-selector='title-link']");
        title = GS_T.text.lower().strip();
        #GS_T.screenshot("foo.png")
        #print("  title:{"+title+"}")
        #print(" title2:{"+article_title+"}")
        
        if(re.sub("[^a-zA-Z]+", "",title)==re.sub("[^a-zA-Z]+", "",article_title)):
            #print("  title:{"+title+"}")
            hrefval=GS_T.get_attribute('href');
            #print("   href:{"+hrefval+"}")
        
            list_authors_html_link = item.find_elements_by_xpath(".//a[@class='cl-paper-authors__author-link']");
            authors=[];
            for dat in list_authors_html_link:
                authors.append(dat.text);
            
            #print(authors,",")
            
            mydata={
                "title":title,
                "authors":authors,
                "href":hrefval
            };
            
            if(len(hrefval)!=0):
                # access Semantic Scholar main page
                #print(hrefval);
                driver2 = webdriver.Chrome(path_of_chromedriver, options=options);
                driver2.get(hrefval)

                # waits for the page to load, searching for the Field of Study filter to be enabled
                try:
                    waitelement = WebDriverWait(driver2, 20). \
                        until(EC.presence_of_element_located((By.XPATH, "//div[@class='scorecard-stat__body']")))
                except:
                    print("CITATION PAGE DID NOT LOAD!")
                    return [],mydata;
                
                #waitelement.screenshot('foo3b.png')
                #driver2.save_screenshot('foo3.png')
                
                list_of_cited = driver2.find_elements_by_xpath("//div[@class='cl-paper-row citation-list__paper-row']")
                

                n=0;
                for item in list_of_cited:
                    # saves the article title as a string
                    GS_RT = item.find_element_by_xpath(".//a[@data-heap-id='citation_title']");
                    title = GS_RT.text.lower().strip();
                    
                    if(title!=article_title):
                        hrefval=GS_RT.get_attribute('href');
                        authors_list = item.find_elements_by_xpath(".//a[@class='cl-paper-authors__author-link']");
                        
                        authors=[];
                        for dat in authors_list:
                            #print(dat.text)
                            authors.append(dat.text);
                            
                        tmp={
                            "title":title,
                            "authors":authors,
                            "href":hrefval
                        };
                        mycited.append(tmp);
                        n=n+1;
    
    return mycited,mydata;
