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
    if M==0:
        return -1;
    
    text1=re.sub("[^a-zA-Z]+", "",title.lower().strip());
    for m in range(M):
        text2=re.sub("[^a-zA-Z]+", "",paper_data[m]["title"].lower().strip());
        if text1==text2:
            return m;
    return -1;


'''
Makes a fusion of two paper data.
[Input]
paper_data1: {dictionary} Paper data.
paper_data2: {dictionary} Paper data.
[Return]
paper_data: {dictionary} Paper data.
'''
def fusion_two_paperdata(paper_data1,paper_data2):
    text1=re.sub("[^a-zA-Z]+", "",paper_data1["title"].lower().strip());
    text2=re.sub("[^a-zA-Z]+", "",paper_data2["title"].lower().strip());
    
    if text1!=text2:
        return None;
    
    paper_data={
        "paperId":"",
        "title":"",
        "authors":[],
        "url":"",
        "year":0,
        "referenceCount":0,
        "citationCount":0
    };
    
    paper_data["title"]=paper_data1["title"].lower().strip();

    if len(paper_data1["paperId"])>len(paper_data2["paperId"]):
        paper_data["paperId"]=paper_data1["paperId"];
    else:
        paper_data["paperId"]=paper_data2["paperId"];
    
    if len(paper_data1["authors"])>len(paper_data2["authors"]):
        paper_data["authors"]=paper_data1["authors"].copy();
    else:
        paper_data["authors"]=paper_data2["authors"].copy();
    
    if paper_data1["year"]>paper_data2["year"]:
        paper_data["year"]=paper_data1["year"];
    else:
        paper_data["year"]=paper_data2["year"];
    
    if len(paper_data1["url"])>len(paper_data2["url"]):
        paper_data["url"]=paper_data1["url"];
    else:
        paper_data["url"]=paper_data2["url"];
    
    if paper_data1["citationCount"]>paper_data2["citationCount"]:
        paper_data["citationCount"]=paper_data1["citationCount"];
    else:
        paper_data["citationCount"]=paper_data2["citationCount"];
        
    if paper_data1["referenceCount"]>paper_data2["referenceCount"]:
        paper_data["referenceCount"]=paper_data1["referenceCount"];
    else:
        paper_data["referenceCount"]=paper_data2["referenceCount"];
    
    return paper_data;

'''
Calculates the internal reference table.
[Inputs]
reference: {List of dictionary list} list of reference list, each reference is a paper data.
paperdata: {Dictionary list} List with the dat of N papers (paper data).
[Return]
    table: {list of integer list} List with N elements (one per paper), each n-th element is a index paper list with the realtion of n-th paper with the others.

'''
def private_InterReferences(paperdata,reference):
    N=len(paperdata)
    table=[None]*N;
    for n in range(N):
        table[n]=[];
        for m in range(N):
            if title_in_paperdata(paperdata[n]["title"],reference[m])>=0:
                table[n].append(m);
    return table;

'''
'''
def private_ExtraReferences(paperdata,reference):
    N=len(paperdata);
    
    #drop paperdata in reference
    for n in range(N):
        for m in range(N):
            if n!=m:
                ID=title_in_paperdata(paperdata[n]["title"],reference[m])
                if(ID>=0):
                    del reference[m][ID];
    
    listref=[];
    linkref=[];
    # drop referencias
    for n in range(N):
        while len(reference[n])>0:
            paper=reference[n][0];
            
            del reference[n][0];
            
            listref.append(paper);
            linkref.append([]);
            linkref[-1].append(n);
            
            for m in range(N):
                if m!=n:
                    ID=title_in_paperdata(paper["title"],reference[m])
                    if(ID>=0):
                        listref[-1]=fusion_two_paperdata(paper,reference[m][ID]);
                        linkref[-1].append(m);
                        
                        del reference[m][ID];
                    
    return listref,linkref

'''
[Input]
       article_title: {string list} List of article titles.
{Return}
paperdata: {Dictionary list} List with the dat of N papers (paper data).
    table: {list of integer list} List with N elements (one per paper), each n-th element is a index paper list with the realtion of n-th paper with the others.
'''
def InterReferences(article_title, func_message=None):
    N=len(article_title);

    reference=[None]*N;
    paperdata=[None]*N;
    for n in range(N):
        if func_message is not None:
            func_message("\n========="+"="*len(article_title[n]));
            func_message("\nworking: "+article_title[n]);
            
        mydata = SST.article_dict_from_title(article_title[n])
        myrefs=SST.references_dicts_from_id(mydata["paperId"], func_message=func_message)
        reference[n]=myrefs;
        paperdata[n]=mydata;
    
    '''
    calculando table
    '''
    table=private_InterReferences(paperdata,reference);
    
    '''
    calculando table2
    '''
    listref,linkref=private_ExtraReferences(paperdata,reference);
    
    return paperdata,table,listref,linkref;
