from pypeg2 import *
from attributes import *

class MakeType(Keyword):
	grammar = Enum(K("Button"), K("Window"), K("Menu"), K("MenuItem"), K("TextBox"))

class Make(List):
	grammar = "make", blank, attr("type", MakeType), blank, attr("varname", name()), optional("with", attr("attributes",AttributeList)), "."

class GooeySet(List):
	grammar = "set", blank, attr("varname", name()), attr("attributes",AttributeList), "."

class FunctionDefinition(List):
	grammar = "function", blank, attr("funcname", name()), "(", attr("params", csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), "."

class FunctionCall(List):
    grammar = "run", blank, attr("funcname", name()), "(", attr("params", csl(maybe_some(word))), ")", "."

class Program(List):
	grammar = maybe_some([Make, GooeySet, FunctionDefinition, FunctionCall])
