class Node():
    def __init__(self):
        self.children = []
        self.data = None
    
    def getChildren(self):
        return self.children
        
    def addChild(self, node):
        self.children.append(node)
    
    def removeChild(self):
        self.children.pop()
    
    def getData(self):
        return self.data
    
    def setData(self, item):
        self.data = item
    
    def printNode(self):
        print (self.data)