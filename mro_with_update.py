class U():
	pass
#	def m1(self):
#		print('method of U ')
class A(U):
	pass
	#def m1(self):
#		print('method of A ')

class B():
	def m1(self):
		print('method of B ')

class C():
	#pass
	def m1(self):
		print('method of C ')
class X(A,B):
	pass
	#def m1(self):
#		print('method of X ')

class Y(C):

	def m1(self):
		print('method of Y ')
class P(X,Y,C):
	pass
#	def m1(self):
#		print('method of X ')
		
		
		
d=P()
print(P.mro())
d.m1()