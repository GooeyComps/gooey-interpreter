from pypeg2 import *
'''
# [make] Button b with color red, size large.
class Command(Keyword):
	grammar = Enum(K("make"))

# make [Button] b with color red, size large.
class ObjType(Keyword):
	grammar = Enum( K("Button"), K("Window") )
	
# make Button [b] with color red, size large
class Var:
	grammar = name()

# make Button b with [color] red, [size] large.
class AttributeType(Keyword):
	grammar = Enum(K("color"),K("size"))
	
# make Button b with color [red], size [large].
class AttributeValue(Keyword):
	grammar = Enum(K("red"),K("blue"),K("small"),K("large"))
	
# make Button b with [color red], [size large].
class Attribute:
	grammar = attr("attrType", AttributeType), blank, attr("attrValue", AttributeValue)
	
# make Button b with [color red, size large].
class Attributes(List):
	grammar = optional("with", csl(Attribute))
	
	
# [make Button b with color red, size large]
class Make(List):
	grammar = attr("command", Command), blank, attr("objType", ObjType), blank, attr("varname", Var), attr("attributes",Attributes), "."
'''

class make:
    name()

#Type, keyword, variable name
class var:
    grammar = re.compile('[a-zA-Z][a-zA-Z0-9\_]*')

class floatingPoint:
    grammar = re.compile('\d+\.{0,1}\d+')

class integer:
    grammar = re.compile('\d+')

class period:
    grammar = re.compile('\.')

class symbols:
    grammar = re.compile('[\=\+\-\/\*]')

class comma:
    grammar = re.compile('\,')

class stringDouble:
    grammar = re.compile('\"[a-zA-Z\s]+\"')

class stringSingle:
    grammar = re.compile('\'[a-zA-Z\s]+\'')

class RGBtriplet:
    grammar = re.compile('\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)')

class HEX:
    grammar = re.compile('\#[A-Fa-f0-9]{6}') 
	
