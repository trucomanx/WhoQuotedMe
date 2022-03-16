import textwrap
splitme = "Hello this is a long string and it may contain an extremelylongwordlikethis bye!"

def text_width(splitme,width,separator="\n"):
    list_string=textwrap.wrap(splitme, width=width)
    return separator.join(list_string);
