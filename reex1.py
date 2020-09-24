import re
p=re.compile('ab')
#print(type(p))
m=p.finditer('abaababa')
for x in m:
	
	print(x.start(),'....',x.end(),'....',x.group())