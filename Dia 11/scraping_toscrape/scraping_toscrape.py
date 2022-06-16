import bs4
import requests

stars = 'Four', 'Five'
url_base = 'http://books.toscrape.com/catalogue/'
url = 'http://books.toscrape.com/'

execution = True

while execution:
    print(url)
    result = requests.get(url)

    soup = bs4.BeautifulSoup(result.text, 'lxml')

    result_pages_article = soup.select('.product_pod')
    result_pages_li = soup.find_all('li', attrs={"class": "next"})

    for star in result_pages_article:
        for article in result_pages_article:
            for h3 in article.select('h3'):
                for a in h3.select('a'):
                    for p in star.select('p'):
                        if p['class'][0] == 'star-rating':
                            if p['class'][1] in stars:
                                print(a['title'])
                                print(p['class'][1] + 'Stars')

    if len(result_pages_li) != 0:
        for li in result_pages_li:
            for a in li.select('a'):
                if 'page' in a['href']:
                    if a['href'] == 'catalogue/page-2.html':
                        new_url = 'http://books.toscrape.com/' + a['href']
                        url = new_url
                        pass
                    else:
                        new_url = url_base + a['href']
                        url = new_url
    else:
        print('false')
        execution = False




'''        for p in article.select('p'):
            try:
                if p['class'][1] != 'availability':
                    if p['class'][1] in stars:
                        for h3 in article.select('h3'):
                            for a in h3.select('a'):
                                print(a['title'])
                                print(p['class'][1] + 'Stars')
            except:
                pass

     if len(result_pages_li) != 0:
        for li in result_pages_li:
            for a in li.select('a'):
                if 'page' in a['href']:
                    if a['href'] == 'catalogue/page-2.html':
                        new_url = 'http://books.toscrape.com/' + a['href']
                        url = new_url
                        pass
                    else:
                        new_url = url_base + a['href']
                        url = new_url
    else:
        print('false')
        execution = False '''