# -*- coding: utf-8 -*-
"""
Created on Sat May 14 07:39:30 2022

@author: sueki
"""

#%% 参考
# selenium　基本メソッド
# https://qiita.com/mochio/items/dc9935ee607895420186
# 新規ウィンドウの立ち上げ
# https://code-examples.net/ja/q/2d575f3
# ウィンドウの変更
# https://tanuhack.com/selenium-change-window/#i-2

#%%
import os
import time
import csv
import datetime
import glob


from bs4 import BeautifulSoup


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #//追記

#%%

url = "https://www.boatrace.jp/"

#url = "https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/"

driver =   webdriver.Chrome(ChromeDriverManager().install()) #//追記
driver.get(url)
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
url_plus = soup.find("a", class_="btn is-type3_3__3rdadd").get("href")


driver.get(url + url_plus)

# ログイン
el = driver.find_element_by_name("in_KanyusyaNo")
el.clear()
el.send_keys('07720494')
time.sleep(1)

el = driver.find_element_by_name("in_AnsyoNo")
el.clear()
el.send_keys('6969')
time.sleep(1)

el = driver.find_element_by_name("in_PassWord")
el.clear()
el.send_keys('vhD5AM')
time.sleep(1)

el = driver.find_element_by_name("TENTP017A_2")
#el.submit()
el.click()

time.sleep(1)

#%%

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
url_plus = soup.find("p", class_="btnGroup1_btn").find("a").get("href")

driver.get(url + url_plus)

#%%

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
url_plus = soup.find("a", id="TENTP090A0").get("onclick")

driver.execute_script(url_plus)

#%%
# ウィンドウハンドルを取得する
handle_array = driver.window_handles

# 一番最後のdriverに切り替える
driver.switch_to.window(handle_array[-1])

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
url_plus = soup.find("a", class_="btn is-type1_5").get("onclick")

soup.find("title")

driver.execute_script(url_plus)


