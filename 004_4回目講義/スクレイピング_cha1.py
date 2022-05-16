#%% chap1 で重要なこと

#Webページの取得は "requests" のライブラリを使用する。 P24を参照

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

response.text

# 文字化けしないようにする
response.encoding = response.apparent_encoding

response.text

#%% chap1-1

import requests

# Webページを取得する
url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字化けしないようにする
response.encoding = response.apparent_encoding

# 取得した文字列データを表示する
print(response.text)

#%% chap1-2

import requests

# Webページを取得する
url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字化けしないようにする
response.encoding = response.apparent_encoding

# ファイルを書き込みモードで開いて
filename = "download.txt"
f = open(filename, mode="w")

# ネットから取得した読み込んだデータを書き込んで
f.write(response.text)

# 最後にファイルを閉じる
f.close()

#%% chap1-3

import requests

# Webページを取得する
url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字化けしないようにする
response.encoding = response.apparent_encoding

# ファイルを書き込みモードで開いて
filename = "download.txt"
with open(filename, mode="w") as f:
	# ネットから取得した読み込んだデータを書き込む
	f.write(response.text)

