import time
def ss(n):
	s=time.time()
	for i in range(len(n)):
		min=i
		for j in range(i+1,len(n)):
			if n[min]>n[j]:
				min=j
		n[i],n[min]=n[min],n[i]
	print(time.time()-s)			
	print(n)
#x=[]	
#n=int(input('enter the length of numbers'))
#for k in range(1,n+1):
#	i=int(input(f'enter {k} number'))
#	x.append(i)
x=[13,2,47,64,25,76,-25,11,32,45,68,86,54,79,85,53]
print(x)

ss(x)