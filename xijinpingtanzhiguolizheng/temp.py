# coding=utf-8
import os
import sys
import time

import requests
from bs4 import BeautifulSoup
import xlwt
import io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def result2file(parent_dic, article_date, article_title):
    try:
        root_dic = '/Users/Tuoxian/PycharmProjects/demo/test'
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
        'Cookie': 'i18n_browser_Lang=zh-cn; JEECGINDEXSTYLE=hplus; JSESSIONID=E8970F5EF61C7EB53BAAD89709568A27; Hm_lvt_098e6e84ab585bf0c2e6853604192b8b=1567391196; Hm_lpvt_098e6e84ab585bf0c2e6853604192b8b=1567672118; ZINDEXNUMBER=2000',
        'Upgrade-Insecure-Requests': '1'}
    try:
        response = requests.post(url, data={'userName': '经理','realName':'xxx','password':'mabin','devFlag':'1'}, headers=headers)
        result = response.content.decode('utf-8')
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


def main():
    reload(sys)  # reload 才能调用 setdefaultencoding 方法
    sys.setdefaultencoding('utf-8')
    url = 'http://localhost:8080/jeecg_war/userController.do?saveUser'
    html = request_douban(url)
    print html
    # soup = BeautifulSoup(html, 'lxml')
    # title_list = soup.select("ul > li > a")
    # chapter = soup.select("h3 > a > font> b")
    # chapter_index = [5, 12, 17, 22, 25, 31, 38, 41, 43, 49, 54, 57, 60, 63, 69, 73, 76, 80]
    # test_index = 0
    # # # article_date = soup.select("div.listBox > ul > li > span")
    # for i in range(len(title_list)):
    #     test_index = i+1
    #     article_url = title_list[i].get("href")
    #     title_index = str(i)
    #     if 'html' in 'html':
    #         try:
    #             html1 = request_douban(article_url)
    #             result_soup = BeautifulSoup(html1, 'lxml')
    #             result_title = result_soup.select("h3")
    #             print '-----------------------------抓取《'+result_title[0].get_text().strip()[:-2]+'》成功！'
    #             result_title_str = '/' + title_index + result_title[0].get_text().strip()[:-2] + '.txt'
    #             artcle_content = result_soup.select("div#font_area > p")
    #         except BaseException:
    #             print '----------------------------------------------------------抓取第'+ str(i)+'篇文章失败！'
    #         try:
    #             file_root_dic = '/习近平谈治国理政卷一'
    #             for j in range(len(chapter_index)):
    #                 if test_index >= chapter_index[j] and test_index < chapter_index[j+1]:
    #                     parent_dic = '/' + chapter[j+1].get_text()
    #                     break
    #                 elif test_index < 5:
    #                     parent_dic = '/' + chapter[0].get_text()
    #                     break
    #
    #
    #             f = result2file(file_root_dic, parent_dic, result_title_str)
    #             if f is None:
    #                 continue
    #             title_file = result_title[0].get_text().strip()[:-2]
    #             f.write(title_file + '\n')
    #             for k in range(len(artcle_content)):
    #                 if 'style' in str(artcle_content[k]) or 'strong' in str(artcle_content[k]) or 'href' in str(
    #                             artcle_content[k]):
    #                     continue
    #                 else:
    #                     f.write(artcle_content[k].get_text() + '\n')
    #             f.close()
    #         #
    #         #
    #         except Exception:
    #             print 'what?'
    # print ('----------------------------------------------共获取:%d篇文章' % len(title_list))
    #
    # #
    #     try:
    #         r2 = result_title
    #         article_title_str = '/' + r2 + '.txt'
    #         f = result2file('/网络聚焦/北京新闻', article_date_str1, article_title_str)
    #         if f is None:
    #             continue
    #         f.write(r2 + '\n')
    #         for k in range(len(artcle_content)):
    #             f.write('  ' + artcle_content[k].get_text() + '\n')
    #
    #         f.close()
    #         print '《' + r2 + '》' + article_date[i].get_text()[5:].replace('-', '月') + '日'
    #
    #     except IndexError:
    #         print 'result_title is None!'
    # print ('----------------------------------------------共获取:%d条新闻' % len(title_list))


main()
