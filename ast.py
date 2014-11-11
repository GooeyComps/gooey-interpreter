from pypeg2 import *
#from make import *

class Make(Namespace):
    grammar = re.compile(r"\w+")


def ast(input):
	return parse(input,Make)