import requests
from bs4 import BeautifulSoup
url="https://github.com/"

r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')

#print(soup.prettify())

# markup="<p><!....this is a comment....></p>"
# soup2=BeautifulSoup(markup)
# print(type(soup2.p.string))
# exit()

title=soup.title
#print(title)

paras = soup.find_all('p')
#print(paras)




print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find("p",class_='lead'))

print(soup.find('p').get_text())
print(soup.get_text())

anchors = soup.find_all('a')
#print(anchors)
all_links=set()
for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://github.com/"+link.get('href')
        all_links.add(link)
        print(linkText)
    
navbarSupportedContent=soup.find(id="navbarSupportedContent")
for elem in navbarSupportedContent.contents:
    print(elem)    