import subprocess

p = subprocess.Popen('Ping baidu.com', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in p.stdout.readlines():

    print(line.decode('gb2312'))

retval = p.wait()