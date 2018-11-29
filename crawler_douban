'''
爬取豆瓣影评和评分
'''
import requests,re
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        response = requests.get(url)
        response.raise_for_status
        response.encoding = 'utf-8'
        return response.text
    except:
        print('爬取异常')

def parser(html,shortlist,scoresum):
    try:
        soup = BeautifulSoup(html,'html.parser')
        short = soup('span','short')
        #每人的评分
        score = re.findall('<span class="user-stars allstar(.*?)rating',html)

        for i in range(len(short)):
            shortlist.append(short[i].string)
        for x in score:
            scoresum +=int(x)
        return scoresum
            
    except:
        print('解析异常')

def printShort(shortlist,scoresum):
    for i in range(len(shortlist)):
        print('书评' + str(i+1)+' : ')          
        print(shortlist[i],'\n')
    print('本书评分为：%.1f' % (scoresum/int(i+1)))
    

def main():
    shortlist = []
    scoresum = 0
    for i in range(1,4):
        try:
            if i == 1:
                #此处修改url
                url = 'https://book.douban.com/subject/30271484/comments/'
            else:
                url = 'https://book.douban.com/subject/30271484/comments/hot?p=%s' % i
            html = getHtmlText(url)
            scoresum = parser(html,shortlist,scoresum)
        except:
            break
        printShort(shortlist,scoresum)

if __name__ == '__main__':
    main()
    
