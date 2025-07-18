# 字典
def use_dict():
    d = {'zhangsan':30,'lisi':45}
    print(d['zhangsan'])
    
    # 插入值
    d['zhangsan'] = 56
    print(d['zhangsan'])
    
    # 判断key是否存在
    print('zhangsan' in d)
    
    print(d.get('zhangsan'))
    # 不存在返回 None
    print(d.get('Thomas'))
    # 不存在返回 自定义值 -1
    print(d.get('Thomas',-1))

    # 删除 key
    d.pop('zhangsan')

def use_set():
    # 定义set的两种方式
    s = {1,2,3}
    s = set([1, 2, 3])
    print(s)

    # 重复元素自动过滤
    s1 = {1,2,2,3,4,4,'zhangs'}
    print(s1)

    # 添加元素
    s1.add(5)
    print(s1)

    # 删除元素
    s1.remove('zhangs')
    print(s1)

use_set()
    