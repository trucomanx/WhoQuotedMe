#
import tools.ScholarGoogleTools as SGT


path_of_chromedriver = "/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA/CRAWLER/SeleniumSemanticScraper/OnlyCrawler/ChromeDriver/ChromeDriverLin";

article_title="Bangla sign language detection using sift and cnn";

mycited,mydata=SGT.ScholarGoogleCited(path_of_chromedriver, article_title,'Citado por');

print("  Title:\t"+mydata["title"]);
print("Authors:\t"+mydata["authors"]);
print("   href:\t"+mydata["href"]);


for dat in mycited:
    print("  Title:["+dat["title"]+"]");
    print("Authors:["+dat["authors"]+"]");
    print("   href:["+dat["href"]+"]");

