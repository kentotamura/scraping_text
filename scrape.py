from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os

emoji_list = []
word_list = []
point_list = []

site_url = "https://www.emojiall.com/zh-hant/all-emojis"
get_url = requests.get(site_url)
soup = BeautifulSoup(get_url.text, "lxml")

for script in soup(["span"]):
    script.extract()

emojis = soup.select('.emoji_font')
words = soup.select('.emoji_name')

for emoji in emojis:
    emoji = emoji.getText().replace('\u200d','')
    if not repr(emoji).startswith(r"'\U") and len(emoji) < 2:
        emoji_list.append(emoji)
    else:
        continue
# print(emoji_list)

for emoji in emoji_list:
    code_point = hex(ord(emoji))
    point_list.append(code_point)
# print(point_list)

for word in words:
    word = word.getText()
    word_list.append(word)
print(word_list)