from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
baseUrl = 'http://clien.net/cs2/bbs/'
html = urlopen(baseUrl + 'board.php?bo_table=news')
bs = BS(html)
titleList = bs.select('td.post_subject a')
for title in titleList:
    url = title.attrs['href']
    html = urlopen(baseUrl + url)
    bs = BS(html)
    contents = bs.select('.view_content')

    fileName = url.split('=')[-1]

    #print(contents[0].text)
    #f = open(fileName + '.txt','w',encoding="utf-8")
    #f.write(contents[0].text)
    #f.close

    print(fileName)