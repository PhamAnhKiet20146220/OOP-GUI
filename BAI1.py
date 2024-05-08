from string import punctuation 

class stringcount:
	def __init__(self,s):
		self.words = s


	def counts(self):
		return len(self.words)

	def countupper(self,s):
		return len([w for w in self.words if w[:len(s)]== s.upper()])




s = ("Cuong","Cuongasdasd","asdasdasd")
a = stringcount(s)
print(a.words)
print("The number of string: ", a.counts())
