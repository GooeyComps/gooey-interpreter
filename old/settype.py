from pypeg2 import *
from attributes import *

class SetType(Keyword):
	grammar = Enum(K("Button"), K("Window"))
	
class GooeySet(List):
	grammar = "set", blank, attr("varname", name()), attr("attributes",AttributeList), "."

	
