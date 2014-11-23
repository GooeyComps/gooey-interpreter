class Token(object):

	def __init__(self):
	    self.token = ""
	    self.type = None
	
	def getToken(self):
	    return self.token
	    
	def setToken(self,data):
	    self.token = data

	def getType(self):
	    return self.type

	def setType(self,data):
	    self.type = data
	    
	def printTokenInfo(self):
	    print (self.token)
	    print (self.type)
	    
