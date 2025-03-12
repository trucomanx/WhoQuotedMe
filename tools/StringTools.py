import textwrap

'''
[Inputs]
my_string: {string} Long string.
    width: {integer} Number with the break line width.
separator: {string} Separator added in each break line.
[Return]
{string} Return a string with break lines to each <width> characteres,
in each break line is used the <separator>.
'''
def text_width(my_string,width,separator="\n"):
    list_string=textwrap.wrap(my_string, width=width)
    return separator.join(list_string);

'''
Print the information of paper data.
[Inputs]
 paper_data: {dictionary} Paper data.
'''
def print_paper_data(paper_data):
    print("  title:",paper_data["title"]);
    print("authors:",paper_data["authors"]);
    print("   year:",paper_data["year"]);
    print("    url:",paper_data["url"]);
    

def data_to_string(paper_data,width):
    title_format = str(paper_data["year"])+"\\n";
    title_format+= text_width(paper_data["title"],width,"\\n");
    title_format+= "\\n-\\n";
    title_format+= text_width(";".join(paper_data["authors"]),width,"\\n");
    return title_format;
    

import pathlib

'''
[Input]
myfile: {String} path of file.
[Return]
The directory of filepath <myfile>
'''
def path_of_file(myfile):
    return str(pathlib.Path(myfile).parent.resolve())

