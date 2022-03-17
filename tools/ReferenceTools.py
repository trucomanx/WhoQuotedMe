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
