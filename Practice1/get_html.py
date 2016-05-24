#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://score.hanshintigers.jp/game/score/table/table20160506.html"
htmlfp = urllib2.urlopen(url)
html = htmlfp.read().decode("utf-8", "replace")
htmlfp.close()

soup = BeautifulSoup(html)
for link in soup.findAll("td"):
    print link
    print('合計' in link)
