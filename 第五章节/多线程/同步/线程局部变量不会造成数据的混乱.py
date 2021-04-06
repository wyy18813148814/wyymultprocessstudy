#coding:utf-8

from threading import *
import time
g_num=0

def run():
    print('当前进程%s,开始启动：%s'%(current_thread().name,time.time()))
    global g_num
    for i in range(5000):
        g_num+=1
    # time.sleep(0.000011)
    print('线程%s,执行之后g_num的值为：%s'%(current_thread().name,g_num))

if __name__ == '__main__':
    threads=[]
    for i in range(5):
        t=Thread(target=run)
        t.start()
        threads.append(t)

    for j in threads:
        j.join()
    print('主线程结束，g_num的值为：%s'%g_num)