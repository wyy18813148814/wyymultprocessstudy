#coding:utf-8

import subprocess

# 1.简单的写法
# #开启一个子进程执行系统命令，args,encoding,shell三个参数
# runcmd=subprocess.run('dir C:\intel',encoding='utf-8',shell=True)
#
# print(runcmd)

# 2.定义一个函数调用系统的所有命令
def run_cmd(command):

    runcmd=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='GBK',shell=True)

    if runcmd.returncode==0:
        print('success:')
        print(runcmd.stdout)
    else:
        print('命令执行错误')
        print(runcmd.stderr)

run_cmd('dir C:\\a')