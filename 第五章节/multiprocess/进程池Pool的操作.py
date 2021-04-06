#coding:utf-8

from multiprocessing.pool import Pool
import os,time
import random

#打印进程的信息，并且记录该进程执行的时长
def run(name):
    start=time.time()
    print('进程名字:%s,ID:%s;已经启动'%(name,os.getpid()))

    time.sleep(random.choice([1,2,3,4,5])) #进程随机休眠秒数
    end=time.time()
    print('进程名字:%s,ID:%s;已经结束，耗时：%.2f'%(name,os.getpid(),(end-start)))

if __name__ == '__main__':
    p=Pool(5) #参数默认为CPU的核心数
    for i in range(10):
        #请求得到一个进程，然后异步调用run函数（非阻塞式）
        p.apply_async(run,('process'+str(i),))
    p.close()
    p.join()
    print('父进程结束')
