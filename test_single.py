#

import tools.SemanticScholarTools as SST


title="estimating pose from pressure data for smart beds with deep image-based pose estimators"

mydata1 = SST.article_dict_from_title(title);

print(mydata1)

mydata2 = SST.article_dict_from_id(mydata1["paperId"])

print(mydata2)
