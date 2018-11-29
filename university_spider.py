
'''
爬取中国最好大学排行
'''

from bs4 import BeautifulSoup
import bs4,requests

class Spider():

    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'

    #爬取页面
    def __GetHtmlText(self):
        try:
            r=requests.get(Spider.url,timeout=30)
            r.raise_for_status
            r.encoding=r.apparent_encoding
            return r.text
        except:
            print('爬取失败')

    #分析页面并把数据装进列表       
    def __analysis(self,htmls):
        anchors=[]
        soup=BeautifulSoup(htmls,'html.parser')
        for tr in soup.find('tbody').children:
           if isinstance(tr,bs4.element.Tag):
               tds=tr('td')
               anchors.append([tds[0].string,tds[1].string,tds[3].string])
        return anchors

    #打印列表    
    def __show(self,anchors,number):
        flag='{0:^10}\t{1:{3}^10}\t{2:^10}'
        
        print(flag.format('排名','大学名称','总分',chr(12288)))
        
        for x in range(number):
            u=anchors[x]
            print(flag.format(u[0],u[1],u[2],chr(12288)))
    
    # 执行函数
    def go(self,number):
        htmls=self.__GetHtmlText()
        anchors=self.__analysis(htmls)
        self.__show(anchors,number)

spider=Spider()
spider.go(66)
