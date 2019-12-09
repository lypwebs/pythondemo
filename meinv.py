# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup  #从网页抓取数据
import urllib3,urllib.request
x = 0;
urls = ['https://www.buxiuse.com/?page={}'.format(str(i)) for i in range(5,11)]
for url in urls:
    def crawl(url):  # 模拟浏览器  加上headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        req = urllib.request.Request(url, headers=headers)  # 用地址创建一个request对象
        page = urllib.request.urlopen(req, timeout=20)  # 打开网页
        contents = page.read()  # 获取源码
        soup = BeautifulSoup(contents, features="lxml")
        my_girl = soup.find_all('img')
        for girl in my_girl:
            link = girl['src']
            global x
            urllib.request.urlretrieve(link, "image\%s.jpg" % x)  # 下载
            print("爬取完第" + str(x) + "张")
            x += 1
    crawl(url)

