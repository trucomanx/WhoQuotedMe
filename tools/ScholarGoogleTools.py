#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

def ScholarGoogleCited(path_of_chromedriver, article_title,cited_text):
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
    driver.get('https://scholar.google.com.br/')

    # waits for the page to load, searching for the Field of Study filter to be enabled
    try:
        waitelement = WebDriverWait(driver, 20). \
            until(EC.presence_of_element_located((By.XPATH, "//form[@action='/scholar']")))
    except TimeoutError:
        print("~~~~ PAGE 1 DID NOT LOAD! ~~~~")
    
    # input the desired search phrase in the input box and hits ENTER
    driver.find_element_by_name('q').send_keys("body languages cnn")
    driver.find_element_by_name('q').send_keys(Keys.ENTER)

    # waits for the page to load, searching for the Field of Study filter to be enabled
    try:
        waitelement = WebDriverWait(driver, 20). \
            until(EC.presence_of_element_located((By.XPATH, "//span[@class='gs_nph gs_nta']")))
    except TimeoutError:
        print("~~~~ PAGE 2 DID NOT LOAD! ~~~~")
        
    list_articles_in_page = driver.find_elements_by_xpath("//div[@class='gs_r gs_or gs_scl']")


    for item in list_articles_in_page:
        # saves the article title as a string
        GS_T = item.find_element_by_xpath(".//h3[@class='gs_rt']");
        title = GS_T.text;
        
        if(title.lower().strip()==article_title.lower().strip()):
            hrefval=GS_T.find_element_by_tag_name('a').get_attribute('href');
            
            GS_A=item.find_element_by_xpath(".//div[@class='gs_a']");
            authors = GS_A.text;
            
            GS_FL = item.find_element_by_xpath(".//div[@class='gs_fl']");
            element_cited = GS_FL.find_element_by_partial_link_text(cited_text);
            cited_by=element_cited.text;
            
            mydata={
                "title":title,
                "authors":authors,
                "href":hrefval
            };
            
            
            href_cited=element_cited.get_attribute('href');
            
            print(href_cited+"\n")
            
            if(len(href_cited)!=0):
                # access Semantic Scholar main page
                #print(href_cited);
                driver2 = webdriver.Chrome(path_of_chromedriver, options=options);
                driver2.get(href_cited)
            
                # waits for the page to load, searching for the Field of Study filter to be enabled
                try:
                    waitelement = WebDriverWait(driver2, 20). \
                        until(EC.presence_of_element_located((By.XPATH, "//form[@action='/scholar']")))
                except TimeoutError:
                    print("~~~~ PAGE 1 DID NOT LOAD! ~~~~")
                
                list_of_cited = driver2.find_elements_by_xpath("//div[@class='gs_r gs_or gs_scl']")
                
                
                n=0;
                for item in list_of_cited:
                    # saves the article title as a string
                    GS_RT = item.find_element_by_xpath(".//h3[@class='gs_rt']");
                    title = GS_RT.text;
                    
                    if(title.lower().strip()!=article_title.lower().strip()):
                        hrefval=GS_RT.find_element_by_tag_name('a').get_attribute('href');
                        authors = item.find_element_by_xpath(".//div[@class='gs_a']").text;
                        
                        tmp={
                            "title":title,
                            "authors":authors,
                            "href":hrefval
                        };
                        mycited.append(tmp);
                        n=n+1;
    return mycited,mydata;
