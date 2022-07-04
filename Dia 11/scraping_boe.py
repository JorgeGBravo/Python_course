import bs4
import requests


url_boe = 'https://boe.es/diario_boe/xml.php?id=BOE-S-20141006'

result = requests.get(url_boe)
soup = bs4.BeautifulSoup(result.text, 'xml')
result = soup.select('sumario')

for seccion in result:
    departamento = seccion.select('departamento')
    for epigrafe in departamento:
        #print(epigrafe['nombre'])
        items = epigrafe.select('item')
        for item in items:
            print(f'id : {item["id"]}')
            print(f'control : {item["control"]}')
            titulo = item.select('titulo')[0]
            print(f'titulo : {titulo.string}')
            print(f'url : https://boe.es{item.urlXml.string}')
