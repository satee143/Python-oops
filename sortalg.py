def qs(l):
	for i in range(len(l)):
		for j in range(i):
			if l[i]<l[j]:
				l[i],l[j]=l[j],l[i]
				
	return(l)
	
l=[39,87,63,-32,76,11,4]
print(qs(l))