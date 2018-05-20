try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
# 所有的错误类型都继承自BaseException
# except 不但捕获该类型的错误，还把其子类也“一网打尽”
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
main()
print('END')

# 可以通过配置level达到log分级输出
# 加上filename参数还能很方便的支持输出log到文件，比如
logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='test.log',
        filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')