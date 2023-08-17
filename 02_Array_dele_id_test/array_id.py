#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 18:18
# @Author  : Aries
# @Site    : 
# @File    : array_id.py
# @Software: PyCharm
import csv
import pandas as pd
from collections import namedtuple


def screen_date():
    with open("20230731.csv", "r", encoding="utf-8") as f_input: # 源文件
        with open("test2023.csv", "w", encoding="utf-8") as f_output: # 过滤后的文件
            ereader = csv.reader(f_input)
            ewriter = csv.writer(f_output)
            eheader = next(ereader)
            ewriter.writerow(eheader)
            for row_list in ereader:
                last_login = str(row_list[6].strip())
                if last_login < "2022-07": # 改这里筛选所需的日期
                #if last_login < "2020": # 改这里筛选所需的日期
                    #print(last_login)
                    ewriter.writerow(row_list)


def screen_id():
    with open("test2023.csv", "r", encoding="utf-8") as f_input:  # 源文件
        ereader = csv.reader(f_input)
        with open("screen_id.txt", "w") as f:
            for row_list in ereader:
                last_login = str(row_list[0].strip())
                # print(last_login)
                f.write(last_login + "\n")



def screen_distinguish_id():
    with open("screen_id.txt", 'r') as f:
        for line in f.readlines():
            # 去掉前后空白
            line = line.strip()
            # 忽略空格行，len=1
            if len(line) == 11:
                shi_num = line
                print("__【十一】__位数的账号有：%s" % shi_num)
            elif len(line) == 9:
                jiu_num = line
                print("__【九】__位数的账号有：%s" % jiu_num)
            elif len(line) == 8:
                ba_num = line
                print("__【八】__位数的账号有：%s" % ba_num)
            elif len(line) == 7:
                qi_num = line
                print("__【七】__位数的账号有：%s" % qi_num)
            else:
                qita = line
                print("__【其他】__位数的账号有：%s" % qita)



screen_date()
screen_id()
screen_distinguish_id()