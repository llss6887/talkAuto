# -*- coding:utf-8 -*-


import requests
from lxml import etree

from talkAuto.TalkAuto import autoTalk

url = 'http://localhost:8082'
header = {"accept": "*/*", "connection": "Keep-Alive",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}


def talkAuto(title, lable):
    for index, value in enumerate(title):
        t = value.strip()
        l = lable[index]
        autoTalk(t, l)


def get_url(uri):
    res = requests.get(uri, headers=header)
    html = etree.HTML(res.text)
    xpath = html.xpath('//*[@class="blog-content"]/a/@href')
    title = html.xpath('//*[@id="grid"]/li/section/article/text()')
    split_ = html.xpath("//li[@class='next']/a/@href")
    talkAuto(title,xpath)
    if split_:
        split_ = split_[0].split(';')[0]
        get_url(url+split_)


if __name__ == '__main__':
    get_url(url)
    print("done")


