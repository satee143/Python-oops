class Test:
	def __init__(self):
		self.name='dusa'
		self.age=30
		
	def m1(self):
		self.no=2000
		
t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)