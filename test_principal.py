#
import tools.SemanticScholarTools as SGT
import tools.ReferenceTools as RT
import tools.GraphvizTools as GT
import tools.StringTools as ST

path_of_chromedriver = ST.path_of_file(__file__)+"/ChromeDriver/ChromeDriverLin";

article_title = [
"Patient 3d body pose estimation from pressure imaging",
"A Multi-view RGB-D Approach for Human Pose Estimation in Operating Rooms",
"Patient MoCap: Human pose estimation under blanket occlusion for hospital monitoring applications",
"Patient-Specific Pose Estimation in Clinical Environments",
"Estimating pose from pressure data for smart beds with deep image-based pose estimators",
"Detection of patient’s bed statuses in 3D using a microsoft kinect",
"Body Pose Analysis using CNN and Pressure Sensor Array Data"
];

N=len(article_title);

cited=[None]*N;
data=[None]*N;
for n in range(N):
    print("\nworking:", article_title[n]);
    mydata,myrefs=SGT.SemanticScholarCited(path_of_chromedriver, article_title[n])
    cited[n]=myrefs;
    data[n]=mydata;


table=[None]*N;
for n in range(N):
    table[n]=[];
    for m in range(N):
        if RT.title_in_paperdata(data[n]["title"],cited[m]):
            table[n].append(m);

dotfilepath = "salida.dot";
GT.export_graphviz_file_of_references(table,data,dotfilepath);

