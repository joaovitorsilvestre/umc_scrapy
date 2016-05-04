# -*- coding: utf-8 -*-
import requests
from html.parser import HTMLParser
parser = HTMLParser()

def html_umc(rgm,senha):
    with requests.Session() as c:
        url ='http://aluno.umc.br/entra.php'
        USERNAME = rgm
        PASSWORD = senha
        c.get(url)
        login_data = dict(txt_rgm=USERNAME, txt_senha=PASSWORD, entrar='Entrar')
        c.post(url, data=login_data, headers={"Referer": "http://aluno.umc.br/info01.php"})
        page =c.get('http://aluno.umc.br/index2.php?nPGMenu=1&nAplic=2')
        html = page.text

        html = parser.unescape(html)

        return(html)
