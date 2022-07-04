import bs4
import requests
import datetime

def soap_result(url, label):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'xml')
    return soup.select(label)


date = datetime.datetime.now().strftime('%Y%m%d')
url_boe = f'https://boe.es/diario_boe/xml.php?id=BOE-S-{date}'
result = soap_result(url_boe, 'sumario')

if len(result) == 0:
    print('Introduce una fecha anterior con el siguiente formato AAAAMMDD')
    date = input('Dia: ')
    url_boe = f'https://boe.es/diario_boe/xml.php?id=BOE-S-{date}'
    result = soap_result(url_boe, 'sumario')

search = input('Busqueda: ')
for seccion in result:
    departamento = seccion.select('departamento')
    for epigrafe in departamento:
        items = epigrafe.select('item')
        for item in items:
            titulo = item.select('titulo')[0]
            if len(search) != 0:
                str_titulo = str(titulo)
                if search.lower() in str_titulo.lower():
                    print(f'id : {item["id"]}')
                    print(f'titulo : {titulo.string}')
                    url_search = (f'https://boe.es{item.urlXml.string}')
                    url_pdf = (f'https://boe.es{item.urlPdf.string}')
                    print(f'url : {url_pdf}')
                    search_result = soap_result(url_search, 'p')
                    for line in search_result:
                        print(line.string.center(20, ' '))
                    print('-' * 20)


            else:
                print(f'id : {item["id"]}')
                print(f'titulo : {titulo.string}')
                url_search = (f'https://boe.es{item.urlXml.string}')
                print(f'url : {url_search}')