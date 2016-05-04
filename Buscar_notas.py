# -*- coding: utf-8 -*-
from Get_html_Notas import html_umc
import re

def Curso_Scraping(site_str):
    ## Nome do Curso
    regex = '<span style="display: inline;">&nbsp;(.+?)</span>'
    pattern = re.compile(regex)

    curso_find = re.findall(pattern, site_str)

    while len(curso_find)>1:    # caso ache um ou mais nomes de curso
        curso_find.pop(1)       # apaga os restantes

    ## Nome do estudante
    regex = '<td class="textomeu1" style="text-transform:uppercase; width:200px; float:left">&nbsp;(.+?)</td>'
    pattern = re.compile(regex)

    aluno_find = re.findall(pattern, site_str)

    #curso_find.append(aluno_find[0])  ## adiciona o nome do estudante a lista do curso
    return (curso_find)

def Materias_Scraping(site_str):
    regex = '<td class="textomeu1" align="left">(.+?)</td>'
    pattern = re.compile(regex)

    materias_find = re.findall(pattern,site_str)

    return (materias_find)

# essa função executa a Curso_Scraping e Materias_scraping entao junta toda a informação em uma unica lista
def Notas_Scraping(site_str):
    regex = '<td class="textomeu1" align="center">(\s*\S*)</td>'    ## (\s*\S*) acha espaços com ou sem caracteres
    pattern = re.compile(regex)

    N_final_find = re.findall(pattern, site_str)

    ##  refaz a busca para as Notas ND e N1 pois as mesmas necessitam tem outro padrao no html
    regex = '<td class="textomeu1" colspan="1">(\s*\S*)</td>'
    pattern = re.compile(regex)

    N1_ND_find = re.findall(pattern, site_str)

    notas_find = []  #lista final que contem todas as notas

    # aqui é criada uma sublista dentro da lista notas_find, cada sublista é uma materia com o nome e suas notas
    a = -1
    b = 0
    for nome in Materias_Scraping(site_str):    # para cada materia encontrada
        a += 1
        notas_find.append([nome])       # adiciona uma sublista com o nome da materia encontrada
        ## aqui as notas seram adicionadas na sublista correspondente
        for num in range(b,b+10):

            notas_find[a].append(N_final_find[num])
        b += 10                         # esta variavel evita que seja adicionadas as mesmas notas para todas as sublistas

    num = 0                                         ## faz a contagem para dizer qual valor vai ser inserido, ND e NI
    for materia in range(0,len(notas_find)):
        notas_find[materia].insert(3,N1_ND_find[num+1])  ## insere na sub lista ND
        notas_find[materia].insert(3,N1_ND_find[num])    ## insere na sub lista NI
        num += 2                                    ## soma dois para que a proxima dupla de ND e NI seja adicionada


    #### verifica cada nota se é '' ou ' ' e troca por zero, pois no site o espaço vazio representa nota ainda nao colocada
    for item in range(0,len(notas_find)):
        for num in range(2,13):
            if notas_find[item][num] == ' ' or notas_find[item][num] == '':
                notas_find[item][num] = 0

    return (notas_find)         # retorna tudo em listas e sublistas

def Inicializar(rgm,senha):
    site_str = html_umc(rgm,senha)
    return Notas_Scraping(site_str)     # retorna uma lista de listas

### cheme a função inicializar com os dois argumentos rgm e senha, ambos em string