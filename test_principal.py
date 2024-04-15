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
# Others
"Learning Spatiotemporal Features with 3D Convolutional Networks",
# RGB prime
"Multimodal Sleeping Posture Classification",
# RGB-D Carlos Torres paper's
"Sleep Pose Recognition in an ICU Using Multimodal Data and Environmental Feedback",
"Eye-CU: Sleep pose classification for healthcare using multimodal multiview data",
"Summarization of ICU Patient Motion from Multimodal Multiview Videos",
"Deep Eye-CU (DECU): Summarization of Patient Motion in the ICU",
"A Multiview Multimodal System for Monitoring Patient Sleep",
# RGB-D
"Sleep position classification from a depth camera using Bed Aligned Maps",
# RGB-D babies
"RGB-D scene analysis in the NICU",
# presure paper's
"In-Bed Pose Estimation: Deep Learning With Shallow Dataset",
"A Vision-Based System for In-Sleep Upper-Body and Head Pose Classification",
"Video-Based Inpatient Fall Risk Assessment: A Case Study",
"Multimodal In-bed Pose and Shape Estimation under the Blankets"
];

dotfilepath = "salida.dot";

data,table,listref,linkref=RelT.InterReferences(path_of_chromedriver, article_title);
GT.export_graphviz_file_of_references(table,data,listref,linkref,dotfilepath,force=5);


