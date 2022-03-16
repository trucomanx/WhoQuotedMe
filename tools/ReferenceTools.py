import re 

def title_in_references(title,cited):
    M=len(cited);
    
    text1=re.sub("[^a-zA-Z]+", "",title.lower().strip());
    for m in range(M):
        text2=re.sub("[^a-zA-Z]+", "",cited[m]["title"].lower().strip());
        if text1==text2:
            return True;
    return False;
