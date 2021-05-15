from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os
import csv

emoji_list = []
word_list = []
point_list = []


headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
site_url = "https://www.emojiall.com/zh-hant/all-emojis"

get_url = requests.get(site_url,headers={"User-Agent": headers})

soup = BeautifulSoup(get_url.text, "lxml")

#　不要なHTMLタグデータを排除
for x in soup.find_all("a",{"class":"emoji_font tooltip"}):
    x.extract()

for y in soup(["span"]):
    y.extract()

emojis = soup.select('.emoji_font')# 絵文字データを取得
words = soup.select('.emoji_name')# 意味データを取得

# 意味のリストを作成
for word in words:
    word = word.getText()
    word_list.append(word)


# 絵文字のリストを作成
for emoji in emojis:
    emoji = emoji.getText()
    emoji_list.append(emoji)

# 絵文字のリストの中から絵文字をFor文で１要素づつord関数で文字コード化する
for emoji in emoji_list:
    if len(emoji) < 2:
        code_point = hex(ord(emoji))
        point_list.append(code_point)

# 絵文字と意味のリスト作成
dic = dict(zip(emoji_list,word_list)) 


# 絵文字の文字コードリストであるpoint_listはord関数の特性上１要素の絵文字分のみ格納されてるため、絵文字と意味も１要素分のみになるよう調整する
# {絵文字：意味}となっている変数dicの中からキー(k)である絵文字部分が２要素以上の場合、pop関数でセットごと削除
# 上の処理で絵文字が２要素以外のだけが残る
# kがキー、vが値
new_list = []
for k,v in list(dic.items()):
    if len(k) > 2:
        dic.pop(k)
    else:
        new_list.append((k,v))

file0 = "./emoji.txt"
with open(file0, 'w') as f:
    for _unicode, (emoji, word) in zip(point_list, list(new_list)):
        f.writelines('{},{},{}\n'.format(_unicode, emoji, word))