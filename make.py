from pypeg2 import *

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

	
	
	