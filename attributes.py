from pypeg2 import *

#   SYMBOL DEFINITIONS: regex, Symbol, str, and Keyword
rgbRegex = re.compile('\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)')
intRegex = re.compile('\d+')
hexRegex = re.compile('\#[A-Fa-f0-9]{6}')
actionPrint = re.compile('"(.*?)"')
optionsRegex = re.compile('\"(.+?)\"|\w+')
textRegex = re.compile('[^"\n](.[^"]*)')
fileRegex = re.compile('.*\.\w+')

class SizeGridValue(str):
	grammar = "(", attr("columns", intRegex), ",", attr("rows", intRegex), ")"

class ColorKeywordValue(Keyword):
	grammar = Enum(K("red"),K("blue"),K("green"))

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

class ButtonTextAttribute(List):
    grammar = 'text', blank, attr('value', QuotedText)

class ButtonActionAttribute(List):
    grammar = 'action', blank, attr("value", word)

class ButtonAttribute(List):
    grammar = [attr('color', ButtonColorAttribute), attr('size', ButtonSizeAttribute), attr('position', ButtonPositionAttribute), attr('text', ButtonTextAttribute), attr('action', ButtonActionAttribute)]

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

#Accept anything after options
class MenuItemOptionsAttribute(List):
    grammar = 'options', blank, attr('value', maybe_some([word, MenuItemTerminal]))

class MenuItemTextAttribute(List):
    grammar = 'text', blank, attr('value', QuotedText)

class MenuItemAttribute(List):
    grammar = [attr('options', MenuItemOptionsAttribute), attr('text', MenuItemTextAttribute)]

class MenuItemAttributeList(List):
    grammar = csl(MenuItemAttribute)


#   TEXTBOX
class TextBoxTextAttribute(List):
    grammar = 'text', blank, attr('value', QuotedText)

class TextBoxPositionAttribute(List):
    grammar = 'position', blank, attr('value', [PositionKeywordValue, PositionGridValue])

class TextBoxAttribute(List):
    grammar = [attr('text', TextBoxTextAttribute), attr('position', TextBoxPositionAttribute)]

class TextBoxAttributeList(List):
    grammar = csl(TextBoxAttribute)


#   IMAGE
class ImageSourceAttribute(List):
    grammar = 'source', blank, attr('value', SourceFileText)

class ImagePositionAttribute(List):
    grammar = 'position', blank, attr('value', [PositionKeywordValue, PositionGridValue])

class ImageAttribute(List):
    grammar = [attr('source', ImageSourceAttribute), attr('position', ImagePositionAttribute)]

class ImageAttributeList(List):
    grammar = csl(ImageAttribute)


class AttributeList(List):
    grammar = [WindowAttributeList, ButtonAttributeList, MenuAttributeList, MenuItemAttributeList, TextBoxAttributeList, ImageAttributeList]

'''
#Various regex to catch different value types


#Colors

'''
class ColorRGBValue(str):
	grammar = rgbRegex

class ColorHEXValue(str):
	grammar = hexRegex

#Positions
class PositionGridValue(str):
	grammar = "(", intRegex, ",", intRegex, ")"

class PositionKeywordValue(Keyword):
	grammar = Enum(K("bottom"),K("top"), K("middle"), K("left"), K("right"))

class PositionAttribute:
    grammar = "position", blank, attr("value", [PositionGridValue,PositionKeywordValue])


class ColorAttribute:
	grammar = "color", blank, attr("value", [ColorRGBValue, ColorHEXValue, ColorKeywordValue])

#Sizes
class SizeKeywordValue(Keyword):
	grammar = Enum(K("small"),K("large"))

class SizeGridValue(str):
	grammar = "(", intRegex, ",", intRegex, ")"

class SizeIntValue(str):
	grammar = intRegex

class SizeAttribute:
	grammar = "size", blank, attr("value", [SizeKeywordValue, SizeIntValue, SizeGridValue])

#Parent window for a Button
class WindowAttribute:
	grammar = "window", blank, attr("value", name())

#Text
class TextAttribute:
	grammar = "text", blank, "\"", attr("value", textRegex), "\""

#Menu Options
class MenuOptionsAttribute:
	grammar = "options", blank, attr("options", maybe_some(optionsRegex))

#Button action (name of a function):
class ActionAttribute:
	grammar = "action", blank, attr("value", word), optional(attr("text", actionPrint)), optional(attr("color", [ColorRGBValue, ColorHEXValue, ColorKeywordValue]))

#Wrap as Attribute object and put into AttributeList
class Attribute:
	grammar = [attr("color", ColorAttribute), attr("size", SizeAttribute), attr("window",WindowAttribute), attr("text", TextAttribute), attr("action",ActionAttribute), attr("options",MenuOptionsAttribute), attr("position",PositionAttribute)]

class AttributeList(List):
	grammar = csl(Attribute)
 
