#coding:utf-8
import subprocess

# return_cmd=subprocess.run('python',stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)



#通过文件句本的方式传参给系统,PIPE是不能传参给系统命令的，subprocess有接口Popen可以传参给系统命令
f = open(r'F:\wyyProject\第五章节\进程\in.txt')
return_cmd=subprocess.run('python',stdin=f,stdout=subprocess.PIPE,shell=True)

print(return_cmd.stdout)
