from pypeg2 import *
import re
# [make] Button b with color red, size large.
class Command(Keyword):
	grammar = Enum(K("make"))

# make [Button] b with color red, size large.
class ObjType(Keyword):
	grammar = Enum( K("Button"), K("Window"))
	
# make Button [b] with color red, size large
class Var:
	grammar = name()

# make Button b with [color] red, [size] large.
class AttributeType(Keyword):
	grammar = Enum(K("color"),K("size"))
	

RGBtriplet = Symbol("rgb")

RGBtriplet.regex = re.compile('\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)')
	
# make Button b with color [red], size [large].
class ColorAttributeKeywordValue(Keyword):
	grammar = Enum(K("red"),K("blue"))

class Integer:
    grammar = re.compile('\d+')

class SizeAttributeValue(Keyword):
    grammar = re.compile('\d+')

# make Button b with color [red], size [large].
class ColorAttributeRGBValue(Keyword):
	grammar = attr("rgbTriplet",RGBtriplet)
	
# make Button b with [color red], [size large].
class ColorAttribute:
	grammar = attr("attrType", AttributeType), blank, attr("attrValue", [ColorAttributeRGBValue, ColorAttributeKeywordValue])
	
# make Button b with [color red], [size large].
class SizeAttribute:
	grammar = attr("attrType", AttributeType), blank, attr("attrValue", SizeAttributeValue)
    
	
# make Button b with [color red, size large].
class Attributes(List):
	grammar = optional("with", csl([ColorAttribute, SizeAttribute]))
	
	
# [make Button b with color red, size large]
class Make(List):
	grammar = attr("command", Command), blank, attr("objType", ObjType), blank, attr("varname", Var), attr("attributes",Attributes), "."

'''
#Type, keyword, variable name
class var:
    grammar = re.compile('[a-zA-Z][a-zA-Z0-9\_]*')

class floatingPoint:
    grammar = re.compile('\d+\.{0,1}\d+')


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
'''
	
