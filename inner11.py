class University:
	def __init__(self):
		print('outer class creation')
	def unv_info(self):
		print('outer class method')
		
	class Department:
		def __init__(self):
			print('inner method')
		def m1(self):
			print('University is')
			print('Department is:')
				
u=University()
d=u.Department()
d.m1()
