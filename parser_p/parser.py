import requests
from bs4 import BeautifulSoup
# import schedule
# import time


URL = 'https://spb.rt.ru/support/internet/connect/conduct-internet-in-house'
HEADERS = {
'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68'
}


# получаем html
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


html = get_html(URL)
links = list()
names = list()
dic = {}


"""в get_content() получаем элементы с html и также получаем нужный нам файл!!!можно выполнить один раз,чтобы появился 
нужный файл и потом уже убрать из кода вызов этой функции(так как ее потом будет вызывать schedule автоматически"""


def get_content():
    soup = BeautifulSoup(html.text, 'html5lib')
    items = soup.find_all('div', class_="menu-wiki__child-links")
    with open('all_html.html', 'w') as f:
        f.write(str(items))
    with open('all_html.html', 'r') as pars:
        soup = BeautifulSoup(pars, 'html5lib')
    for link in soup.find_all('a'):
        b = link.get('href')
        links.append('https://spb.rt.ru' + str(b))
        key = link.get_text()
        names.append(key)

    def map_return():
        for i in range(len(links)):
            dic.update({names[i]: links[i]})
        with open('file.txt', 'w') as our_dict:
            our_dict.write(str(dic))

        return dic
    map_return()


# когда получишь этот text файл,сможешь удалить строку 54
# get_content()
with open('file.txt', 'r') as new_dict:
    dictionary = new_dict.read()


# возвращает нужный нам словарь!!!
def return_dic():
    res = eval(dictionary.replace("[", "{").replace("]", "}"))
    return res


#def updating_for_dict():
    # # shedule работа со временем(должен выполняться пока запущена прогга
    # schedule.every().monday.at('01:00').do(get_content)
    # schedule.every().monday.at('01:01').do(return_dic)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)