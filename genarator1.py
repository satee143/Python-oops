# l=[i*i for i in range(1000000000)]
# print(l)

g=(i*i for i in range(10000000000))
print(next(g))
print(next(g))
for i in range(10):
    print(i)