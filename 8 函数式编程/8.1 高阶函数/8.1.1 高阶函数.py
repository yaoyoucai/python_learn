# 求 绝对值的普通函数
x = abs(-10);
print(x);

# 把函数本身赋值给变量
f = abs;
print(f);
print(f(-56));

# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x)+f(y);
print(add(-5,6,f))

