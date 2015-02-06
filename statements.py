from pypeg2 import *
from attributes import *
#Starts with a lowercase letter, can only be one word long,
#only contain letters, numbers, or underscore

#varnameRegex = re.compile('[a-z][A-Za-z\d\_]*')
'''
class VarName(str):
	grammar = varnameRegex

class MakeType(Keyword):
	grammar = Enum(K("Button"), K("Window"), K("Menu"), K("MenuItem"), K("TextBox"))

class Make(List):
	#grammar = "make", blank, attr("type", MakeType), blank, attr("varname", VarName), optional("with", attr("attributes",AttributeList)), "."
	grammar = "make", blank, attr("type", MakeType), blank, attr("varname", VarName), optional("with", attr("attributes",AttributeList))

class GooeySet(List):
	#grammar = "set", blank, attr("varname", VarName), attr("attributes",AttributeList), "."

 	grammar = "set", blank, attr("varname", VarName), attr("attributes",AttributeList)
'''
class Line(List):
	grammar = attr("lineAction", [Make, GooeySet]), ";", blank

class Return(List):
	grammar = "return", attr("param", optional(blank, word))

class FunctionDefinition(List):
	# grammar = "function", blank, attr("funcname", VarName), "(", attr("params", \
	# csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), ";", \
	# blank, optional("returns", blank, word), "."
	# grammar = "function", blank, attr("funcname", VarName), "(", attr("params", \
	# csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(word))), "."
	# grammar = "function", blank, attr("funcname", VarName), "(", attr("params", \
	# csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", [Make, GooeySet])
	grammar = "function", blank, attr("funcname", VarName), "(", attr("params", \
	csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(Line), blank, Return))


class FunctionCall(List):
    grammar = "run", blank, attr("funcname", VarName), "(", attr("params", csl(maybe_some(word))), ")"


class MakeWindow(List):
    grammar = ['make','Make'], blank, attr('type', 'Window'), blank, attr('varname', word), optional( 'with', attr('attributes',WindowAttributeList)), '.'
    
class MakeButton(List):
    grammar = ['make','Make'], blank, attr('type', 'Button'), blank, attr('varname', word), optional( 'with', attr('attributes',ButtonAttributeList)), '.'

class MakeMenu(List):
    grammar = ['make','Make'], blank, attr('type', 'Menu'), blank, attr('varname', word), optional( 'with', attr('attributes',MenuAttributeList)), '.'

class MakeMenuItem(List):
    grammar = ['make','Make'], blank, attr('type', 'MenuItem'), blank, attr('varname', word), optional( 'with', attr('attributes',MenuItemAttributeList)), '.'

class MakeTextBox(List):
    grammar = ['make','Make'], blank, attr('type', 'TextBox'), blank, attr('varname', word), optional( 'with', attr('attributes',TextBoxAttributeList)), '.'


class Program(List):
	grammar = maybe_some([MakeWindow, MakeButton, MakeMenu, MakeMenuItem])
    
    

