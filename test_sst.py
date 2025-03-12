#
import tools.SemanticScholarTools as SST
import tools.GraphvizTools as GT

# Variables
article_title="estimating pose from pressure data for smart beds with deep image-based pose estimators";

dotfilepath = "salida.dot";


art_dict = SST.article_dict_from_title(article_title)

refs_list = SST.references_dicts_from_id(art_dict["paperId"],func_message=print);
cits_list = SST.citations_dicts_from_id(art_dict["paperId"],func_message=print);


GT.graphviz_file_of_references_and_article(refs_list,art_dict,dotfilepath);
GT.view_dot_graphvizonline(dotfilepath)


