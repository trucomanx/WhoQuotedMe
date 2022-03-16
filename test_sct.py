#
import tools.SemanticScholarTools as SCT
import tools.GraphvizTools as GT

# Variables
path_of_chromedriver = (
"/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA"
"/CRAWLER/SeleniumSemanticScraper"
"/ChromeDriver/ChromeDriverLin"
);
#article_title="Detection of patient’s bed statuses in 3D using a microsoft kinect";
article_title="Patient 3D body pose estimation from pressure imaging";
dotfilepath = "salida.dot";

# body
mydata,myrefs=SCT.SemanticScholarCited(path_of_chromedriver, article_title,'Citado por');
GT.export_graphviz_file_of_article(myrefs,mydata,dotfilepath,"svg");


