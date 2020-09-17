from datetime import date 
from pathlib import Path

p = Path('/storage/emulated/0/oops2/')
#print(type(p))
#for i in p.iterdir():
#	print(i.stat())
#print(date.today())
f = [(i, date.today()- date.fromtimestamp(i.stat()[-2])) for i in p.iterdir()]
print(type(f))
for x,y in f:
	print(type(x))
	#print('{:20} {} days before.'.format(x.name, y.days))