# -*- coding:utf-8 -*-

import requests
from urllib import parse

username = 'llss6887'
repos = 'myblog'
#title = 'demo1'
#label = '/blog/article/87'
domain = 'http://heimamba.com'
token = 'b0ccf54d3653f8ff596058a54a9dc67cf627c534'


def autoTalk(title, label):
    doUrl = 'https://api.github.com/repos/%s/%s/issues' % (username, repos)

    param = "{\"title\":\"%s\",\"labels\":[\"%s\", \"Gitalk\"],\"body\":\"%s%s\\n\\n\"}" % ('ceshi', label, domain, label)
    #param = parse.quote_plus(param)
    header = {"accept": "*/*", "connection": "Keep-Alive",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
              "Authorization": "token %s" % token}
    sesson = requests.session()
    post = sesson.post(doUrl, data=param, headers=header)
