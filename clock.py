#!/usr/bin/env python3
#-*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import pandas as pd
import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

# 开启chrome
def openChrome():
    #使用代理ip
    #proxy_ip = '123.122.155.139:19630'
    #options.add_argument('--proxy-server=http://' + proxy_ip)

    option = webdriver.ChromeOptions()
    option.add_argument('--disable-infobars')
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path = path+'/chromedriver', options=option)
    driver.implicitly_wait(10)  # seconds,隐式等待获取组件，推荐显示
    return driver

def openurl(driver):
    #打开的网址
    url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0"
    try:
        driver.get(url)
    except:
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
        #绿码
        select = Select(driver.find_element_by_name("myvs_13"))
        select.select_by_value("g")
        #疫苗
        select = Select(driver.find_element_by_name("myvs_26"))
        select.select_by_value("2")

        #input 具体地址
        ele = driver.find_element_by_xpath("//input[@name='myvs_13c']")
        ele.clear()
        ele.send_keys("郑大")

        # 提交
        try:
            driver.find_element_by_css_selector('[onclick="myform52.submit()"]').click()
        except:
            return -1


if __name__ == '__main__':
    driver = openChrome()
    datas = pd.read_csv(path + '/user.csv',dtype = str)
    for row in datas.itertuples():
        id = getattr(row, 'id')
        password = getattr(row, 'password')
        driver = openurl(driver)
        operate_dk(driver, id, password)
    driver.quit()