from abc import *
class exte(ABC):
	
	@abstractmethod
	def m1(self):
		print('hello')
		
	
e=exte()
e.m1()