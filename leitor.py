import requests
from bs4 import BeautifulSoup

class LeitorUrl:
    def buscarTag(url:str, tag:str):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        req = requests.get(url, headers)
        pagina_bs = BeautifulSoup(req.content,'html.parser')

        texto_tag = pagina_bs.find_all(tag)

        # texto = str(pagina_bs.prettify)

        return str(texto_tag).replace('[','',2).split(',')