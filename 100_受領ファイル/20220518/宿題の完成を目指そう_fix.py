# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:25:53 2022

@author: user
"""

import pandas as pd

import requests
from bs4 import BeautifulSoup

url = "https://www.boatrace.jp/owpc/pc/race/pay?hd=20220512"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
#print(soup)

jo = soup.find_all(class_ = "table1_areaName")
kaisai = []
for j in jo:
    place = (j.find("img").get("alt"))
    kaisai.append(place)
print(kaisai)

#開催場の取得が出来た

list_data = []
for p, k in enumerate(kaisai):
    p = p + 1
    if p == 1 or p == 6 or p == 11 or p == 16:
            s_kekka = []
            for r in range(1, 13):
                race = "cellbg c{}-{}"
                rn = race.format(p, r)
                atari = soup.find_all(class_ = rn)
                #print(atari)
                kekka = []
                for a in(atari):
                    a_d = (a.text)
                    kekka.append(a_d)
                    #print(a_d)
                s_kekka.append(kekka)

                data = [k]
                data.extend(kekka)
                list_data.append(data)

            print(k)
            print(s_kekka)           
            

            
    else:
            s_kekka = []
            for r in range(1, 13):
                race = "is-borderLeft1 cellbg c{}-{}"
                rn = race.format(p, r)
                race2 = "cellbg c{}-{}"
                rn2 = race2.format(p, r)
                atari = soup.find_all(class_ =[rn, rn2])
                #print(atari)
                kekka = []
                for a in(atari):
                    a_d = (a.text)
                    kekka.append(a_d)
                    #print(a_d)
                s_kekka.append(kekka)
                
                data = [k]
                data.extend(kekka)
                list_data.append(data)                
                
            print(k)
            print(s_kekka)
            
"""
開催場のところに各場を代入したかったが時間ぎれです
"""



df = pd.DataFrame(list_data)
df.columns = ["開催場所", "組番", "払い戻し金", "人気"]
df.to_csv("払い戻し金.csv", index=False)


df.shape

11*12

