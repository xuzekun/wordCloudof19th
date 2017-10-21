# coding=utf-8

import requests
from lxml import html
import os

class Spider():
	def getHtml(self, url, retryNum=5):
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
		try:
			rsp = requests.get(url, headers=headers, timeout=20)
		except Exception as e:
			if retryNum > 0:
				return self.getHtml(url, retryNum - 1)

		if rsp.status_code == 200:
			return rsp.content
		else:
			if retryNum > 0:
				return self.getHtml(url, retryNum-1)

	def extraInfo(self, htmlPage, xpath):
		tree = html.fromstring(htmlPage)
		lists = tree.xpath(xpath)
		if len(lists) == 1:
			return lists[0]
		return lists




if __name__ == '__main__':
    spider = Spider()
    rsp = spider.getHtml('http://www.yocajr.com/news/16492/')
    c = spider.extraInfo(rsp,'/html/body/div[4]/div[1]/div[2]/text()')
    print ''.join(c)