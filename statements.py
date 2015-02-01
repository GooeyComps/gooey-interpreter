from pypeg2 import *
from attributes import *
#Starts with a lowercase letter, can only be one word long,
#only contain letters, numbers, or underscore
varnameRegex = re.compile('[a-z][A-Za-z\d\_]*')
class VarName(str):
	grammar = varnameRegex

class MakeType(Keyword):
	grammar = Enum(K("Button"), K("Window"), K("Menu"), K("MenuItem"), K("TextBox"))

class Make(List):
	grammar = "make", blank, attr("type", MakeType), blank, attr("varname", VarName), optional("with", attr("attributes",AttributeList)), "."

class GooeySet(List):
	grammar = "set", blank, attr("varname", VarName), attr("attributes",AttributeList), "."

class FunctionDefinition(List):
	grammar = "function", blank, attr("funcname", VarName), "(", attr("params", csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), "."


class FunctionCall(List):
    grammar = "run", blank, attr("funcname", VarName), "(", attr("params", csl(maybe_some(word))), ")", "."

class Program(List):
	grammar = maybe_some([Make, GooeySet, FunctionDefinition, FunctionCall])
