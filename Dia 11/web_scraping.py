import bs4
import requests

result = requests.get('https://escueladirecta.com/p/trucos-y-atajos-de-excel')

#print(type(result))
#print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')

#print(soup)
#print(soup.select('title'))
#print(soup.select('title')[0].getText())
#print(soup.select('p'))

p_special = soup.select('p')[9].getText()
#print(p_special)

extract_div = soup.select('div')[9]
#print(extract_div.getText().strip().rstrip())
#print(type(extract_div.getText()))
#print(len(p_special))

extract_content = soup.select('p')
#print(extract_content)

#for i in extract_content:
#    print(i.getText())

# Capture images

result_images = requests.get('https://escueladirecta.com/courses')
soup_images = bs4.BeautifulSoup(result_images.text, 'lxml')


extract_images = soup_images.select('img')
extract_select_images = soup_images.select(('.course-box-image'))
#print(extract_images)

for i in extract_select_images:
    print(i['src'])

extract_image_get = extract_select_images[0]['src']
image_get = requests.get(extract_image_get)
#print(image_get.content)
#f = open('image_get.jpg', 'wb')
#f.write(image_get.content)
#f.close()
