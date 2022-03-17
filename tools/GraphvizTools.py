import tools.StringTools as ST
from graphviz import Digraph
#    pip install graphviz


'''
Generates a *.dot file (dotfilepath) with the relation of a paper (paper_data) and yours references (mylistdata)
[Inputs]
 mylistdata: {list of Dictionaries} Paper data list.
 paper_data: {dictionary} Paper data.
dotfilepath: {string} File path of *.dot output Graphviz file.
    formato: {string} Format of additional binary file.
      width: {Integer} Number of characteres in each line of text blocks.
'''
def export_graphviz_file_of_article(mylistdata,paper_data,dotfilepath,formato='svg',width=20):
    dot = Digraph(format=formato, comment='One article',node_attr={'shape': 'Mrecord'})
    
    dot.attr(style='filled')
    title_format = str(paper_data["date"])+"\\n";
    title_format+= ST.text_width(paper_data["title"],width,"\\n");
    title_format+= "\\n-\\n";
    title_format+= ST.text_width(",".join(paper_data["authors"]),width,"\\n");
    
    dot.node('PRINCIPAL',title_format);
    #dot.node('PRINCIPAL',title_format,href=paper_data["href"]);

    N=len(mylistdata);
    for n in range(N):
        title_format = str(mylistdata[n]["date"])+"\\n";
        title_format+= ST.text_width(mylistdata[n]["title"],width,"\\n");
        title_format+= "\\n-\\n";
        title_format+= ST.text_width(", ".join(mylistdata[n]["authors"]),width,"\\n");
        dot.node("REF"+str(n),title_format,href=mylistdata[n]["href"]);
    
    for n in range(N):
        title_format=ST.text_width(mylistdata[n]["title"],width,"\\n");
        dot.edge("REF"+str(n),'PRINCIPAL', style='dashed');
    
    #print(dot);
    
    dot.render(dotfilepath);


'''
Generates a *.dot file (dotfilepath) with the relations of N papers (paper_data).
[Inputs]
      table: {list of list of integers} List with N elements (one per paper), each n-th element is a index paper list with the realtion of n-th paper with the others.
 paper_data: {Dictionary list} List with the dat of N papers.
dotfilepath: {string} File path of *.dot output Graphviz file.
    formato: {string} Format of additional binary file.
      width: {Integer} Number of characteres in each line of text blocks.
'''
def export_graphviz_file_of_references(table,paper_data,dotfilepath,formato='svg',width=20):
    dot = Digraph(format=formato, comment='many article',node_attr={'shape': 'Mrecord'})
    
    dot.attr(style='filled')
    
    N=len(paper_data);
    for n in range(N):
        title_format = str(paper_data[n]["date"])+"\\n";
        title_format+= ST.text_width(paper_data[n]["title"],width,"\\n");
        title_format+= "\\n-\\n";
        title_format+= ST.text_width(",".join(paper_data[n]["authors"]),width,"\\n");
        dot.node("ARTICLE"+str(n),title_format,href=paper_data[n]["href"]);
        
    for n in range(N):
        M=len(table[n]);
        for m in range(M):
            dot.edge("ARTICLE"+str(n),"ARTICLE"+str(table[n][m]), style='dashed');
    
    #print(dot);
    
    dot.render(dotfilepath, view=True)
