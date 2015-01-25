from pypeg2 import *
from attributes import *

class MakeType(Keyword):
	grammar = Enum(K("Button"), K("Window"))

class Make(List):
	grammar = "make", blank, attr("type", MakeType), blank, attr("varname", name()), optional("with", attr("attributes",AttributeList)), "."

class SetType(Keyword):
	grammar = Enum(K("Button"), K("Window"))

class GooeySet(List):
	grammar = "set", blank, attr("varname", name()), attr("attributes",AttributeList), "."



class Parameter:
	grammar = attr("typing", word, name())

class Parameters(Namespace):
	grammar = optional(csl(Parameter))

class FunctionType(Keyword):
	grammar = Enum(K("Button"))

#class Program(List):
	# grammar = maybe_some([Make,GooeySet,Function])

class Function(List):
	#grammar = "function", blank, attr("funcname", name()), "(", Parameters, ")", blank, "does", blank, attr("funcaction", maybe_some([Make,GooeySet])), "."
	#grammar = "function", blank, attr("funcname", name()), "(", Parameters, ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), "."
	grammar = "function", blank, attr("funcname", name()), "(", optional(Parameters), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), "."

class Program(List):
	grammar = maybe_some([Make,GooeySet, Function])
#	grammar = maybe_some([Make,GooeySet])
