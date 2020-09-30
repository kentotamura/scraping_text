from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os
import csv

emoji_list = []
word_list = []
point_list = []

site_url = "https://www.emojiall.com/zh-hant/all-emojis"
get_url = requests.get(site_url)
# print (get_url.text)
soup = BeautifulSoup(get_url.text, "lxml")

for x in soup.find_all("a",{"class":"emoji_font tooltip"}):
    x.extract()

for script in soup(["span"]):
    script.extract()

emojis = soup.select('.emoji_font')
words = soup.select('.emoji_name')

for word in words:
    word = word.getText()
    word_list.append(word)
# print(len(word_list))

for emoji in emojis:
    emoji = emoji.getText()
    emoji_list.append(emoji)
# print(len(emoji_list))

for emoji in emoji_list:
    if len(emoji) < 2:
        code_point = hex(ord(emoji))
        point_list.append(code_point)
# print(point_list)

dic = dict(zip(emoji_list,word_list))
# print(dic)

new_list = []
for k,v in list(dic.items()):
    if len(k) > 2:
        dic.pop(k)
    else:
        new_list.append((k,v))
# print(new_list)

file0 = "/Users/ktamura/Downloads/emoji.txt"
with open(file0, 'w') as f:
    for _unicode, (emoji, word) in zip(point_list, list(new_list)):
        f.writelines('{},{},{}\n'.format(_unicode, emoji, word))
