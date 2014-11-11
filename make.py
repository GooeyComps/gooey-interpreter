from pypeg2 import *
from attributes import *

class MakeType(Keyword):
	grammar = Enum(K("Button"), K("Window"))
	
class Make(List):
	grammar = "make", blank, attr("type", MakeType), blank, attr("varname", name()), optional("with", attr("attributes",AttributeList)), "."
	
