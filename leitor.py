import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status"
req = requests.get(url, headers)
pagina_bs = BeautifulSoup(req.content,'html.parser')

print(pagina_bs.find_all("a"))

# texto = str(pagina_bs.prettify)

# print(texto)
print('Terminado o trabalho!!!')