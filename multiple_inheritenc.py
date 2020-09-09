class A:
	def m1(self):
		print('Class A m1 method')
		
class B:
		def m1(self):
			print('Class B m1 method')
			
		def m2(self):
			print('Class B m2 method')
		
class C(B,A):
	def x(self):
		print('class c x method')
		d=B.m1(self)
		
		
c=C()
c.x()
#c.m1()
#c.m2()
	