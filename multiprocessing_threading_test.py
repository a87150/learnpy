import multiprocessing, threading, time

# 定义全局变量Queue
g_queue = multiprocessing.Queue()
c = multiprocessing.cpu_count()

def init_queue():
    print("init g_queue start")

    while not g_queue.empty():
        g_queue.get()

    for _index in range(10):
        g_queue.put(_index)

    print("init g_queue end")

# 定义一个IO密集型任务：利用time.sleep()
def task_io(task_id, g_queue = g_queue):
    print("IOTask[%s] start" % task_id)

    while not g_queue.empty():
        try:
            data = g_queue.get(block=True, timeout=1)
            print("IOTask[%s] get data: %s" % (task_id, data))
            time.sleep(1)
        except Exception as excep:
            print("IOTask[%s] error: %s" % (task_id, str(excep)))

    print("IOTask[%s] end" % task_id)

g_search_list = list(range(10000))
# 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
def task_cpu(task_id, g_queue = g_queue):
    print("CPUTask[%s] start" % task_id)

    while not g_queue.empty():
        try:
            data = g_queue.get(block=True, timeout=1)
            print("CPUTask[%s] get data: %s" % (task_id, data))
            count = 0
            for i in range(10000):
                count += pow(3*2, 3*2) if i in g_search_list else 0
        except Exception as excep:
            print("CPUTask[%s] error: %s" % (task_id, str(excep)))

    print("CPUTask[%s] end" % task_id)

if __name__ == '__main__':
    print("cpu count:", multiprocessing.cpu_count(), "\n")

    print("========== 直接执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_io(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_io, args=(i,)) for i in range(c)]

    for t in thread_list:
        t.start()

    for t in thread_list:
        if t.is_alive():
            t.join()
    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行IO密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_io, args=(i, g_queue)) for i in range(c)]

    for p in process_list:
        p.start()

    for p in process_list:
        if p.is_alive():
            p.join()

    print("结束：", time.time() - time_0, "\n")

    print("========== 直接执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    task_cpu(0)
    print("结束：", time.time() - time_0, "\n")

    print("========== 多线程执行CPU密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    thread_list = [threading.Thread(target=task_cpu, args=(i,)) for i in range(c)]

    for t in thread_list:
        t.start()

    for t in thread_list:
        if t.is_alive():
            t.join()

    print("结束：", time.time() - time_0, "\n")

    print("========== 多进程执行cpu密集型任务 ==========")
    init_queue()
    time_0 = time.time()
    process_list = [multiprocessing.Process(target=task_cpu, args=(i, g_queue)) for i in range(c)]

    for p in process_list:
        p.start()

    for p in process_list:
        if p.is_alive():
            p.join()

    print("结束：", time.time() - time_0, "\n")