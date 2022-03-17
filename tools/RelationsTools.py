import tools.SemanticScholarTools as SST
import re 

'''
[Input]
     title: {string} Paper title to verify if pertain to paper data list.
paper_data: {list of dictionaries} Paper data list.
{Return}
Return true if title pertain to any title in the paper data list, false in other cases.
'''
def title_in_paperdata(title,paper_data):
    M=len(paper_data);
    
    text1=re.sub("[^a-zA-Z]+", "",title.lower().strip());
    for m in range(M):
        text2=re.sub("[^a-zA-Z]+", "",paper_data[m]["title"].lower().strip());
        if text1==text2:
            return True;
    return False;
    
'''
[Input]
path_of_chromedriver: {string} Path of driver of crome.
       article_title: {string list} List of article titles.
{Return}
 data: {Dictionary list} List with the dat of N papers.
table: {list of integer list} List with N elements (one per paper), each n-th element is a index paper list with the realtion of n-th paper with the others.
'''
def InterReferences(path_of_chromedriver, article_title):
    N=len(article_title);

    cited=[None]*N;
    data=[None]*N;
    for n in range(N):
        print("\nworking:", article_title[n]);
        mydata,myrefs=SST.SemanticScholarReferences(path_of_chromedriver, article_title[n])
        cited[n]=myrefs;
        data[n]=mydata;
    
    table=[None]*N;
    for n in range(N):
        table[n]=[];
        for m in range(N):
            if title_in_paperdata(data[n]["title"],cited[m]):
                table[n].append(m);
    
    return data,table;
