# 定义一个装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

def now():
    print('2025-4-20')
# 使用装饰器
now = log(now)

now()
