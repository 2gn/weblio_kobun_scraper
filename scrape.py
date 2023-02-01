from urllib.parse import quote 
from requests import get as get
from bs4 import SoupStrainer, BeautifulSoup

def getMeaningsByKanji(kanji):
    url = f"https://kobun.weblio.jp/content/{kanji}"

    html = get(quote(url, safe=":/")).text

    strainer = SoupStrainer("div", attrs={"class": "kiji"})

    soup = BeautifulSoup(html, "lxml", parse_only=strainer)

    find_attr = lambda name: soup.find(attrs={"class",name}).text

    key = find_attr("midashigo")

    meaning = find_attr("lvlB")
    
    return (key, meaning)
    


