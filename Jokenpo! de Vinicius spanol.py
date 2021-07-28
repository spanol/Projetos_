import random
print("***********Bem vindo ao jokenpo!**********")
jogar = input('Deseja iniciar?(S/N) ').upper()
cont = int(input('Quantos jogos serão? '))
possib_maquina = ["Pedra","Papel","Tesoura"]
jogada_player =  ["Pedra","Papel","Tesoura"]
Contagem_player = 0
Contagem_Maquina = 0
while jogar == 'S':
    while cont >= 1:
     jogada_player = input('Qual sua jogada? Pedra, Papel ou Tesoura? ')
     jogada_maquina = random.choice(possib_maquina)
    
     if jogada_player == jogada_maquina:
        print("Draw!")
        cont +=0
     
     elif jogada_player == "Pedra" or "pedra" and jogada_maquina == "Papel":
        print('Papel embrulha pedra!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -=1
        
    
     elif jogada_player == "Pedra" or "pedra" and jogada_maquina == "Tesoura":
        print('Pedra quebra tesoura!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -=1
        
    
     elif jogada_player == "Tesoura" or "tesoura" and jogada_maquina == "Papel":
        print('Tesoura corta o papel!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -=1
        
    
     elif jogada_player == "Tesoura" or "tesoura" and jogada_maquina == "Pedra":
        print('Pedra quebra a tesoura!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -=1
        
    
     elif jogada_player == "Papel" or "papel" and jogada_maquina == "Tesoura":
        print('A tesoura corta o papel!')
        print('Vitoria da maquina!')
        Contagem_Maquina += 1
        cont -=1
        
    
     elif jogada_player == "Papel" or "papel" and jogada_maquina == "Pedra":
        print('Papel embrulha a pedra!')
        print('Vitória do player!')
        Contagem_player += 1
        cont -=1
        
    if jogada_player not in (jogada_player):
      print('Resposta incorreta')
    
   
    jgdnv = input('Deseja jogar novamente?(S/N)').upper()
    if jgdnv == 'S':
         cont += int(input('Quantas vezes? '))
    else:
     print('Fim do programa!')
     print(f'O jogador tem {Contagem_player} pontos!')
     print(f'A maquina tem {Contagem_Maquina} pontos!')
     break

     
if Contagem_player > Contagem_Maquina:
    print('O jogador foi o grande campeão!!!')
else:
      print('A maquina foi a grande campeã!')