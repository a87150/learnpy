import os

os.sep #可以取代操作系统特定的路径分隔符。windows下为 '\\'

os.name #字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是 'posix'

os.getcwd()  #得到当前目录路径

os.listdir(path)  #返回指定目录path下的所有文件和目录名

os.remove(path) #删除一个文件

os.rename(old, new)  #重命名

os.makedirs(path)  #创建多级目录

os.mkdir(path) #创建单个目录

os.path.isfile() #判断给出路径是否为一个文件

os.path.isdir()  #判断给出的路径是否为一个目录

os.path.isabs()  #判断给出的路径是否是绝对路径

os.path.exists()  #判断给出的路径是否真实存在

os.path.split(p) #分离给定路径的目录名和文件名

os.path.splitext(p)  #分离文件名与扩展名

os.path.dirname(p) #获取路径名

os.path.basename(p)  #获取文件名

os.path.join(path,name) #连接目录与文件名或目录

os.path.getsize(name) #获得文件大小，如果name是目录返回0L


import shutil

shutil.copyfile(src, dst) #复制数据从src到dst（src和dst均为文件）

shutil.copy2(src, dst) #复制数据从src到dst（src为文件，dst可以为目录）

shutil.copytree(src, dst) #递归复制文件夹，其中，src和dst均为目录，且dst不存在

shutil.move(src, dst) #递归移动一个文件或目录到另一个位置，类似于"mv"命令

shutil.rmtree(path) #递归删除一个目录（有内容，空的均可）

shutil.disk_usage(path) #Return disk usage statistics about the given path as a named tuple with the attributes total, used and free, which are the amount of total, used and free space, in bytes.

