def func():
    print("a")
    yield
    print("b")
    yield
    print("c")

def a():
    co = func()
    next(co)
    print('in function A')
    next(co)

a()