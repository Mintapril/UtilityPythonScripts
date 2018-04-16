import requests
from bs4 import BeautifulSoup
import re

name_patterns = re.compile('https://etternaonline.com/user/\w+')

def get_url(url, word, int1, int2):
    r = requests.get(url)
    r = str(r.content)
    r = r.split("\\n")
    for tmp in r:
        tmp = tmp.strip().strip("\\r")
        if word in tmp:
            url = tmp[int1:int2]
    return url

def get_user(user_url):
    r = requests.get(user_url)
    r = r.text
    html = BeautifulSoup(r, "lxml")
    name = html.find("a", href=name_patterns)
    user_url = name["href"]
    user_name = name.get_text()
    user_page = requests.get(user_url)
    user_page = user_page.text
    user_page = BeautifulSoup(user_page, "lxml")
    rating = user_page.find("span", class_="pull-right")
    rating = rating.get_text()
    ratings = user_page.find("div", class_="panel-body")
    ratings = ratings.get_text()
    return user_name.strip(), rating.strip(), ratings
