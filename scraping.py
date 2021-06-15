import requests
from bs4 import BeautifulSoup

termos = ['php', 'javascript', 'python', 'java', 'c']
contador = 0
iterador = len(termos)

while contador < iterador:

    for termo in termos:
        tag = termo
        arquivo = 'relatorio_'+tag+'.txt'

        with open(arquivo, 'w') as relatorio:

            url = 'https://pt.stackoverflow.com/questions/tagged/'+tag
            response = requests.get(url)
            html = BeautifulSoup(response.text, 'html.parser')

            for pergunta in html.select('.question-summary'):
                titulo = pergunta.select_one('.question-hyperlink')
                data = pergunta.select_one('.relativetime')
                votos = pergunta.select_one('.vote-count-post')

                relatorio.write(
                    f'PERGUNTA: {titulo.text} \nDATA: {data.text} \nVOTOS: {votos.text}\n\n')

            print('Relatório gerado com sucesso!')
            contador += 1
    print(f'TOTAL: {iterador} relatório(s) gerado com sucesso.')
