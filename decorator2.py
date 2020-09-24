def decor(func):
    def enhanc(a,b):
        print('*'*50)
        print("The first argument is :",a)
        print("The second argument is :",b)
        print(f'The sum of {a} and {b} is {a + b}')
        func(a,b)
    return enhanc


@decor
def add(a,b):
    print(a+b)
add(10,20)
