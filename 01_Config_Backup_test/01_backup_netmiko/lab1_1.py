#!/usr/bin/env python3
# encoding: utf-8
"""
@author: donato
@license:
@contact:
@software: 基于netmiko的批量配置备份
@application:
@file: lab1_h3c.py
@time: 2022/9/3 3:21 PM
@desc:
"""
import pandas as pd
from netmiko import ConnectHandler
import openpyxl


def get_batch_backup_dev_infos(filename='new_inventory.xlsx.bk'):
    """
    读取Excel表格加载网络设备基本信息和其配置备份的命令，结果返回一个元组的列表
    :param filename: 表格名称，默认值是inventory.xlsx
    :return: [(<netmiko连接设备所需基本信息的字典>,<配置备份的命令>)]
    示例：
    [({'host': '192.168.137.201',
       'device_type': 'huawei',
       'username': 'netdevops',
       'password': 'Admin123~',
       'secret': nan,
       'timeout': 180,
       'conn_timeout': 20},
       'display current-configuration'),
    ]
    """
    # 读取并将表格加载成字典的列表
    df = pd.read_excel(filename)
    # print(df)
    items = df.to_dict(orient='records')
    # print(items)
    # 构建返回的结果，dev_infos是一个元组的列表。
    dev_infos = []
    for i in items:
        # 取出配置备份的命令，并用del 将其从字典中删除
        backup_cmd = i['backup_cmd']
        del i['backup_cmd']
        # 删除配置备份命令后的字典就是netmiko登录设备所需的信息
        dev = i
        # print(dev)
        dev_infos.append((dev, backup_cmd))
    return dev_infos


def network_device_backup(dev, cmd='display current-configuration'):
    """
    登录设备执行配置备份的命令，并将设备回显的配置写入一个<设备IP或者host>.txt的文件中，编码格式utf8
    :param dev: 设备的基础信息，类型字典，key与创建netmiko所需的参数对应
    :param cmd: 要执行的配置备份的命令，默认是华为的“display current-configuration”
    :return: None 不返回，只打印
    """
    with ConnectHandler(**dev) as conn:
        conn.enable()
        output = conn.send_command(command_string=cmd)
        file_name = '{}.txt'.format(dev['host'])
        with open(file_name, mode='w', encoding='utf8') as f:
            f.write(output)
            print('{}执行备份成功'.format(dev['host']))


def batch_backup(inventory_file='new_inventory.xlsx.bk'):
    dev_infos = get_batch_backup_dev_infos(inventory_file)
    print(dev_infos)
    for dev_info in dev_infos:
        dev = dev_info[0]
        # print(dev)
        cmd = dev_info[1]
        # print(cmd)
        # network_device_backup(dev, cmd)
        network_device_backup(dev, cmd)


if __name__ == '__main__':

    batch_backup()
