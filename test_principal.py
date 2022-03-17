#
import tools.StringTools as ST
import tools.RelationsTools as RelT
import tools.GraphvizTools as GT

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

dotfilepath = "salida.dot";

data,table=RelT.InterReferences(path_of_chromedriver, article_title);
GT.export_graphviz_file_of_references(table,data,dotfilepath);

