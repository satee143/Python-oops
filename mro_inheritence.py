class A():
	def m1(self):
		print('method of A ')
class X():
	def m1(self):
		print('method of X ')
		
class B(X):
	pass
	#def m1(self):
#		print('method of B ')
class C(B,A):
	pass
	#def m1(self):
#		print('method of C ')
class D(C):
	pass
	#def m1(self):
#		print('method of D ')
		
d=D()
print(D.mro())
d.m1()