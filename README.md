# UMC Scrapy

Um simples algoritimo para fazer a busca das notas do portal do aluno da Universidade de Mogi das Cruzes.

O algoritimo retorna uma lista com sublistas. Cada sublista é referente a uma matéria encontrada.

Para utilizar chame a função Inicializar que está no Buscar_notas.py, lembrando que a função leva dois argumentos,
o rgm e a senha, ambos em formato de string.

A resposta esperada deverá ser como o exemplo a seguir:

['09489-ALGORITMOS', '1', '9.5', '6.6', '7.5', '6.9', '7.8', 0, 0, 0, 0, 'CURSANDO', '4']
['09499-INTRODUÇÃO À REDES DE COMPUTADORES', '1', '6.8', '6.0', '7.5', '6.5', '6.6', 0, 0, 0, 0, 'CURSANDO', '0']
['12154-TÉCNICAS DE PROGRAMAÇÃO I', '1', '9.1', '7.5', '7.5', '7.5', '8', 0, 0, 0, 0, 'CURSANDO', '0']
['12304-ÉTICA E LEGISLAÇÃO EM TECNOLOGIA DA INFORMAÇÃO', '1', '8.0', '10', '7.5', '9.3', '8.9', 0, 0, 0, 0, 'CURSANDO', '0']
['13211-ORGANIZAÇÃO DE COMPUTADORES E SOFTWARE BÁSICO', '1', '6.8', '8.4', '7.5', '8.1', '7.7', 0, 0, 0, 0, 'CURSANDO', '4']
['13212-FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO', '1', '10', '8.5', '7.5', '8.2', '8.8', 0, 0, 0, 0, 'CURSANDO', '0']
['13301-ATIVIDADES COMPLEMENTARES', '1', 0, 0, 0, 0, '0', 0, 0, 0, 'SUF', 'APROVADO', 0]
['14790-LÍNGUA BRASILEIRA DE SINAIS - LIBRAS (OPTATIVA)', '1', 0, 0, 0, 0, '0', 0, 0, 0, 0, 'CURSANDO', 0]
