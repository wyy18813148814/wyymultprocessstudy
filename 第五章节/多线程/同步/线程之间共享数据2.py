#coding:utf-8

#主线程中的全局变量，作为所有子线程的共享数据

from threading import Thread
import time,os

#定义一个全局变量
g_num=0

def run1():
    global g_num
    time.sleep(1)
    for i in range(10):
        g_num+=1
    print('线程1，执行之后的结果为：%d'%g_num)
def run2():
    global g_num

    print('线程2，执行之后的结果为：%d'%g_num)

if __name__ == '__main__':
    t1=Thread(target=run1)
    t2=Thread(target=run2)

    # t2.start()
    t1.start()
    time.sleep(1)
    t2.start()

    print('主线程结束，全局变量g_num的值是：%s'%g_num)
