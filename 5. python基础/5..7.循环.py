# 第一种循环方式: for...in
def test_for_in():
    names = ['aa','bb']
    for name in names:
        print('name:',name)

# 第二种循环方式: while
def test_while():
    sum = 0 
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)    

# 测试 break
def test_break():
    n = 1
    while n <= 100:
        if n > 10: # 当n = 11时，条件满足，执行break语句
            break # break语句会结束当前循环
        print(n)
        n = n + 1
    print('END')    

# 测试 continue
def test_continue():
    for value in (range(20)):
        if value % 2 ==0:
            continue
        print(value)

def demo1():
    L = ['Bart', 'Lisa', 'Adam']
    for value in L:
        print(value,sep=",",end="aaa")

demo1()
