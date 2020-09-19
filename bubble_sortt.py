def bs(n):
	for i in range(len(n)-1):
		for j in range(len(n)-1):
			if n[j]>n[j+1]:
				n[j+1],n[j]=n[j],n[j+1]
				
	print(n)
	
	
x=[13,2,47,64,25,76,-25,11,32]
print(x)
bs(x)