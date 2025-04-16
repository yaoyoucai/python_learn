from functools import reduce
def f(x):
    return x * x;
def add(x,y):
    return x+y;
def change(x,y):
    return (x*10)+y;

# f为上面的函数,传入Iterable,通过 f 作用到每一项，然后重新返回Iterator
result = map(f,[1,2,3]);
print(list(result));

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
result = reduce(change,[1,2,3]);
print(result);

# 把string转换成为int
