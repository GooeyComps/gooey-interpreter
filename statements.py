from pypeg2 import *
from attributes import *
#Starts with a lowercase letter, can only be one word long,
#only contain letters, numbers, or underscore

varnameRegex = re.compile('[a-z][A-Za-z\d\_]*')

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

class GooeyMake(List):
	grammar = [MakeWindow, MakeButton, MakeMenu, MakeMenuItem, MakeTextBox]
	
	
class SetWindow(List):
    grammar = ['set','Set'], blank, attr('varname', word), blank, attr('attributes',WindowAttributeList), '.'
    
class SetButton(List):
    grammar = ['set','Set'], blank, attr('varname', word), blank, attr('attributes',ButtonAttributeList), '.'

class SetMenu(List):
    grammar = ['set','Set'], blank, attr('varname', word), blank, attr('attributes',MenuAttributeList), '.'

class SetMenuItem(List):
    grammar = ['set','Set'], blank, attr('varname', word), blank, attr('attributes',MenuItemAttributeList), '.'

class SetTextBox(List):
    grammar = ['set','Set'], blank, attr('varname', word), blank, attr('attributes',TextBoxAttributeList), '.'

class GooeySet(List):
	grammar = [SetWindow, SetButton, SetMenu, SetMenuItem, SetTextBox]
	
class Line(List):
	grammar = attr("lineAction", [MakeWindow, MakeButton, MakeMenu, MakeMenuItem, MakeTextBox, SetWindow, SetButton, SetMenu, SetMenuItem, SetTextBox]), ";", blank
	
class Return(List):
	grammar = "return", attr("param", optional(blank, word))

class FunctionDefinition(List):
	grammar = "function", blank, attr("funcname", varnameRegex), "(", attr("params", \
	csl(maybe_some(word))), ")", blank, "does", blank, attr("funcaction", csl(maybe_some(Line), blank, Return))

class FunctionCall(List):
    grammar = "run", blank, attr("funcname", varnameRegex), "(", attr("params", csl(maybe_some(word))), ")"
	
class Program(List):
	grammar = maybe_some([MakeWindow, MakeButton, MakeMenu, MakeMenuItem, MakeTextBox, SetWindow, SetButton, SetMenu, SetMenuItem, SetTextBox])
    
    

