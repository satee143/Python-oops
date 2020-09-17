from threading import *
import time
class Myclass(Thread):
	def run(self):
		for i in range(10):
			print('S')
			time.sleep(1)
			print(current_thread().name)
t=Myclass()
t.start()
for i in range(10):
	print('D')
	print(current_thread().getName())
	
