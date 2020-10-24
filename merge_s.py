def sorteed(l):
	if len(l)>1:
		mid=len(l)//2
		le=l[:mid]
		ri=l[mid:]
		sorteed(le)
		sorteed(ri)
		
	
		i=j=k=0
		while i<len(le) and j<len(ri):
			if le[i]<ri[j]:
				l[k]=le[i]
				i+=1
			else:
				l[k]=ri[j]
				j+=1
			k+=1
				
		while i<len(le):
				l[k]=le[i]
				i+=1
				k+=1
				
		while j<len(ri):
				l[k]=ri[j]
				j+=1
				k+=1
				
	return l
			
l=[54,26,93,17,77,31,44,55,20]
sorteed(l)
print(sorteed(l))