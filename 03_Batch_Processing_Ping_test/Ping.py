#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import time
from multiprocessing import freeze_support
from multiprocessing.pool import ThreadPool
from datetime import datetime
import os
import subprocess
import ipaddress
import threading
import logging
import sys


# 线程数()
THREADING_NUM = 100
# 线程池
pool = ThreadPool(THREADING_NUM)
# 线程锁
queueLock = threading.Lock()

# 打印消息
def show_info(msg):
    queueLock.acquire()
    print(msg)
    queueLock.release()


def do_ping(target_ip):
    """
    批量ping测试
    """
    try:
        res, res_out = '', ''
        # 判断系统平台，执行对应命令
        if sys.platform == 'linux':
            res = subprocess.run(['ping', '-c', '2', '-W', '1000', target_ip], stdout=subprocess.PIPE)
            res_out = str(res.stdout.decode('gbk'))
        # 判断系统平台，执行对应命令
        elif sys.platform == 'darwin':
            res = subprocess.run(['ping', '-c', '2', '-W', '1000', target_ip], stdout=subprocess.PIPE)
            res_out = str(res.stdout.decode('gbk'))
            # print(res_out)
        # 判断系统平台，执行对应命令
        elif sys.platform == 'win64' or sys.platform == 'win64':
            res = subprocess.run(['ping', '-n', '2', '-w', '1000', target_ip], stdout=subprocess.PIPE)
            res_out = str(res.stdout.decode('gbk'))
        else:
            show_info('不支持该平台系统，非常抱歉!')

        # print(f'res状态是: {res.returncode}')

        if res.returncode == 0:
            show_info('%-20s%-20s' % (target_ip, '*****success*****'))

        else:
            show_info('%-20s%-20s' % (target_ip, 'failure'))

    except Exception as e:
        show_info(e)


def get_ip_list(ip):
    """
    获取ip列表
    """
    temp = ipaddress.ip_network(ip, False).hosts()
    ip_list = []
    for item in temp:
        ip_list.append(str(item))
    # print(ip_list)
    return ip_list

if __name__ == '__main__':
    freeze_support()
    start_time = datetime.now()
    while True:
        # 批量执行ping
        ip_list = get_ip_list(input("输入要ping的网段；例如192.168.1.0/255.255.255.0 :"))
        for ip in ip_list:
            pool.apply_async(do_ping, args=(ip,))
        pool.close()
        pool.join()

    end_time = datetime.now()
    print('All done.总花费时间{:0.2f}s.'.format((end_time - start_time).total_seconds()))
