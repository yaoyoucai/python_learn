# 函数可以被赋值给变量
f = abs
print(f)

# 赋值后的变量可以作为函数正常使用
print(f(10))

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))