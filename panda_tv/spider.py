'''
爬起熊猫直播人气排行
'''

# from urllib import request
from durations import duration
import re,requests
from durations import duration
class Spider():
    url='https://www.panda.tv/cate/lol?pdt=1.24.s1.3.1eu1vtp3uaj'
    root_pattern='<div class="video-info">([\s\S]*?)</div>'
    name_pattern='</i>([\d\D]*?)</span>'
    number_pattern='<span class="video-number">([\s\S]*?)</span>'
    #爬取页面
    def __htmlcontent(self):
        r=requests.get(Spider.url).content
        htmls=str(r,encoding='utf-8')
        return htmls

    #爬取直播名字和人气
    def __analysis(self,htmls):
        root=re.findall(Spider.root_pattern,htmls)

        anchors=[]
        for html in root:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_pattern,html)
            anchor={
                'name':name,
                'number':number
                }
            anchors.append(anchor)

        return anchors

    #整理字典
    def __refind(self,anchors):
        l=lambda anchors:{
            'name':anchors['name'][0].strip(),
            'number':anchors['number'][0]
        }
        return map(l,anchors)

    #排序     
    def __sort(self,anchors):
        return sorted(anchors,key = self.__sort_seed,reverse=True)
    
    #定义排序关键字
    def __sort_seed(self,anchor):
        r=re.findall('\d*',anchor['number'])
        number=float(r[0])
        if '万' in anchor['number']:
            number*=10000
        return number

    #打印
    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('Rank :'+str(rank+1)+'    : '+anchors[rank]['name'] +'    '+anchors[rank]['number'])

    #执行
    @duration
    def go(self):
        htmls=self.__htmlcontent()
        anchors=self.__analysis(htmls)
        anchors=list(self.__refind(anchors))
        anchors=self.__sort(anchors)
        self.__show(anchors)

if __name__ == '__main__':
    spider=Spider()
    spider.go()