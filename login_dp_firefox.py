# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:57:22 2018

@author: wmq
"""

import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#设置用户名密码
username_  = "********"
password_  = "********"

#设置日志等级
logging.basicConfig(level=logging.INFO)

#打开浏览器
browser = webdriver.Firefox()
href = 'http://www.dianping.com/'
browser.get(href)
time.sleep(2)

# 右上登陆
login_btn = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/span[2]/a[1]')
login_btn.click()
time.sleep(3)

# 选择账号登录
iframe = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/iframe')
browser.switch_to_frame(iframe)   #切换至登录模块iframe

#选择账号密码登录
icon_pc = browser.find_element_by_xpath('/html/body/div/div[2]/div[1]')
icon_pc.click()
time.sleep(2)
name_login = browser.find_element_by_xpath('//*[@id="tab-account"]')
name_login.click()
time.sleep(2)

# 输入用户名,密码
username = browser.find_element_by_xpath('//input[@id="account-textbox"]')
password = browser.find_element_by_xpath('//input[@id="password-textbox"]')
username.clear()
username.send_keys(username_)
password.clear()
password.send_keys(password_)

    
# 提交登陆
sub_btn = browser.find_element_by_xpath('//button[@id="login-button-account"]')
sub_btn.click()
time.sleep(5)


while True:
    #检测是否有登录失败警告
    try:
        alert = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[3]/span')
    except NoSuchElementException:
        break
    
    if alert:
        #账密登录失败，尝试手机验证码登录
        mobile_login = browser.find_element_by_xpath('//*[@id="tab-mobile"]')
        mobile_login.click()
        username = browser.find_element_by_xpath('//*[@id="mobile-number-textbox"]')
        username.clear()
        username.send_keys(username_)
        
        #点击获取验证码
        get_code = browser.find_element_by_xpath('//*[@id="send-number-button"]')
        get_code.click()
        
        #输入验证码
        verify_code = browser.find_element_by_xpath('//*[@id="number-textbox"]')
        verify_code_ = input('verify_code > ')
        verify_code.clear()
        verify_code.send_keys(verify_code_)
        
        # 提交登陆
        sub_btn = browser.find_element_by_xpath('//*[@id="login-button-mobile"]')
        sub_btn.click()
        time.sleep(5)
        break
    else:
        raise Exception("Mobile login failed!")
               
#切换回主页
browser.switch_to_default_content()
