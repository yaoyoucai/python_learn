# list 使用
def use_list():
    classmates = ['zhangsan','lisi','wangwu']
    # 索引访问
    print(classmates[0])
    # 访问最后一个元素
    print(classmates[-1])
        # 访问倒数第二个元素
    print(classmates[-2])


    # 追加元素
    classmates.append('liuliu')
    # 追加到指定的位置
    classmates.insert(2,'aaaa')

    # 删除索引位置为1的元素
    classmates.pop(1)

    # 替换元素
    classmates[-2]='buzhidao'

    # 数据类型也可以不同
    L = ['Apple', 123, True]

    # list元素也可以是另一个list
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print(s[2][1]) 

    # 空list
    list = []

def use_tuple():
    classmates = ('zhangsan','lisi','wangwu')
    print(classmates[-1])

    # 这样定义的是数字 1
    t = (1)
    print('数字',t,sep=" : ")
    
    # 这样定义才是元组
    t = (1,)
    print('元组',t[0],sep=" : ")

def lianxi():
    L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
    ]

    # 打印 Apple
    print(L[0][0])

    # 打印 Python
    print(L[1][1])

    # 打印 Bob
    print(L[2][2])

lianxi()