class University:
	def __init__(self,name):
		self.name=name
	def unv_info(self):
		print('university is:',self.name)		
	class Department:
		def __init__(self,dept):
			self.dept=dept
			print('inner method')
		def m1(self):
			print('Department is:',self.dept)
				
u=University('Jntu')
d=u.Department('cse')
u.unv_info()
d.m1()

University('ou').Department('ece').m1()