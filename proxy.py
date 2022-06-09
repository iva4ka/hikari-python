import threading
from bs4 import BeautifulSoup as BS
import os.path, os, requests, re, items
from time import sleep

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if os.path.exists("./proxies.txt"):
    os.remove("./proxies.txt")

file = open('proxies.txt', 'w')
file.write('')
file.close()
file = open('proxies.txt', 'a')
good_proxies = list()
def pattern_one(url):
    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
    if not ip_port: pattern_two(url)
    else:
        for i in ip_port:
            file.write(str(i) + '\n')
            good_proxies.append(i)


def pattern_two(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('td>(\d{2,5})<', url)
    if not ip or not port: pattern_three(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_three(url):
    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('>\n[\s]+(\d{2,5})\n', url)
    if not ip or not port: pattern_four(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_four(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('>(\d{2,5})<', url)
    if not ip or not port: pattern_five(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_five(url):
    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('(\d{2,5})', url)
    for i in range(len(ip)):
        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
        good_proxies.append(str(ip[i]) + ':' + str(port[i]))

def start(url):
    try:
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
        pattern_one(req)
    except requests.exceptions.SSLError: pass
    except: pass
class Proxy:
    def parse(file):
        # load proxies file
        open('proxies.txt', 'w').write('')
        f = open('proxies.txt', 'r')
        s4_read = f.read()
        f.close()

        # parse
        with open('proxies.txt', 'a') as file:
            lol = 0
            r = requests.get(f'https://hidemy.name/ru/proxy-list/?type=4#list', headers=HEADERS)
            soup = BS(r.content, 'html.parser')
            proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')
            for i in proxies:
                _proxy = i.find('td')
                _port = _proxy.find_next('td').text
                _proxy = _proxy.text
                proxy = _proxy + ':' + _port
                if proxy in s4_read: continue
                if lol == 0:
                    if s4_read == [''] or s4_read == [] or s4_read == '':
                        file.write(proxy)
                    lol = 1
                else:
                    file.write(f'\n' + proxy)
            threads = list()
            for url in items.URL_LIST_PROXY.splitlines():
                if url:
                    x = threading.Thread(target=start, args=(url, ))
                    x.setDaemon(True)
                    x.start()
                    threads.append(x)
            for th in threads:
                th.join()
        while True:
            try:
                with open('proxies.txt', 'a') as file:
                    site = soup.find('li', class_='next_array').find('a').get('href')

                    r = requests.get(f'https://hidemy.name{site}', headers=HEADERS)
                    soup = BS(r.content, 'html.parser')

                    proxies = soup.find('div', class_='table_block').find('tbody').find_all('tr')

                    for i in proxies:
                        _proxy = i.find('td')
                        _port = _proxy.find_next('td').text
                        _proxy = _proxy.text
                        proxy = _proxy + ':' + _port
                        if proxy in s4_read: continue
                        file.write(f'\n' + proxy)

            except Exception as e:
                break
            
        r = requests.get(f'https://github.com/TheSpeedX/PROXY-List/blob/master/proxies.txt', headers=HEADERS)
        soup = BS(r.content, 'html.parser')

        proxies = soup.find_all('tr')

        with open('proxies.txt', 'a') as file:
            for i in proxies:
                proxy = i.text.split('\n')[2]
                if proxy in open('proxies.txt', 'r').read(): continue
                file.write('\n' + proxy)

        r = requests.get(f'https://api.openproxylist.xyz/proxies.txt', headers=HEADERS)
        soup = BS(r.content, 'html.parser')

        proxies = str(r.content).split(f'\n')[0].split(f'\\n')

        with open('proxies.txt', 'a') as file:
            for i in proxies:
                if i in open('proxies.txt', 'r').read(): continue
                if '<' in i: continue
                lol = 0
                for j in abc:
                    if j in i: lol = 1
                if lol == 1: continue
                file.write('\n' + i)

