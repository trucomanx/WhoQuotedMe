import tools.StringTools as ST
from graphviz import Digraph
#    pip install graphviz

def export_graphviz_file_of_article(mycited,mydata,dotfilepath,formato='svg',width=20):
    dot = Digraph(format=formato, comment='One article',node_attr={'shape': 'Mrecord'})
    
    dot.attr(style='filled')
    title_format = str(mydata["date"])+"\\n";
    title_format+= ST.text_width(mydata["title"],width,"\\n");
    title_format+= "\\n-\\n";
    title_format+= ST.text_width(",".join(mydata["authors"]),width,"\\n");
    
    dot.node('PRINCIPAL',title_format);
    #dot.node('PRINCIPAL',title_format,href=mydata["href"]);

    N=len(mycited);
    for n in range(N):
        title_format = str(mycited[n]["date"])+"\\n";
        title_format+= ST.text_width(mycited[n]["title"],width,"\\n");
        title_format+= "\\n-\\n";
        title_format+= ST.text_width(", ".join(mycited[n]["authors"]),width,"\\n");
        dot.node("REF"+str(n),title_format,href=mycited[n]["href"]);
    
    for n in range(N):
        title_format=ST.text_width(mycited[n]["title"],width,"\\n");
        dot.edge("REF"+str(n),'PRINCIPAL', style='dashed');
    
    print(dot);
    
    dot.render(dotfilepath)


def export_graphviz_file_of_references(table,mydata,dotfilepath,formato='svg',width=20):
    dot = Digraph(format=formato, comment='One article',node_attr={'shape': 'Mrecord'})
    
    dot.attr(style='filled')
    
    N=len(mydata);
    for n in range(N):
        title_format = ST.text_width(mydata[n]["title"],width,"\\n");
        title_format+= "\\n-\\n";
        title_format+= ST.text_width(",".join(mydata[n]["authors"]),width,"\\n");
        dot.node("ARTICLE"+str(n),title_format,href=mydata[n]["href"]);
        
    for n in range(N):
        M=len(table[n]);
        for m in range(M):
            dot.edge("ARTICLE"+str(n),"ARTICLE"+str(table[n][m]), style='dashed');
    
    print(dot);
    
    dot.render(dotfilepath, view=True)
