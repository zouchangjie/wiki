# coding=utf-8
#jupyter notebook


import scrapy
from scrapy import Request, FormRequest
import sys
import pandas as pd
import numpy as np
sys.path.append("..")

reload(sys)
sys.setdefaultencoding("utf-8")
import os
# import items
# import sys,os
# sys.path.append('../items.py')
# sys.path.append(os.path.abspath(os.path.dirname(Github) + '/'))

# os.path.join(os.path.join(os.path.dirname(__file__),os.pardir))
n=0
m_pra = 1
class WikiSpiderbanben(scrapy.Spider):

    name = 'wiki'
    allowed_domains = ["wikipedia.org"]
    # user = ""
    # password = ""
    start_urls = [""] * 5
    items = []

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            # 'authority': 'https://github.com/',
            # 'accept': 'application/json, text/javascript, */*; q=0.01',
            # 'accept-encoding': 'gzip, deflate',
            # 'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            # 'referer': 'https://github.com/',
            # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
            #               'Chrome/48.0.2564.97 Safari/537.36',
            # 'x-requested-with': 'XMLHttpRequest',
        },
    }

    # 伪装头部
    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://en.wikipedia.org",
    }

    def start_requests(self):
        # 读取需要爬取的用户名和密码
        # userFile = open("user.txt")
        # self.user = userFile.readline().strip('\n')
        # self.password = userFile.readline()
        # userFile.close()
        # 添加需要爬取的网页  https://en.wikipedia.org/w/index.php?title=Steve_Jobs&diff=prev&oldid=7097489
        self.start_urls[0] = "https://en.wikipedia.org"
        self.start_urls[1] = "https://en.wikipedia.org/w/index.php?title=Steve_Jobs&diff=next&oldid=54274058"
        # self.start_urls[1] = "https://en.wikipedia.org/w/index.php?title=Steve_Jobs&diff=next&oldid=1799944"

        # self.start_urls[2] = "https://en.wikipedia.org/w/index.php?title=Steve_Horn&diff=next&oldid=33215588"


        return [scrapy.Request(self.start_urls[1],
                        meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        # current_url = response
        # print current_url.url
        print response

        global n
        next_text = response.xpath("//div[@id='mw-diff-ntitle4']/a/@href").extract()
        if next_text:
            next_url = "https://en.wikipedia.org" + next_text[0]
            # print next_url
        else:
            self.parse(1)

        dfs = pd.read_html(response.url, attrs={"class": "diff diff-contentalign-left"})


        table = dfs[0]
        t_len = len(table.iloc[0,])
        if t_len==3:
            table[3] = np.nan
            str = next_url.split('oldid=')
            # str1 = str[1].split('&')
            banbenhao = str[1]
            row1 = table.iloc[0, 0]
            name1 = row1.split('(view source)')
            user_name1 = name1[0].split(' ')
            user_name = user_name1[0]
            file_banben = open("banbanhao.txt", 'a')
            file_banben.write(banbenhao + '\t' + user_name + '\n')
            file_banben.close()
            # table.to_csv(ss, index=False, sep=',', encoding='utf-8')
            # file_error = open("./data/a_error.csv", 'a')
            # file_error.write('test'+str(n)+'    '+str(response.url)+'\n')
            # file_error.close()
            # file_berror = open("./data/berror.csv", 'a')
            # file_berror.write('test' + str(n) + '    ' + str(response.url) + '\n')
            # file_berror.close()
            # ss = "./data/test" + str(n) + ".csv"
            # table.to_csv(ss, index=False, sep=',', encoding='utf-8')
            n = n + 1



        # if
        elif t_len == 4:
            str = next_url.split('oldid=')
            banbenhao = str[1]
            row1 = table.iloc[0, 0]
            name1 = row1.split('(view source)')
            name2 = name1[1].split('(')
            user_name1 = name2[0].split(' ')
            user_name  = user_name1[0]
            file_banben = open("banbanhao.txt", 'a')
            file_banben.write(banbenhao+'\t'+user_name+'\n')
            file_banben.close()
            # file_berror = open("./data/berror.csv", 'a')
            # file_berror.write('test' + str(n) + '    ' + str(response.url) + '\n')
            # file_berror.close()
            # ss = "./data/test" + str(n) + ".csv"
            # table.to_csv(ss, index=False, sep=',', encoding='utf-8')
            n = n + 1

        # elif t_len == 2:
        #     # file_error1 = open("./data/2222.csv", 'a')
        #     # file_error1.write('test' + str(n) + '    ' + str(response.url) + '\n')
        #     # file_error1.close()
        #     # print ('2222222222222222222222222222222222')
        #     # print (response.url)
        #
        #
        # elif t_len == 1:
        #     # file_error0 = open("./data/1111.csv", 'a')
        #     # file_error0.write('test' + str(n) + '    ' + str(response.url) + '\n')
        #     # file_error0.close()
        #     # print ('1111111111111111111111111111111')
        #     # print (response.url)
        #
        # elif t_len == 0:
        #     # file_error00 = open("./data/0000.csv", 'a')
        #     # file_error00.write('test' + str(n) + '    ' + str(response.url) + '\n')
        #     # file_error00.close()
        #     # print ('00000000000000000000000000000')
        #     # print (response.url)
        print n





        return [scrapy.Request(next_url,
                        meta={'cookiejar': response.meta['cookiejar']}, callback=self.post_login)]




    # 去掉list中所有元素中的换行符和空格
    @staticmethod
    def replace_space(arr):
        for i in range(len(arr)):
            arr[i] = arr[i].replace("\n", "").replace("\r", "").replace(" ", "")
        return arr

    # 去掉list中所有空元素,并且去掉list中所有元素中的换行符和空格
    @staticmethod
    def remove_null(arr):
        for i in range(len(arr)):
            arr[i] = arr[i].replace("\n", "").replace("\r", "").replace(" ", "")
        while "" in arr:
            arr.remove("")
        return arr

    # 返回arr第一个元素并去掉所有元素中的换行符和空格，如果第一个元素不存在则返回空
    @staticmethod
    def return_1(arr):
        if len(arr) != 0:
            arr[0] = arr[0].replace("\n", "").replace("\r", "").replace(" ", "")
            return arr[0]
        else:
            return ""



    def parse(self, response):
        print "爬虫结束"
        sys.exit(0)

