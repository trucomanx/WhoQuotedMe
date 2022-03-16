import tools.StringTools as ST
#    pip install graphviz

def export_graphviz_imgfile(mycited,mydata,imgfilepath):
    width=20;
    from graphviz import Digraph
    
    dot = Digraph(comment='One article',node_attr={'shape': 'Mrecord'})
    
    dot.attr(style='filled')
    
    title_format = ST.text_width(mydata["title"],width,"\\n");
    title_format+= "\\n-\\n";
    title_format+= ST.text_width(",".join(mydata["authors"]),width,"\\n");
    

    dot.node('PRINCIPAL',title_format);

    N=len(mycited);
    for n in range(N):
        title_format = ST.text_width(mycited[n]["title"],width,"\\n");
        title_format+= "\\n-\\n";
        title_format+= ST.text_width(", ".join(mycited[n]["authors"]),width,"\\n");
        dot.node("REF"+str(n),title_format);
    
    for n in range(N):
        title_format=ST.text_width(mycited[n]["title"],width,"\\n");
        dot.edge('PRINCIPAL',"REF"+str(n), style='dashed');
    
    print(dot);
    dot.render(imgfilepath, view=True)

