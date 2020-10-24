def merges(d):
	for i in range(len(d)):
			m=i
			for j in range(i):
				if d[m]>d[j]:
					m=i
				d[i],d[m]=d[m],d[i]
	return d
	
r=[54,26,93,17,77,31,44,55,20]
print(merges(r))
		