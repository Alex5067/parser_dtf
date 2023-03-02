from bs4 import BeautifulSoup
import requests
import re
import webbrowser

def list_href(bs, limit): #done
    #temp = bs.find_all('a', 'content-link', limit=limit, href=True)
    temp = bs.find_all('a', 'content-header__item content-header-number', limit=limit, href=True)
    res = []
    for a in temp:
        res.append(a['href'])
    return res

def parse_title(bs, limit):
    filteredNews = []
    res = []
    title = bs.find_all('div', 'content-title content-title--short l-island-a', limit=limit)
    for data in title:
            filteredNews.append(data.text)
    for data in filteredNews:
        data = re.sub(r"Статьи редакции", "", data)
        newdata = " ".join(data.split())
        res.append(newdata)
    return res

def href_title(bs):
    #limit = int(input("Кол-во статей:"))
    limit = 8  # if limit > 8, work not as expected, crashed when limit > 11
    href = list_href(bs, limit)
    title = parse_title(bs, limit)
    for i in range(limit):
        print(i,")", title[i])
        print(href[i])
    while (1):
        chose = int(input("Pick post from 0 to 7 or 101 to rechose: "))
        if (chose == 101):
            print("\n")
            init()
        webbrowser.open(href[chose], new=2)
        next = input("Y to continue, Q to exit, R to rechose ")
        if (next == 'q' or next == 'Q'):
            exit()

def init():
    dict = {"games":"https://dtf.ru/games", "hard":"https://dtf.ru/hard", "cinema":"https://dtf.ru/cinema",
            "gameindustry":"https://dtf.ru/gameindustry", "gamedev":"https://dtf.ru/gamedev", "life":"https://dtf.ru/life"}
    print("Available subjects: games, hard, cinema, gameindustry, gamedev, life")
    url = input("Pick subject or exit: ")
    if (url == "exit"):
        exit()
    response = requests.get(dict[url])
    bs = BeautifulSoup(response.text, "html.parser")
    href_title(bs)

if __name__ == '__main__':
    init()
