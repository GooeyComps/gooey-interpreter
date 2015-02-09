from pypeg2 import *

#   SYMBOL DEFINITIONS: regex, Symbol, str, and Keyword
rgbRegex = re.compile('\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)')
intRegex = re.compile('\d+')
hexRegex = re.compile('\#[A-Fa-f0-9]{6}')
actionPrint = re.compile('"(.*?)"')
optionsRegex = re.compile('\"(.+?)\"|\w+')
textRegex = re.compile('[^"\n](.[^"]*)')

class SizeGridValue(str):
	grammar = "(", attr("columns", intRegex), ",", attr("rows", intRegex), ")"
    
class ColorKeywordValue(Keyword):
	grammar = Enum(K("red"),K("blue"),K("green"))
    
class SizeKeywordValue(Keyword):
	grammar = Enum(K("small"),K("large"))
    
class PositionGridValue(str):
	grammar = "(", attr("x", intRegex), ",", attr("y", intRegex), ")"
    
class Text(str):
	grammar = "\"", word, "\""
    

    
class PositionKeywordValue(Keyword):
	grammar = Enum(K("bottom"),K("top"), K("middle"), K("left"), K("right"))


#   WINDOW
class WindowColorAttribute(List):
    grammar = 'color', blank, attr('value', [rgbRegex, hexRegex, ColorKeywordValue])
    
class WindowSizeAttribute(List):
    grammar = 'size', blank, attr('value', [intRegex, SizeGridValue, SizeKeywordValue])
    
class WindowAttribute(List):
    grammar = [attr('color', WindowColorAttribute), attr('size', WindowSizeAttribute)]
    
class WindowAttributeList(List):
    grammar = csl(WindowAttribute)
    
    
#   BUTTON
class ButtonColorAttribute(List):
    grammar = 'color', blank, attr('value', [rgbRegex, hexRegex, ColorKeywordValue])
    
class ButtonPositionAttribute(List):
    grammar = 'position', blank, attr('value', [PositionKeywordValue, PositionGridValue])
    
class ButtonSizeAttribute(List):
    grammar = 'size', blank, attr('value', [intRegex, SizeGridValue])
    
class ButtonAttribute(List):
    grammar = [attr('color', ButtonColorAttribute), attr('size', ButtonSizeAttribute), attr('position', ButtonPositionAttribute)]
    
class ButtonAttributeList(List):
    grammar = csl(ButtonAttribute)
    
    
#   MENU
class MenuOptionsAttribute(List):
    grammar = 'options', blank, attr('value', maybe_some(word))
    
class MenuAttribute(List):
    grammar = [attr('options', MenuOptionsAttribute)]
    
class MenuAttributeList(List):
    grammar = csl(MenuAttribute)
    
    
#   MENUITEM
class MenuItemTerminal(str):
	grammar = "\"", attr("text", word), "\"", ":", attr("action", word)
	
class MenuItemOptionsAttribute(List):
    grammar = 'options', blank, attr('value', maybe_some([word, MenuItemTerminal]))
    
class MenuItemTextAttribute(List):
    grammar = 'text', blank, attr('value', Text)
    
class MenuItemAttribute(List):
    grammar = [attr('options', MenuItemOptionsAttribute), attr('text', MenuItemTextAttribute)]
    
class MenuItemAttributeList(List):
    grammar = csl(MenuItemAttribute)
    
	
#   TEXTBOX
class TextBoxTextAttribute(List):
    grammar = 'text', blank, attr('value', Text)
    
class TextBoxAttribute(List):
    grammar = [attr('options', TextBoxTextAttribute)]
    
class TextBoxAttributeList(List):
    grammar = csl(TextBoxAttribute)

