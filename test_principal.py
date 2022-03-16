#
import tools.SemanticScholarTools as SGT
import tools.ReferenceTools as RT
import tools.GraphvizTools as GT

path_of_chromedriver = \
"/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA/CRAWLER/SeleniumSemanticScraper/ChromeDriver/ChromeDriverLin";
article_title = [
"Patient 3d body pose estimation from pressure imaging",
"Patient MoCap: Human pose estimation under blanket occlusion for hospital monitoring applications",
"Detection of patient’s bed statuses in 3D using a microsoft kinect",
"Body Pose Analysis using CNN and Pressure Sensor Array Data"
];

cited_text = "Citado por";


N=len(article_title);

cited=[None]*N;
data=[None]*N;
for n in range(N):
    print("\nworking:", article_title[n]);
    mydata,myrefs=SGT.SemanticScholarCited(path_of_chromedriver, article_title[n] ,cited_text)
    cited[n]=myrefs;
    data[n]=mydata;


table=[None]*N;
for n in range(N):
    table[n]=[];
    #print("("+str(n)+")");
    
    for m in range(N):
        if RT.title_in_references(data[n]["title"],cited[m]):
            table[n].append(m);
    #print(table);
    #print("\n");

dotfilepath = "salida.dot";
GT.export_graphviz_file_of_references(table,data,dotfilepath);

