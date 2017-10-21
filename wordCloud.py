# coding=utf-8

from spider import Spider
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy
from PIL import Image


class wordCloudof19th():
    def getContent(self):
        spider = Spider()
        rsp = spider.getHtml('http://www.yocajr.com/news/16492/')
        content = spider.extraInfo(rsp, '/html/body/div[4]/div[1]/div[2]/text()')
        self.content = ''.join(content)
        return self.content

    def cut(self, content):
        seg_list = jieba.cut(content, cut_all=False)
        return ' '.join(seg_list)

    def analyse(self, content):
        seg_list = jieba.analyse.extract_tags(content, 180 ,True)
        for i in seg_list:
            print i[0], i[1]
        dic = {i[0] : i[1] for i in seg_list}
        return dic

    def generatebyText(self, text):
        wordCloud = WordCloud(font_path="res/simsun.ttf").generate(text)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def generateByFrequency(self, text):
        wordCloud = WordCloud(font_path="res/simsun.ttf").generate_from_frequencies(text)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def generateByMask(self, mask, text):
        wordCloud = WordCloud(font_path='res/simsun.ttf',mask=mask,background_color='white', max_words=180).generate_from_frequencies(text)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def wordCloudByText(self):
        content = self.getContent()
        text = self.cut(content)
        self.generatebyText(text)

    def wordCloudByFrequency(self):
        content = self.getContent()
        text = self.analyse(content)
        self.generateByFrequency(text)

    def wordCloudByMask(self):
        content = self.getContent()
        text = self.analyse(content)

        img = Image.open('res/mask.png')
        mask = numpy.array(img)
        self.generateByMask(mask, text)






if __name__ == '__main__':
    wc = wordCloudof19th()
    #wc.wordCloudByText()
    #wc.wordCloudByFrequency()
    wc.wordCloudByMask()