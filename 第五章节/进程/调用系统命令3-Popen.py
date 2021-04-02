#encoding=utf-8

import subprocess

# popen=subprocess.Popen('dir C:\\',encoding='utf-8',shell=True)
# print(popen.stdout)

#创建一个子进程执行python命令
popen=subprocess.Popen('python',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)

# 往python命令中传入三条参数
popen.stdin.write('print("hello")\n'.encode('utf-8'))
popen.stdin.write('import os\n'.encode('utf-8'))
popen.stdin.write('print(os.environ)'.encode('utf-8'))

popen.stdin.close()
# 输出结果
out=popen.stdout.read().decode("GBK")
popen.stdout.close()

print(out)