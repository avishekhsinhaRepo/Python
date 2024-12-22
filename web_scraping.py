import requests, bs4
basePath = "https://www.aarpmedicareplans.com";
result = requests.get(basePath)
soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup.select('title')[0].getText())

image =soup.select('img.loadOnlyDesktop')[0]
imgSrc = image['data-src']
downloaded_image_link = requests.get(basePath + imgSrc)
print(downloaded_image_link.content)
downloaded_image = open('downloaded_image.jpg', 'wb')
downloaded_image.write(downloaded_image_link.content)
downloaded_image.close()