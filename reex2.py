import re
p=re.compile('ab')
#print(type(p))
m=re.finditer('[a]','abaababa')
for x in m:
	
	print(x.start(),'....',x.end(),'....',x.group())