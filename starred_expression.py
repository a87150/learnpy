def one(a,*b):
    # a是一个普通传入参数，*b是一个非关键字星号参数
    print(b)

one(1,2,3,4,5,6)
#--------
def two(a=1,**b):
    # a是一个普通关键字参数，**b是一个关键字双星号参数
    print(b)

two(a=1,b=2,c=3,d=4,e=5,f=6)

def three(*x):
    # 输出传入的第一个参数
    print(x[0])

lst={"a","b","c","d"}
stri="www.pythontab.com"
three(stri,lst)
three(lst)
three(*stri)

def test_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   for v in args:
      print('Optional argument (*args): ', v)
   for k, v in kwargs.items():
      print('Optional argument %s (*kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
'''
*args和**kwargs语法不仅可以在函数定义中使用，同样可以在函数调用的时候使用。
不同的是，如果说在函数定义的位置使用*args和**kwargs是一个将参数pack的过程，那么在函数调用的时候就是一个将参数unpack的过程了。
下面使用一个例子来加深理解：
'''
def test_args(first, second, third, fourth, fifth):
    print('First argument: ', first)
    print('Second argument: ', second)
    print('Third argument: ', third)
    print('Fourth argument: ', fourth)
    print('Fifth argument: ', fifth)

# Use *args
args = [1, 2, 3, 4, 5]
test_args(*args)
kwargs = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
    'fifth': 5
}

test_args(**kwargs)