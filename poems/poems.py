'''
下载古诗文网的推荐古诗
'''

import requests
import re
import threading
from queue import Queue
class Producer(threading.Thread):

    def __init__(self,page_queue,poem_queue,*args,**kwargs):
        self.page_queue = page_queue
        self.poem_queue = poem_queue
        super(Producer,self).__init__(*args,**kwargs)

    def parse_page(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text
        titles = re.findall(r'<p>.*?<a.*?><b>(.*?)</b>',html,re.DOTALL)
        dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',html,re.DOTALL)
        authors = re.findall(r'</span>.*?<a.*?>(.*?)</a>',html,re.DOTALL)
        contents_tag = re.findall(r'<div.*?class="contson".*?>.*?(.*?)</div>', html, re.DOTALL)
        contents = []
        for i in range(len(contents_tag)):
            content = re.sub(r'<.*?>','',contents_tag[i]).strip()
            contents.append(content)
        for i in zip(titles,dynasties,authors,contents):
            self.poem_queue.put(i)

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            # 把页面url传出队列
            url = self.page_queue.get()
            self.parse_page(url)

class Consummer(threading.Thread):

    def __init__(self,page_queue,poem_queue,*args,**kwargs):
        self.page_queue = page_queue
        self.poem_queue = poem_queue
        super(Consummer,self).__init__(*args,**kwargs)

    def run(self):
        while True:
            if self.page_queue.empty() and self.poem_queue.empty():
                break
            poem = self.poem_queue.get()
            with open('poems.txt','a+') as fp:
                fp.write(str(poem))
                fp.write('\n')
            print(poem[0] + '下载完成')

#运行函数
def main():
    page_queue = Queue(100)
    poem_queue = Queue(1000)
    for i in range(1,101):
        url = 'https://www.gushiwen.org/default_{}.aspx'.format(i)
        #把页面url传进队列
        page_queue.put(url)
    for i in range(3):
        t = Producer(page_queue,poem_queue)
        t.start()
    for i in range(3):
        t = Consummer(page_queue,poem_queue)
        t.start()

if __name__ == '__main__':
    main()


