#
import tools.RelationsTools as RelT
import tools.GraphvizTools as GT

articles = [
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

data,table,listref,linkref=RelT.InterReferences(articles,func_message=print);

GT.export_graphviz_file_of_references(table,data,listref,linkref,dotfilepath,force=5);

GT.view_dot_graphvizonline(dotfilepath)
