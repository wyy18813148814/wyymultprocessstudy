#coding:utf-8

from multiprocessing import Process,Queue
import os,time

#创建两个进程，一个负责读，一个负责写

#负责写的进程，（发送数据的进程）
class WriterProcess(Process):
    def __init__(self,xname,mq):
        Process.__init__(self)
        self.name=xname
        self.mq=mq

    def run(self):
        #把多条数据写入到队列中
        print('进程名字:%s,ID:%s;已经启动'%(self.name,os.getpid()))
        for i in range(1,600):
            self.mq.put(i) #writer 进程负责把数据写入Queue
            time.sleep(1)#休眠1秒
        print('进程名字:%s,ID:%s;已经结束'%(self.name,os.getpid()))

#负责从消息队列读数据
class ReaderProcess(Process):
    def __init__(self,xname,mq):
        Process.__init__(self)
        self.name=xname
        self.mq=mq

    def run(self):
        print('进程名字:%s,ID:%s;已经启动'%(self.name,os.getpid()))
        while True:
            #get函数是一个阻塞的函数
            value=self.mq.get(True) #当队列中没有数据，该行代码一直阻塞着
            print(value)
        print('进程名字:%s,ID:%s;已经结束'%(self.name,os.getpid()))

if __name__ == '__main__':
    q=Queue()
    pw=WriterProcess('writer',q)
    pr=ReaderProcess('reader',q)

    #启动两个进程
    pw.start()
    pr.start()

    #让父进程等待子进程结束
    pw.join()
    #pr进程是一个死循环
    pr.terminate() #强制杀死pr进程
    print('父进程结束')