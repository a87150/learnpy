import requests
from multiprocessing.dummy import Pool as ThreadPool

def getHtml(url):
    try:
        requests.get(url, timeout = 5)
        print(url)
    except:
        print("wrong: {0}".format(url))

urls = [
'http://huahao917.com',
'http://huanreshebei.net',
'http://hyjsbj.com',
'http://hzjfwj.com',
'http://kitairu.net',
'http://jy-qj.com.cn',
'http://luosi580.com',
'http://lyljbj.com',
'http://psxti.com',
'http://pt-ti.cn']   

pool = ThreadPool(4)
pool.map(getHtml, urls)
pool.close()
pool.join()