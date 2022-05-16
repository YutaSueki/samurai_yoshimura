# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:38:37 2022

@author: user
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=1&jcd=01&hd=20220512"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
#print(soup)


import itertools 
 
    
f1 = soup.find_all("th", class_ = "is-boatColor1")[0].text

f2 = soup.find_all("th", class_ = "is-boatColor2")[0].text

f3 = soup.find_all("th", class_ = "is-boatColor3")[0].text

f4 = soup.find_all("th", class_ = "is-boatColor4")[0].text

f5 = soup.find_all("th", class_ = "is-boatColor5")[0].text

f6 = soup.find_all("th", class_ = "is-boatColor6")[0].text

xs = [f1, f2, f3, f4, f5, f6]


rt = (list(itertools.permutations(xs, 3)))

rt_ol = []
for rt_x in rt:
    rt_o = ("".join(rt_x)) 
    rt_ol.append(rt_o)
#print(rt_ol)


rt_1 = (rt_ol[0:20])
rt_2 = (rt_ol[21:40])
rt_3 = (rt_ol[41:60])
rt_4 = (rt_ol[61:80])
rt_5 = (rt_ol[81:100])
rt_6 = (rt_ol[101:120])
       
#print(rt_1, rt_2, rt_3, rt_4, rt_5, rt_6)


odd = soup.find_all("td", class_ = "oddsPoint")
#print(odd)

odd_ol = []
for odd_d in(odd):
    odd_dl = (odd_d.text)
#    print(odd_dl)
    odd_ol.append(odd_dl)
#print(odd_ol)

od_1 = odd_ol[0:120:6]
od_2 = odd_ol[1:120:6]
od_3 = odd_ol[2:120:6]
od_4 = odd_ol[3:120:6]
od_5 = odd_ol[4:120:6]
od_6 = odd_ol[5:120:6]

#print(od_1, od_2, od_3, od_4, od_5, od_6)


k_odd_1 = dict(zip(rt_1, od_1))
k_odd_2 = dict(zip(rt_2, od_2))
k_odd_3 = dict(zip(rt_3, od_3))
k_odd_4 = dict(zip(rt_4, od_4))
k_odd_5 = dict(zip(rt_5, od_5))
k_odd_6 = dict(zip(rt_6, od_6))


k_odd_s = {**k_odd_1, **k_odd_2, **k_odd_3, **k_odd_4, **k_odd_5, **k_odd_6, }

for k, v in k_odd_s.items():
    print(k, v)














    
 