import re

def newStyleFormatting(s):
    s = re.sub( "%%", "{%}",s)
    s = re.sub("%[dfsegxcbwzolmhia]", "{}", s)

    return re.sub("{%}", "%", s)

