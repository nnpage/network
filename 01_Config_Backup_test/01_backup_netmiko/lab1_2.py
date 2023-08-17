#!/usr/bin/env python3
# encoding: utf-8
"""
@author: donato
@license:
@contact:
@software: tool
@application:
@file: lab1_2.py
@time: 2022/9/3 4:43 PM
@desc:
"""

from netmiko import ConnectHandler

dev = {'device_type': 'huawei',
       'host': '192.168.137.201',
       'username': 'netdevops',
       'password': 'Admin123~',
       'port': 22,
       'session_log': 'netdevops.log'
       }

with ConnectHandler(**dev) as conn:
    # 如需提权 执行enable
    # conn.enable()
    # 将配置放到列表中，实际使用tuple等可以迭代的对象也可以
    config_cmds = ['interface GE1/0/0', 'description cofiged by netmiko', 'commit']
    # 调用send_config_set,赋值config_commands,返回整个交互过程的回显
    config_output = conn.send_config_set(config_commands=config_cmds)
    print('config_output:')
    print(config_output)

    # save_config,无需赋值，netmiko已经处理好它所支持的厂商型号的保存过程,返回整个交互过程的回显
    save_output = conn.save_config()
    print('save_output:')
    print(save_output)
