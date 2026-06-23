def fun():
    return {'1': 'a', '2': 'b', '3': 'c', '3': 'd'}


x = fun()
print(x)
print(type(x))


def funA():
    return {1, 2, 3, 4, 5, 4, 1}


y = funA()
print(y)
print(type(y))


def funA():
    return [1, 2, 3, 4, 5, 4, 1]


z = funA()
print(z)
print(type(z))


def funA():
    return (1, 2, 3, 4, 5, 4, 1)


w = funA()
print(w)
print(type(w))

