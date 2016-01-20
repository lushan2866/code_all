# -*- encoding:utf-8 -*-
import httplib
import urllib2
import random
import time

i = 0
while 1:
  url = 'http://vote.yucheng.gov.cn/vote_list.asp?ClassId=35&Topid=0'
  httplib.HTTPConnection.debuglevel = 1
  request = urllib2.Request(url)
  request.add_header("Accept", "*/*")
  request.add_header('Referer', "http://vote.yucheng.gov.cn/vote_list.asp?ClassId=35&Topid=0")
  request.add_header("Accept-Language", "zh-cn")
  request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; MyIE9; BTRS123646; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
  request.add_header("Accept-Encoding", "gzip, deflate")
  request.add_header("Host", "vote.yucheng.gov.cn")
  request.add_header("Connection", "Keep-Alive")
  opener = urllib2.build_opener()
  f = opener.open(request)
  print f.url

  i += 1
  print i
  time.sleep(6)