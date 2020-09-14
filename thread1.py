from threading import *
#import threading
def display():
	for i in range(10):
		print('Dusa')
		
t=Thread(target=display)
t.start()
print(current_thread().getName())
for i in range(10):
	print('Satheesh')
print(current_thread().getName())
	
print(current_thread().getName())
