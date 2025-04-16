## 正常求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

## 
def lazy_sum(*args):
    def sum(name):
        print(name)
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7)

f(1)


"""
 闭包
"""

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3=count()

print(f1())
print(f2())
print(f3())
