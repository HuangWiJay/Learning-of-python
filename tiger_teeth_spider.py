'''
爬取虎牙tv主播人气排行
'''

import requests,re
from bs4 import BeautifulSoup

class HuyaSpider():
   
    #爬取页面
    def __getHtmlText(self,url):
        try:
            r = requests.get(url)
            r.raise_for_status
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print('爬取页面异常')
   
    #获取数据并形成字典
    def __parser(self,html,anchros):
        namelist = re.findall('<i class="nick" title="(.*?)"',html)
        numberllist = re.findall('<i class="js-num">(.*?)</i>',html)
        
        for i in range(len(namelist)):
            anchros.append([namelist[i],numberllist[i]])
        
        l = lambda anchro:{'name':anchro[0],'number':anchro[1]}
        return map(l,anchros)

    #排序
    def __sort(self,anchros):
        return sorted(anchros,key = self.__sort_seed,reverse = True)

    # 排序规则
    def __sort_seed(self,anchro):
        r=re.findall('\d*',anchro['number'])
        number=float(r[0])
        
        if '万' in anchro['number']:
            number *= 10000
        return number
   
    #打印
    def __print(self,anchros):
        demo = '{0:^4}\t{1:^15}\t{2:^10}'
        print(demo.format('排名','主播名字','当前观看人数'))
        for i in range(len(anchros)):
            print(demo.format(i+1,anchros[i]['name'],anchros[i]['number']))
    
    def main(self):
        anchros = []
        url ='https://www.huya.com/g/wzry'
        html = self.__getHtmlText(url)
        anchros = list(self.__parser(html,anchros))
        anchros = self.__sort(anchros)
        self.__print(anchros)
        
spider = HuyaSpider()
spider.main()