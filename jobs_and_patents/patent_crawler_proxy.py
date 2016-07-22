#-*- coding:utf-8 -*-

import requests
import time
import random
import re
from bs4 import BeautifulSoup


def getIP():
    ip_list = []
    url_ip = "http://dev.kuaidaili.com/api/getproxy/?orderid=926891818067653&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_ha=1&sep=1"
    flag = True
    while flag:
        result = requests.get(url_ip).text.split('\r\n')
        if len(result) == 1 and 'ERROR' in result[0]:
            time.sleep(5)
        else:
            for item in result:
                ip_list.append('http://'+str(item))
            flag = False
    return ip_list

def crawler(proxies,url):
    s = requests.session()
    result = s.get(url,proxies=proxies)
    print result
    return result.text

def fetch(text):
    soup = BeautifulSoup(text,"html.parser", from_encoding='gb2312')
    head = soup.findAll('span',class_="PatentAuthorBlock")
    return head
    
def main():
    ip_list = getIP()
    proxies={}
    print len(ip_list)
    url = 'http://www.soopat.com/Home/Result?SearchWord=2012101915028&FMZL=Y&SYXX=Y&WGZL=Y'
    proxies['http'] = ip_list[random.randint(0,len(ip_list))]
    proxies['https'] = ip_list[random.randint(0,len(ip_list))]
    text = crawler(proxies,url)
    result = fetch(text)
    print result

if __name__ == "__main__":
    main()
