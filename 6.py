class  Test:
	a=10
	def __init__(self):
		self.b=20
'''		
print(Test.a)
print(Test().a)

print(type(Test))
print(type(Test()))'''
x=Test()
x.a=305
print(x.a)
x.a=605
print(x.a)
x.b=1000
print(x.b)
Test.b=4000
print(('dd',Test().b))
Test().b=8000
print(Test.b)