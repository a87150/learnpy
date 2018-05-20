from functools import reduce

def prod(L):
    def de(x,y):
        return x*y
    if L is not None:
        return reduce(de,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def count():
    def f(j):
        def g():
            return j*j
        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()# 等于list里的三个 g
print(f1(),f2(),f3())

def counter(x):
    a = [x]
    def inner():
        a[0] += 1
        return a[0]
    return inner

c1 = counter(10)
c2 = counter(20)
print(c1(), c2(), c1(), c2())
# 可以看到，即使离开了counter函数，变量a还是一直存在。