#
import tools.SemanticScholarTools as SCT
import tools.GraphvizTools as GT

path_of_chromedriver = (
"/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA"
"/CRAWLER/SeleniumSemanticScraper"
"/ChromeDriver/ChromeDriverLin"
);

article_title="Detection of patient’s bed statuses in 3D using a microsoft kinect";

dotfilepath = "salida.dot";

mycited,mydata=SCT.SemanticScholarCited(path_of_chromedriver, article_title,'Citado por');

GT.export_graphviz_dotfile(mycited,mydata,dotfilepath);


