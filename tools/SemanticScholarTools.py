#
import tools.StringTools as ST

from semanticscholar import SemanticScholar
from semanticscholar.SemanticScholarException import GatewayTimeoutException
sch = SemanticScholar()

'''
Find basic data of a paper from the title.
[Input]
paperId: paperId
[Return]
 paper_data: {dictionary} Paper data.
'''
def article_dict_from_id(paperId):
    if paperId is None:
        return None
    
    primeiro_artigo = 'OLD'
    
    while primeiro_artigo=='OLD':
        try:
            # Realiza a busca por artigos com o título fornecido
            primeiro_artigo = sch.get_paper(paperId, fields=['title','authors','url','year','referenceCount','citationCount'])
            if primeiro_artigo is None:
                return None
        except GatewayTimeoutException:
            print("Error GatewayTimeoutException. Trying again. ...")
        except Exception as e:
            print(f"Error getting data: {e}")
            return None

    dicdata={
        "paperId":paperId,
        "title":primeiro_artigo['title'],
        "authors":[d["name"] for d in primeiro_artigo['authors']],
        "url":primeiro_artigo['url'],
        "year":primeiro_artigo['year'] if isinstance(primeiro_artigo['year'], int) else 0 ,
        "referenceCount":primeiro_artigo['referenceCount'],
        "citationCount":primeiro_artigo['citationCount']
    };
    return dicdata

def article_dict_from_title(article_title):
    # Realiza a busca por artigos com o título fornecido
    
    resultados = 'OLD'
    
    while resultados=='OLD':
        try:
            resultados = sch.search_paper(article_title)
            if resultados is None:
                return None
        except GatewayTimeoutException:
            print("Error GatewayTimeoutException. Trying again. ...")
        except Exception as e:
            print(f"Error getting data: {e}")
            return None
      
    # Verifica se há resultados e exibe informações do primeiro artigo encontrado
    if resultados:
        primeiro_artigo = resultados[0]
        
        dicdata={
            "paperId":primeiro_artigo['paperId'],
            "title":primeiro_artigo['title'],
            "authors":[d["name"] for d in primeiro_artigo['authors']],
            "url":primeiro_artigo['url'],
            "year":primeiro_artigo['year'] if isinstance(primeiro_artigo['year'], int) else 0 ,
            "referenceCount":primeiro_artigo["referenceCount"],
            "citationCount":primeiro_artigo["citationCount"]
        };
        return dicdata
    else:
        return None



    
'''
Find basic data and references of a paper from the title.
[Input]
       article_title: {string} Article title.
[Return]
 paper_data: {dictionary} Paper data.
 mylistdata: {list of Dictionaries} Paper data list.
'''
def references_dicts_from_id(paperId, append_none=False, func_message=None):
    list_of_dicdata=[];
    
    if paperId is None:
        return [];
    
    if func_message is not None:
        func_message("finding references ...")
    
    res = sch.get_paper(paperId, fields=[ "referenceCount","references"])
    if res is None :
        return []
    
    L=res.referenceCount
    if func_message is not None:
        func_message(f"found {L} references")
    
    for l, referencia in enumerate(res.references):
        
        if referencia["paperId"] is not None:
            dicRef = article_dict_from_id(referencia["paperId"])
        
            list_of_dicdata.append(dicRef)
            
            if func_message is not None:
                func_message(   "\npaperId: "+referencia["paperId"]+"\n"+
                                "title: "+dicRef["title"]+"\n"+
                                f"Obtained {l+1} of {L}")
        else:
            if append_none:
                list_of_dicdata.append(None)
            
            if func_message is not None:
                func_message(   "\npaperId: None\n"+
                                "title: NoUsed\n"+
                                f"Obtained {l+1} of {L}")
    return list_of_dicdata;

def citations_dicts_from_id(paperId, append_none=False, func_message=None):
    list_of_dicdata=[];
    
    if paperId is None:
        return [];
    
    if func_message is not None:
        func_message("finding citations ...")
    
    res = sch.get_paper(paperId, fields=[ "citationCount","citations"])
    if res is None :
        return []
    
    L=res.citationCount
    if func_message is not None:
        func_message(f"found {L} citations")
    
    for l, item_data in enumerate(res.citations):
        
        if item_data["paperId"] is not None:
            dictData = article_dict_from_id(item_data["paperId"])
        
            list_of_dicdata.append(dictData)
            
            if func_message is not None:
                func_message(   "\npaperId: "+item_data["paperId"]+"\n"+
                                "title: "+dictData["title"]+"\n"+
                                f"Obtained {l+1} of {L}")
        else:
            if append_none:
                list_of_dicdata.append(None)
            
            if func_message is not None:
                func_message(   "\npaperId: None\n"+
                                "title: NoUsed\n"+
                                f"Obtained {l+1} of {L}")
    return list_of_dicdata;
