# coding=utf-8
import os
import sys

import requests
from bs4 import BeautifulSoup
import xlwt
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def result2file(parent_dic, article_date, article_title):
    try:
        root_dic = '/Users/plantkon/Documents/WorkSpacePy/hdqw/test'
        target_dic = root_dic + parent_dic + article_date
        is_exists = os.path.exists(target_dic)
        filename = target_dic + article_title
        if not is_exists:
            os.makedirs(target_dic)
        f = open(filename, 'w')
        return f
    except Exception:
        print 'no such directory'
        return None


def request_douban(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': '__jsluid_h=d3f753f69b3087093a60a7193850d3a9; route=a2cec3cb28b0d59d32db7b39f74f56a5; __utrace=46083bc42d8153816c554a7869e96c5b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cd6e1c7e0165-012bc5135f34b5-38637706-1024000-16cd6e1c7e148e%22%7D; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1566973445; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1567048957; _va_ses=*; _va_id=bc8112bd84bfd167.1566973214.2.1567050528.1567050509.',
        'Upgrade-Insecure-Requests': '1'}
    proxie = {
        'http': 'http://59.44.247.194:9797',
        'http': 'http://59.44.247.194:9797',
        'http': 'http://124.67.165.2:3128',
        'http': 'http://120.83.97.34:9999',
        'http': 'http://123.114.205.93:8118',
        'http': 'http://183.129.207.80:13516'
    }
    try:
        response = requests.get(url, headers=headers)
        result = response.content.decode('gb2312','ignore')
        if response.status_code == 200:
            return result

    except requests.RequestException:
        print 'cnm'


def exchange_url(url):
    http_target_str = 'http://world.people.com.cn'
    if (http_target_str in url):
        # print (title_list[i].get("href"))
        return url
    else:
        # test = http_target_str + title_list[i].get("href")
        _url = http_target_str + url
        return _url


def bjxw(url):
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    # url = 'http://www.beijing.gov.cn/shouye/jrbj/default.htm'
    # url = 'http://www.beijing.gov.cn/ywdt/yaowen'
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    title_list = soup.select("div.listBox > ul > li > a  ")
    article_date = soup.select("div.listBox > ul > li > span")
    for i in range(len(title_list)):
        if len(title_list[i].get("href")) <= 14:
            article_url = url+title_list[i].get("href")[1:]
        else:
            article_url = title_list[i].get("href")
        print article_url
        try:
            html1 = request_douban(article_url)
            result_soup = BeautifulSoup(html1, 'lxml')
            # result_title = result_soup.select("div.header > h1")
            result_title = title_list[i].get_text()
            artcle_content = result_soup.select("div.TRS_Editor > p")
            article_date_str = article_date[i].get_text()[5:]
            _article_date_str = article_date_str.replace('-', '月') + '日'
            article_date_str1 = '/' + _article_date_str
        except BaseException:
            continue
            print 'cnm 页面不存在'

        try:
            r2 = result_title
            article_title_str = '/' + r2 + '.txt'
            f = result2file('/网络聚焦/北京新闻', article_date_str1, article_title_str)
            if f is None:
                continue
            f.write(r2 + '\n')
            for k in range(len(artcle_content)):
                f.write("<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " +
                        artcle_content[k].get_text() + "</span></div>")
                f.write("<div>&nbsp;</div>")


            f.close()
            print '《' + r2 + '》' + article_date[i].get_text()[5:].replace('-', '月') + '日'

        except IndexError:
            print 'result_title is None!'
    print ('----------------------------------------------共获取:%d条新闻' % len(title_list))

bjxw('http://www.beijing.gov.cn/ywdt/yaowen')
bjxw('http://www.beijing.gov.cn/ywdt/gqrd')

