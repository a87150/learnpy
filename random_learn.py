import random

f=int(input('个数'))
a=[random.randint(0, 99) * 2 + 1 for x in range(f)]
b=random.sample([i for i in range(1000) if i % 2 == 1], f) 
print(a)
print(b)

import time, string

time_s_2 = time.time()
for _ in range(10**6):
    s2=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

print('method 2:', str(time.time() - time_s_2))

time_s_3 = time.time()
for _ in range(10**6):
    # choices 是3.6的新函数，速度最快，但是返回list
    s3=''.join(random.choices(string.ascii_letters + string.digits, k=10))

print('method 3:', str(time.time() - time_s_3))

random.random()#函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。

random.uniform()#正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。

random.randint()#随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值，python random.randint。

random.choice()#可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。

random.shuffle()#如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。

random.sample()#可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
