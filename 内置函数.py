# abs 返回一个数的绝对值
print("abs(-45) : ", abs(-45))
print("abs(100.12) : ", abs(100.12))


# all 如果迭代的元素全部不为 0、''、False或者为空，则返回true，否则返回False
print('all', all(['a', 'b', 'c', 'd']))
print('all', all([]))
print('all', all(['a', '', 'c', 'd']))


# any 如果迭代的元素全部为空、0、false，则返回false，如果不都为空、0、false，则返回true
print('any', any(['a', 'b', 'c', 'd']))
print('any', any([]))
print('any', any(['a', '', 'c', 'd']))


# bin 把整数转换成带 "0b" 的二进制字符串
print(bin(3))
print(bin(-13))


# callable 判断对象是否可调用,instances are callable if their class has a __call__() method
a = 1
print('callable', callable(a))


# chr 接受一个整数，返回对应的 Unicode character
print('chr', chr(a))


# ord 接受一个 Unicode character，返回对应的 code
print('ord', ord('o'))


# max 返回一个 iterable 对象或者多个参数中最大的一个项，key 可以指定一个函数分别作用于每个参数
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
print(max(set(test), key=test.count))


# hex 进制转换
n1 = 255
n2 = 1000
print(hex(n1),hex(n2),
    oct(n1),oct(n2),
    bin(n1),bin(n2))


# sorted 排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)

l=[7, -8, 5, 4, 0, -2, -5, 11]
# x < 0 的意思是按 true false 来分组
print(sorted(l, key=lambda x: (x < 0, x), reverse=True))
# -x 的意思是正数和负数转换，类似取反
print(sorted(l, key=lambda x: (x if x > 0 else -x)))


# zip 接受多个 iterable 对象作为参数，将对象中对应的元素打包成一个个 tuple，然后返回由这些 tuple 组成的 iterator
# 若传入参数的长度不等，则返回的 iterator 的长度和参数中长度最短的对象相同
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zipped = zip(*a)
print(list(zipped))