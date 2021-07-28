##############################################################################################################################
candidatos = {'nome':'Jair Messi Bolonaro','votos':0},{'nome':'Lulindro Da Silva','votos':0},{'nome':'Joao Semmedo','votos':0}, {'nome':'Nulo','votos':0},{'nome':'Branco','votos':0}

def votacao(cand,autorizacao):
    if autorizacao == True:
        candidatos[cand-1]['votos'] += 1 #puxa no dict o escolhito candidato
        for i in candidatos:      #ambas trabalham com o dict
            for k,v in i.items():    #
                print(v)  #printa o valor 'votos', ainda não consegui printar o mais votado tentei até o MAX mas n foi
        print(f'Você votou em {candidatos[cand-1]["nome"]}')
    
def autoriza_voto(ano):
     idade = 2021 - ano
     if idade >= 18:
         print(f'Autorização: Autorizado, você é maior de idade com {idade} anos e sua participação na votação é obrigatória!!!') 
         return True
         

     elif idade == 17 and idade == 16 or idade >= 70:
         print(f'Autorização: Autorizado, você tem {idade} anos e sua participação na votação é opcional!!!')
         return True
     
     elif idade < 16:
         print('Autorização: Negado, você tem menos de 16 anos e não pode participar da votação!!! ')
         return False

print('_______________________________________________________________')
inicio = input('Deseja iniciar a votação?(S/N)').upper()
print('_______________________________________________________________')
while inicio == 'S': 
    print('________________________Votação____2021________________________')
    print('_______________________________________________________________')
    print('________________________________________________________________')
    ano = int(input('Digite seu ano de nascimento para validação de dados! '))
    autorizacao = autoriza_voto(ano)
    print('_______________________________________________________________')
    print('[1] Jair Messi Bolonaro [2] Lulindro Da Silva [3] Joao Semmedo [4] Nulo  [5] Branco')
    print('_______________________________________________________________')
    cand = int(input('Em quem deseja votar? '))
    votacao(cand,autorizacao)
    print('____________________Obrigado por votar!!!____________________')
    inicio = input('Deseja continuar votando?').upper()

#############################################################################################################################