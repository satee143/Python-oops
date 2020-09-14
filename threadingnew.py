from threading import *
def display():
    for i in range(15):
        print('Dusa')
t=Thread(target=display)
t.start()
for i in range(15):
    print('Satheesh Kumar')
