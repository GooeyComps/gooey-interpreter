from pypeg2 import *

#   SYMBOL DEFINITIONS: regex, Symbol, str, and Keyword
rgbRegex = re.compile('\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)')
intRegex = re.compile('\d+')
hexRegex = re.compile('\#[A-Fa-f0-9]{6}')
actionPrint = re.compile('"(.*?)"')
optionsRegex = re.compile('\"(.+?)\"|\w+')
textRegex = re.compile('[^"\n](.[^"]*)')
fileRegex = re.compile('.*\.\w+')

class ColorKeywordValue(Keyword):
	grammar = Enum(K("red"),K("blue"),K("green"))

class SizeGridValue(str):
	grammar = "(", attr("columns", intRegex), ",", attr("rows", intRegex), ")"

class SizeKeywordValue(Keyword):
	grammar = Enum(K("small"),K("large"))

class PositionGridValue(str):
	grammar = "(", attr("r", intRegex), ",", attr("c", intRegex), ")"

class PositionKeywordValue(Keyword):
	grammar = Enum(K("center"), K("top"), K("bottom"), K("left"), K("right"), K("topcenter"), K("bottomcenter"), K("topleft"), K("topright"), K("bottomleft"), K("bottomright"))

class QuotedText(str):
	grammar = "\"", some(word), "\""

class SourceFileText(str):
	grammar = "\"", fileRegex, "\""




#Attributes to put in List
class ColorAttribute(List):
    grammar = 'color', blank, attr('value', [rgbRegex, hexRegex, ColorKeywordValue])

#TextColor
class TextColorAttribute:
	grammar = 'textColor', blank, attr('value', [rgbRegex, hexRegex, ColorKeywordValue])

class SizeAttribute(List):
    grammar = 'size', blank, attr('value', [intRegex, SizeGridValue, SizeKeywordValue])

class PositionAttribute(List):
    grammar = 'position', blank, attr('value', [PositionKeywordValue, PositionGridValue])

class TextAttribute(List):
    grammar = 'text', blank, attr('value', QuotedText)

class ActionAttribute(List):
    grammar = 'action', blank, attr("value", word)

class TitleAttribute(List):
    grammar = 'title', blank, attr('title', QuotedText)

#Font
class FontAttribute:
    grammar = "font", blank, "\"", attr("value", textRegex), "\""

#   MENUITEM DOES THIS GO IN ATTRIBUTE CLASS????
class MenuItemTerminal(str):
	grammar = "\"", attr("text", word), "\"", ":", attr("action", word)

#Accept anything after options
class MenuItemOptionsAttribute(List):
    grammar = 'options', blank, attr('value', maybe_some([word, MenuItemTerminal]))

#   IMAGE
class ImageSourceAttribute(List):
    grammar = 'source', blank, attr('value', SourceFileText)

#   CHECKBOXES HOW TO CONDENSE? OR USE NEW KEYWORD?
class CheckboxesOptionsAttribute(List):
    grammar = 'options', blank, attr('options', some(optional("*"), QuotedText))

#  RADIOBUTTONS
class RadioButtonsOptionsAttribute(List):
    grammar = 'options', blank, attr('options', some(optional("*"), QuotedText))


#Wrap as Attribute object and put into AttributeList
class Attribute:
	grammar = [attr("color", ColorAttribute), attr("textColor", TextColorAttribute), attr("size", SizeAttribute), attr("position", PositionAttribute), attr("text", TextAttribute), attr("action", ActionAttribute), attr("title", TitleAttribute), attr("font", FontAttribute), attr("options", MenuItemOptionsAttribute), attr("source", ImageSourceAttribute)]

class AttributeList(List):
 	grammar = csl(Attribute)
