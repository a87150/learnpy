from functools import wraps

def log(func):
    if callable(func):
    #如果接收的参数是函数，则用两层嵌套
        @wraps(func)
        def wrapper(*args,**kw):
            #定义一个包装函数，接收任意参数，返回值为要包装的函数的执行结果
            print('begin call %s()' % (func.__name__))
            func(*args,**kw)
            print('end call %s()' % (func.__name__))
        return wrapper

    else:
    #如果接收的参数是字符串，则用三层嵌套
        def decorator(trueFunc):
            @wraps(trueFunc)
            def wrapper(*args,**kw):
                #定义一个包装函数，接收任意参数，返回值为要包装的函数的执行结果
                print('begin %s %s()' % (func,trueFunc.__name__))
                trueFunc(*args,**kw)
                print('end %s %s' % (func,trueFunc.__name__))
            return wrapper
        return decorator

@log
def f1():
    print('这是F1函数')

@log('excute')
def f2():
    print('这是F2函数')

def cache(func):
    caches = {}
    @wraps(func)
    def wrap(*args):
        if args not in caches:
            print(caches, args)
            caches[args] = func(*args)
        return caches[args]
    return wrap

@cache
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__  == '__main__':
    f1()
    f2()
    fib(5)