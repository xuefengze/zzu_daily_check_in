#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import logging
import datetime
import os
import pandas as pd

today_date = str(datetime.date.today())
log_path = './log/'

logger = logging.getLogger()
file_handler = logging.FileHandler(filename=log_path+'log_'+today_date+'.txt', mode="a", encoding="utf-8")
formatter = logging.Formatter('[%(asctime)s]------%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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


# 开启chrome
def openChrome():
    #使用代理ip
    #proxy_ip = '123.122.155.139:19630'
    #options.add_argument('--proxy-server=http://' + proxy_ip)

    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='./chromedriver', options=option)
    driver.implicitly_wait(10)  # seconds,隐式等待获取组件，推荐显示，懒得写了
    return driver

def openurl(driver):
    #打开的网址
    url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0"
    try:
        driver.get(url)
    except:
        logging.warning('网址打开失败！')
        return -1
    return driver

# 流程
def operate_dk(driver, id, password):
    #input id,password
    driver.find_element_by_xpath("//input[@name='uid']").send_keys(id)
    driver.find_element_by_xpath("//input[@name='upw']").send_keys(password)
    # 提交表单
    driver.find_element_by_xpath("//*[@name='smbtn']").click()
    try:
        iframe1 = driver.find_element_by_xpath("//iframe[@name='zzj_top_6s']")
    except:
        logging.warning(str(id)+'登陆失败！服务器是否又崩了？')
        return -1
    else:
        # 切换frame
        driver.switch_to.frame(iframe1)
        driver.find_element_by_css_selector('[onclick="myform52.submit()"]').click()

        #所有ratio全选否
        elements = driver.find_elements_by_xpath("//input[@value='否']")
        for element in elements:
            element.click()

        #选择省份
        select = Select(driver.find_element_by_id("myvs_13a"))
        select.select_by_value('41')
        #获取地市
        driver.find_element_by_xpath("//input[@name='Btn3']").click()
        #选择地市
        select = Select(driver.find_element_by_id("myvs_13b"))
        select.select_by_index(0)

        #input 具体地址
        ele = driver.find_element_by_xpath("//input[@name='myvs_13c']")
        ele.clear()
        ele.send_keys("郑大")

        # 提交
        try:
            driver.find_element_by_css_selector('[onclick="myform52.submit()"]').click()
        except:
            logging.warning(str(id)+'提交失败！')
            return -1
        time.sleep(1)
        logging.warning(str(id)+"打卡成功")


if __name__ == '__main__':
    clean_log()
    driver = openChrome()
    datas = pd.read_csv('user.csv',dtype=str)
    for row in datas.itertuples():
        id = getattr(row, 'id')
        password = getattr(row, 'password')
        driver = openurl(driver)
        operate_dk(driver, id, password)
    driver.quit()