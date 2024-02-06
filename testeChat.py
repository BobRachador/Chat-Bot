import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}Então {nome} eu fiz um curso de Desenvolvimento Web onde aprendi as competências HTML5, CSS3, JavaScript, PHP e Mysql{os.linesep} Atualmente estudando Orientação Objeta')
    if resposta == '2':
        print(f'{os.linesep}Eu moro na cidade de Curitiba no estado do Paraná')
    if resposta == '3':
        print(f'{os.linesep}Meu email de contato é richardgribsdev@gmail.com e meu numero de telefone é (041)92001-1389')
   
def start():
    print('Olá, me chamo Richard')

    nome = input("Qual o seu nome?: ")


    resposta = input(f'Você gostaria de saber...{os.linesep}[1] - Minha Experiência{os.linesep}[2] - Onde eu moro{os.linesep}[3] - Meu contato{os.linesep}')

    processar_resposta(resposta,nome)

if __name__ == '__main__':
    start()