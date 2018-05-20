def reader():
    # 模拟从文件读取数据的生成器
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper(g):
    # 循环迭代从reader产生的数据 
    for v in g:
        yield v

def reader_wrapper2(g):
    yield from g

wrap = reader_wrapper2(reader())
for i in wrap:
    print(i)


class SpamException(Exception):
    pass

def writer():
    r = ''
    while True:
        try:
            w = yield r
        except SpamException:
            print('***')
            r = '404 NO'
        else:
            print('>> ', w)
            r = '200 OK'

def writer_wrapper(coro):
    # 手工处理异常被抛给子生成器
    r = ''
    coro.send(None)    # 生成器准备好接收数据
    while True:
        try:
            try:
                x = yield r
            except Exception as e:   # 捕获异常
                coro.throw(e)
            else:
                r = coro.send(x)
        except StopIteration:
            pass

def writer_wrapper2(coro):
    yield from coro


wrap = writer_wrapper(writer())
wrap.send(None)  # "prime" the coroutine
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        r = wrap.send(i)
        print(r)