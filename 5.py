class  Test:

	def __init__(self):
		self.b=20
		self.a=60
		
Test.b=50
d=Test()	
d.b=70	#create instance variable
print(d.b)

#calling through Test class object
print(Test().b)

#changing instance varaible value through Test class object 
Test().b=30# will not change value because there is no corresponding object
print(Test().b)


#changing instance varaible value through test class 
Test.b=30# will create new static varaiable value
print(Test().b)
#Calling through Test class
print(Test.b)#will give error it will call only static varaibles



#creating Test class object d
d=Test()
#calling b varaible through object reference it will check instance varaible available or not if its avbl it will call instance varaible else it will call static variable

print(d.b)
print(Test().b)
print(d.b)
print(d.__dict__)
print(Test.__dict__)	
'''	
print(Test().b)
print(Test.__dict__)
print(Test().b)
print(type(Test()))'''