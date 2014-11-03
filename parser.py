import re
import sys
import copy
from stack import *
from node import *
'''
stack = Stack()
for token in tokens:
    if token.data != '.'
        stack.push(token)
    else:
        first = stack.pop()
        expression = Node()
        expression.data = first.data
        while first != ',' or ':'
            expression.addChild(first)
            first = stack.pop()
        
            
            

'''
def parse(tokens):
    
        


def printTree(tree):
    tree.printNode()
    for i in range(len(tree.getChildren())):
        if len(tree.getChildren()[i].getChildren()) > 0:
            printTree(tree.getChildren()[i])
        else:
            tree.getChildren()[i].printNode()