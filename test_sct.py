#
import tools.SemanticScholarTools as SCT
import tools.GraphvizTools as GT
import tools.StringTools as ST

# Variables
path_of_chromedriver = ST.path_of_file(__file__)+"/ChromeDriver/ChromeDriverLin";

#article_title="Detection of patient’s bed statuses in 3D using a microsoft kinect";
#article_title="Patient 3D body pose estimation from pressure imaging";
#article_title="estimating pose from pressure data for smart beds with deep image-based pose estimators";
article_title="Body Pose Analysis using CNN and Pressure Sensor Array Data";
dotfilepath = "salida.dot";

# body
mydata,myrefs=SCT.SemanticScholarCited(path_of_chromedriver, article_title);
GT.export_graphviz_file_of_article(myrefs,mydata,dotfilepath,"svg");


