#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 
import logging
import datetime

today_date = str(datetime.date.today())
log_path = './log/'

def clean_log():
    #对上个月的日志进行删除
    global log_path
    global today_date

    # 遍历目录下的所有日志文件 i是文件名
    for i in os.listdir(log_path):
        file_path = log_path + i  # 生成日志文件的路径

        # 获取日志的年月，和今天的年月
        today_m = int(today_date[5:7])  # 今天的月份
        m = int(i[9:11])  # 日志的月份
        today_y = int(today_date[0:4])  # 今天的年份
        y = int(i[4:8])  # 日志的年份

        # 对上个月的日志进行清理，即删除。
        if (m < today_m):
            if (os.path.exists(file_path)):  # 判断生成的路径对不对，防止报错
                os.remove(file_path)  # 删除文件
        elif (y < today_y):
            if (os.path.exists(file_path)):
                os.remove(file_path)

if __name__ == '__main__':
    clean_log()