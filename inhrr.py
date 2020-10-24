class A:
	
	@classmethod
	def m1(cls):
		print('class method')
		
	@staticmethod
	def m2():
		print('static method')
	def m5(self):
		print('instance method')
		
class  B(A):
	def __init__(self):
		self.m5()
	
	def m3(self):
		self.m5()
		self.m1()
		self.m2()
		
		
b=B()
b.m3()
	