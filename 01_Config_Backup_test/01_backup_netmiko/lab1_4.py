#!/usr/bin/env python3
# encoding: utf-8
"""
@author: donato
@license:
@contact:
@software: tool
@application:
@file: lab1_4.py
@time: 2022/9/3 5:38 PM
@desc:
"""

from multiprocessing import cpu_count
from getpass import getpass
import paramiko
import re
import socket
import time
import pandas as pd

# 登陆网络设备前期准备
# username = input('enter your username:')
username = "belle"
# password = input('input your password:')
password = "2020senda"
# 打开巡检IP文件
f = open('ip_list.txt', 'r')
# 配置2个空列表，1个字典，列表记录设备认证失败和不可达错误，字典用来保存巡检数据
auth_issue = []
not_reach = []


xunjian_dict = {'交换机IP': [], '交换机名称': [], '软件版本': [], 'CPU利用率': [], '内存利用率': [], '设备温度': [], '电源状态': [], '风扇状态': [],
                '硬件状态': []}

# 登陆设备，巡检设备，巡检结果写入表格
for ips, a in zip(f.readlines(), range(1, 2)):
    try:
        ip = ips.strip()


        # 交换机IP
        output_ip = connect.send_command("dis ip interface brief")
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', output_ip)
        print(ip.group())
        xunjian_dict['交换机IP'].append(ip.group())

        # 交换机名称
        output_hostname = connect.send_command("dis current-configuration | include sysname")
        hostname = re.search(r'sysname (\S+)', output_hostname)
        print(hostname.group(1))
        xunjian_dict['交换机名称'].append(hostname.group(1))

        # 交换机版本
        output_version = connect.send_command("dis version  | i Software")
        version = re.search(r'(Version\s\S+)', output_version)
        print(version.group(1))
        xunjian_dict['软件版本'].append(version.group(1))

        # CPU利用率
        output_cpu = connect.send_command("dis cpu-usage")
        cpu = re.search(r'CPU utilization for five seconds:\s+(\d{1,9}\D)', output_cpu)
        print(cpu.group(1))
        xunjian_dict['CPU利用率'].append(cpu.group(1))

        # 内存利用率
        output_memory = connect.send_command("dis memory-usage")
        memory = re.search(r'Memory Using Percentage Is:\s+(\d{1,9}\D)', output_memory)
        print(memory.group(1))
        xunjian_dict['内存利用率'].append(memory.group(1))

        # 设备温度
        output_Current = connect.send_command("display temperature all")
        Current = re.search(r'\d\d', output_Current)
        print(Current.group())
        xunjian_dict['设备温度'].append(Current.group())

        # 电源状态
        output_Power = connect.send_command("display power")
        if 'Normal' in output_Power:
            xunjian_dict['电源状态'].append('正常')
        else:
            xunjian_dict['电源状态'].append('异常')

        if "Info" in output_Power:
            xunjian_dict['电源状态'].append('*')

        # 风扇状态
        output_Fan = connect.send_command("display fan")
        if 'Normal' in output_Fan:
            xunjian_dict['风扇状态'].append('正常')
        else:
            xunjian_dict['风扇状态'].append('异常')

        # 板卡状态
        output_device = connect.send_command("display device")
        if 'Normal' in output_device:
            xunjian_dict['硬件状态'].append('正常')
        else:
            xunjian_dict['硬件状态'].append('异常')

    # 记录IP地址不可达，认证错误的设备地址
    except paramiko.ssh_exception.AuthenticationException:
        print('user auth failed for' + ip)
        auth_issue.append(ip)
    except socket.error:
        print(ip + 'is not reach')
        not_reach.append(ip)

# 展示pandas数据结构
df = pd.Series(xunjian_dict)
print(df)
# 将字典数据写入excel表格
df = pd.DataFrame(xunjian_dict)
df.to_excel('pandas_output.xlsx', sheet_name='巡检', index=True)