# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:25:53 2022

@author: user
"""

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

jo_c = (len(jo))
for p in range(1, jo_c + 1):
    if p == 1 or p == 6 or p == 11:
        for r in range(1, 13):
            race = "cellbg c{}-{}"
            rn = race.format(p, r)
            atari = soup.find_all(class_ = rn)
            print(atari)
            kekka = []
            for a in(atari):
                a_d = (a.text)
                #print(a_d)
                kekka.append(a_d)
                print(a_d)
    else:
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
                print(a_d)
                
"""
一部情報が重複します。　解消めざします。　最後、場と出目を紐づけてゴールと思ってます。
"""

