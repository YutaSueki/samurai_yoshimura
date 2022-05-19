# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:14:47 2022

@author: sueki
"""

#%% ポイント

# 関数化すること
# find_allでデータを取得してfor文で回す
# 抽出したデータはpandasでデータフレーム化して出力する。
# main関数を使用した実行
# 極力ハードコーディングは避ける

#%% ライブラリのインポート

import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

#%%

def main():
    
    ############　ハードコーディング
    # 初日
    url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=20220511"
    df_odds = get_trifecta_odds(url)
    df_odds.to_csv("odds_day1.csv", index=False)
    time.sleep(1)
    
    # 2日目
    url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=20220512"
    df_odds = get_trifecta_odds(url)
    df_odds.to_csv("odds_day2.csv", index=False)
    time.sleep(1)
    
    # 3日目
    url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=20220513"
    df_odds = get_trifecta_odds(url)    
    df_odds.to_csv("odds_day3.csv", index=False)
    time.sleep(1)
    
    # 4日目
    url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=20220514"
    df_odds = get_trifecta_odds(url)
    df_odds.to_csv("odds_day4.csv", index=False)
    time.sleep(1)
    
    # 5日目
    url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=20220515"
    df_odds = get_trifecta_odds(url)
    df_odds.to_csv("odds_day5.csv", index=False)
    time.sleep(1)
    
    ############　ハードコーディングをやめよう
    
    for i in range(1, 6, 1):
        print(i)    
        
        url = f"https://www.boatrace.jp/owpc/pc/race/odds3t?rno=12&jcd=01&hd=2022051{i}"
        df_odds = get_trifecta_odds(url)
        df_odds.to_csv(f"odds_day{i}.csv", index=False)
        
        time.sleep(1)
        
    
#%%

def get_trifecta_odds(url):
    
    ###### HTMLコードの取得 ######
    #url = "https://www.boatrace.jp/owpc/pc/race/odds3t?rno=1&jcd=01&hd=20220512"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    ######　データ抽出 ######

    #表部分を抽出        
    info_body = soup.find("tbody", class_="is-p3-0")
    list_row = info_body.find_all("tr")
    
    #表部分からデータを抽出
    list_data = []
    for row in list_row:
        
        # row = list_row[0]
        # row = list_row[1]
        
        #rowの要素が37個の時
        if len(row)==37:
            
            list_data_37 = []
            list_td = row.find_all("td")

            flag = 0
            first = 0
            for td in list_td:
                
                if flag==0:
                    second = td.text
                    flag += 1
                elif flag==1:
                    third = td.text
                    flag += 1
                else:
                    odds =  td.text
                    flag = 0
                    first += 1
            
                    data = [first, second, third, odds]
                    # print(data)
                    list_data_37.append(data)
                    list_data.append(data)
        
        #rowの要素が37個の以外
        else:
            
            list_data_25 = []
            list_td = row.find_all("td")

            list_second = [second[1] for second in list_data_37]
            
            flag = 0
            first = 0
            flag_second = 0
            for td in list_td:                
                
                if flag==0:
                    second = list_second[flag_second]

                    third = td.text
                    flag += 1
                else:
                    odds =  td.text
                    flag = 0
                    first += 1
                    flag_second += 1
            
                    data = [first, second, third, odds]
                    # print(data)
                    list_data_25.append(data)
                    list_data.append(data)
    
    ###### データ整形 ######
    df_odds = pd.DataFrame(list_data)
    df_odds.columns = ["first", "second", "third", "odds"]
    
    df_odds = df_odds.sort_values(["first", "second", "third"])
    df_odds = df_odds.reset_index(drop=True)
    
    return df_odds


#%%
if __name__=="__main__":
    main()