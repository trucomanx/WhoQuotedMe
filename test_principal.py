#
import tools.StringTools as ST
import tools.RelationsTools as RelT
import tools.GraphvizTools as GT
import platform

if   platform.system() == 'Darwin':
    path_of_chromedriver = ST.path_of_file(__file__)+"/ChromeDriver/ChromeDriverMac";
elif platform.system() == 'Windows':
    path_of_chromedriver = ST.path_of_file(__file__)+"/ChromeDriver/ChromeDriverWin.exe";
else:
    path_of_chromedriver = ST.path_of_file(__file__)+"/ChromeDriver/ChromeDriverLin";

article_title = [
"Sleep Pose Recognition in an ICU Using Multimodal Data and Environmental Feedback",
"Summarization of ICU Patient Motion from Multimodal Multiview Videos",
"A Multiview Multimodal System for Monitoring Patient Sleep",
"Multimodal Sleeping Posture Classification",
"Learning Spatiotemporal Features with 3D Convolutional Networks",
"Action Recognition Using Rate-Invariant Analysis of Skeletal Shape Trajectories",
"Deep Eye-CU (DECU): Summarization of Patient Motion in the ICU",
"Eye-CU: Sleep pose classification for healthcare using multimodal multiview data",
"Learning Spatio-Temporal Representations for Action Recognition: A Genetic Programming Approach",
"Sleep position classification from a depth camera using Bed Aligned Maps",
"Weighted sequence loss based spatial-temporal deep learning framework for human body orientation estimation"
];

dotfilepath = "salida.dot";

data,table,listref,linkref=RelT.InterReferences(path_of_chromedriver, article_title);
GT.export_graphviz_file_of_references(table,data,listref,linkref,dotfilepath,force=4);


