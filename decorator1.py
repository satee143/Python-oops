def decor(func):
    def inner():
        print('*' * 20)
        print('Reading for looks')
        func()

        print('*' * 20)

    return inner()


@decor
def see():
    a=10
    print('Went to Marriage Looks')
