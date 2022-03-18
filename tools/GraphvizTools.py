import tools.StringTools as ST
from graphviz import Digraph
#    pip install graphviz

'''
Generates a *.dot file (dotfilepath) with the relation of a paper (paper_data) and yours references (mylistdata)
[Inputs]
 mylistdata: {list of Dictionaries} Paper data list.
 paper_data: {dictionary} Paper data.
dotfilepath: {string} File path of *.dot output Graphviz file.
      width: {Integer} Number of characteres in each line of text blocks.
'''
def export_graphviz_file_of_article(mylistdata,paper_data,dotfilepath,width=20):
    f = open(dotfilepath, "w");
    f.write("digraph G {\n");
    f.write("\tnode [ shape=\"Mrecord\" ];\n");
    f.write("\tstyle = filled;\n");
    f.write("\tcolor = lightgrey;\n");
    f.write("\n");
    
    title_format = ST.data_to_string(paper_data,width);

    f.write("\tPRINCIPAL [ label=\""+title_format+"\" href=\""+paper_data["href"]+"\"];\n");
    
    N=len(mylistdata);
    for n in range(N):
        title_format = ST.data_to_string(mylistdata[n],width);
        f.write("\tREF"+str(n)+" [ label=\""+title_format+"\" href=\""+mylistdata[n]["href"]+"\"];\n");
    
    for n in range(N):
        f.write("\tREF"+str(n)+"-> PRINCIPAL  [ style=dashed];\n");
    
    f.write("\n");
    f.write("}\n");
    f.close();


def private_file_of_references_1(f,table,paper_data,width,sep=""):
    N=len(paper_data);
    for n in range(N):
        title_format = ST.data_to_string(paper_data[n],width);
        f.write(sep+"\tARTICLE"+str(n)+" [ label=\""+title_format+"\" href=\""+paper_data[n]["href"]+"\"];\n");
        
    for n in range(N):
        M=len(table[n]);
        for m in range(M):
            f.write(sep+"\tARTICLE"+str(n)+" -> ARTICLE"+str(table[n][m])+"  [ style=dashed];\n");
    
def private_file_of_references_2(f,listref,linkref,width,force,sep):
    N=len(listref);
    for n in range(N):
        if len(linkref[n])>=force:
            title_format = ST.data_to_string(listref[n],width);
            f.write(sep+"\tPAPER"+str(n)+" [ label=\""+title_format+"\" href=\""+listref[n]["href"]+"\"];\n");
            for m in range(len(linkref[n])):
                f.write(sep+"\tPAPER"+str(n)+" -> ARTICLE"+str(linkref[n][m])+"  [ style=dashed];\n");
            
    
'''
Generates a *.dot file (dotfilepath) with the relations of N papers (paper_data).
[Inputs]
      table: {list of list of integers} List with N elements (one per paper), each n-th element is a index paper list with the realtion of n-th paper with the others.
 paper_data: {Dictionary list} List with the dat of N papers.
dotfilepath: {string} File path of *.dot output Graphviz file.
      force: {Integer} If force > 0 indicates that accept referencias with [force] links at least.
             In other cases no one reference is included.
      width: {Integer} Number of characteres in each line of text blocks.
'''
def export_graphviz_file_of_references(table,paper_data,listref,linkref,dotfilepath,width=20,force=2):
    f = open(dotfilepath, "w");
    f.write("digraph G {\n");
    f.write("\tnode [ shape=\"box\" ];\n");
    f.write("\tstyle = filled;\n");
    f.write("\tcolor = lightgrey;\n");
    f.write("\n");
    
    
    f.write("\tsubgraph cluster_0{\n");
    
    f.write("\t\tnode [ shape=\"Mrecord\" ];\n");
    private_file_of_references_1(f,table,paper_data,width,"\t");
    f.write("\t}\n");
    
    if force>0:
        private_file_of_references_2(f,listref,linkref,width,force,"");
    
    f.write("\n");
    f.write("}\n");
    f.close();
    
