#
import tools.SemanticScholarTools as SGT


path_of_chromedriver = \
"/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA/CRAWLER/SeleniumSemanticScraper/ChromeDriver/ChromeDriverLin";
article_title = [
"Patient 3d body pose estimation from pressure imaging",
"Bangla sign language detection using sift and cnn",
"Deep residual learning for image recognition",
"Patient MoCap: Human pose estimation under blanket occlusion for hospital monitoring applications",
"Detection of patient’s bed statuses in 3D using a microsoft kinect",
"Body Pose Analysis using CNN and Pressure Sensor Array Data"
];

cited_text = "Citado por";


N=len(article_title);

cited=[None]*N;
data=[None]*N;
for n in range(N):
    print("\n");
    print(article_title[n]);
    mycited,mydata=SGT.SemanticScholarCited(path_of_chromedriver, article_title[n] ,cited_text)
    cited[n]=mycited;
    data[n]=mydata;



print(cited)
print(data)




'''
table=[None]*N;
for i in range(N):
    table[i]=[];
    print("["+str(i)+"]");
    for j in range(N):
        print("\n");
        print(data[i]["title"]);
        print(cited[j]["title"]);
        if data[i]["title"]==cited[j]["title"]:
            table[i].append(j);
            print(j);
    print("\n");
'''

