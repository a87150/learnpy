'''
每次通过实例访问属性，都会经过__getattribute__函数。而当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。
这就好像是一个异常处理函数。每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。
需要注意的是，当使用类访问不存在的变量是，不会经过__getattr__函数。而descriptor不存在此问题，只是把instance标识为none而已。
'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        #print(path)
        print(self._path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


class C(object):
    a = 'abc'

    #无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常）
    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)
        return "haha"

    #当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。
    def __getattr__(self, attr):
        print("__getattr__() is called")
        return attr + " from getattr"

    #只用在descriptor中。可以通过owner class或者instance来访问属性。
    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def foo(self, x):
        print(x)

class C2(object):
    d = C()

if __name__ == '__main__':
    c = C()
    c2 = C2()
    print(c.a)
    print(c.zzzzzzzz)
    c2.d
    print(c2.d.a)