'''
获取不同版本的python及其下载地址
'''

from bs4 import BeautifulSoup
import requests

def getHtmlText(url,headers):
   try:
       response = requests.get(url,headers = headers)
       response.raise_for_status()
       response.encoding = response.apparent_encoding
       return response.text
   except:
       print('爬取异常')

def parser(html):
    info = []
    soup = BeautifulSoup(html,'html.parser')
    menu = soup.find(name = 'ol',attrs = {'class':'list-row-container menu'})
    lis = menu.find_all('li')
    #每个li标签包含一段信息
    for i in range(len(lis)):
        try:
            dict = {}
            a = lis[i].find(name = 'span',attrs = {'class':'release-number'}).find('a')
            name = a.text
            href = a['href']
            dict['版本'] = name
            dict['下载地址'] = href

            info.append(dict)
        except:
            continue
    return info

def show(info):
    for i in range(len(info)):
        print(info[i])
def main():
    url = 'https://www.python.org/downloads/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    html = getHtmlText(url,headers)
    info = parser(html)
    show(info)

if __name__ == '__main__':
    main()

