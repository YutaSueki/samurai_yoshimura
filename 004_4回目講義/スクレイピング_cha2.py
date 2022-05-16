# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:28:04 2022

@author: sueki
"""

#%% 前提としてのＨＴＭＬ

https://saruwakakun.com/html-css/basic/html

・ＨＴＭＬはタグで構成される。
・タグは属性を持つことができる
　ーherf属性　：リンク先URLの属性
　ーclass属性：タグに付加する識別情報　　一つの属性値は同じHTML内で一つのみ
　ーid属性　：タグに付加する識別情報　同じHTML内で一意の値

#%% 2章で重要なこと

### スクレイピングの流れ
# urlの指定
# HTML情報の取得
# HTML情報の解析
# HTMLからの情報抽出
# 繰り返し
###

import requests
from bs4 import BeautifulSoup

##########　urlの指定～HTML情報の解析
# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

########## HTMLからの情報抽出
# HTML全体を表示する
print(soup)

# title、h2、liタグを検索して表示する
print(soup.find("title"))
print(soup.find("h2"))
print(soup.find("li"))

# title、h2、liタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)

# liタグの全てのデータを抽出する。
soup.find_all("li")

# リストなので、for文でデータを抽出する
list_li = soup.find_all("li")

for i in list_li:
    print(i)
    
for i in list_li:
    print(i.text)
    
# herfでURLを取得する

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

soup.find("a").text
soup.find("a").get("href")


#クラスを用いた情報取得
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# class(やid)で検索し、その中のすべてのaタグを検索して表示する P49
list_topic = soup.find_all(class_="sc-jqCOkK jEGAcM")

for topic in list_topic:
    print(topic.text)

# class(やid)とタグで同時に条件取得も可能
list_topic = soup.find_all("a", class_="sc-jqCOkK jEGAcM")

for topic in list_topic:
    print(topic.text)



#%% 2-1
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)

#%% 2-2

import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# title、h2、liタグを検索して表示する
print(soup.find("title"))
print(soup.find("h2"))
print(soup.find("li"))


#%% 2-3
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# title、h2、liタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)


#%% 2-4
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):
	print(element.text)


#%% 2-5
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(id="chap2")
print(chap2)


#%% 2-6
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索し、その中のすべてのliタグを検索して表示する
chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
	print(element.text)


#%% 2-7
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# classで検索し、その中のすべてのaタグを検索して表示する
topic = soup.find(class_="sc-DNdyV lbRQVi")

for element in topic.find_all("a"):
	print(element.text)



#%% 2-8
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
	print(element.text)
	url = element.get("href")
	print(url)


#%% 2-9
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索し、リンクを絶対URLで表示する
for element in soup.find_all("a"):
	print(element.text)
	url = element.get("href")
	link_url = urllib.parse.urljoin(load_url, url)
	print(link_url)


#%% 2-10
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# ファイルを書き込みモードで開く
filename = "linklist.txt"
with open(filename, "w") as f:
	# すべてのaタグを検索し、リンクを絶対URLで書き出す
	for element in soup.find_all("a"):
		url = element.get("href")
		link_url = urllib.parse.urljoin(load_url, url)
		f.write(element.text+"\n")
		f.write(link_url+"\n")
		f.write("\n")

#%% 2-11
import requests

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1]

# 画像データを、ファイルに書き出す
with open(filename, mode="wb") as f:
	f.write(imgdata.content)


#%% 2-12
import requests
from pathlib import Path

# 保存用フォルダを作る
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

# 画像データを、ファイルに書き出す
with open(out_path, mode="wb") as f:
	f.write(imgdata.content)


#%% 2-13
import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
	src = element.get("src")
	
	# 絶対URLと、ファイルを表示する
	image_url = urllib.parse.urljoin(load_url, src)
	filename = image_url.split("/")[-1]
	print(image_url, ">>", filename)
	

#%% 2-14
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 保存用フォルダを作る
out_folder = Path("download2")
out_folder.mkdir(exist_ok=True)

# すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
	src = element.get("src")
	
	# 絶対URLを作って、画像データを取得する
	image_url = urllib.parse.urljoin(load_url, src)
	imgdata = requests.get(image_url)
	
	# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
	filename = image_url.split("/")[-1]
	out_path = out_folder.joinpath(filename)

	# 画像データを、ファイルに書き出す
	with open(out_path, mode="wb") as f:
		f.write(imgdata.content)

	# 1回アクセスしたので1秒待つ
	time.sleep(1)

