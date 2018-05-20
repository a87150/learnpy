def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

from timeit import Timer, timeit

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000))
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000))
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000))
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000))

'''
在上面的例子中，我们对 test1(), test2() 等的函数调用计时，setup 语句可能看起来很奇怪，所以我们详细说明下。
你可能非常熟悉 from ,import 语句，但这通常用在 python 程序文件的开头。
在这种情况下，from __main__ import test1 从 __main__ 命名空间导入到 timeit 设置的命名空间中。
timeit 这么做是因为它想在一个干净的环境中做测试，而不会因为可能有你创建的任何杂变量，以一种不可预见的方式干扰你函数的性能。
'''

print(timeit('x=1'))