player1 = True
player2 = True
verifica = True


#Carregando o tabuleiro
from random import randint
letras_coluna = ['#' ,'1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11', '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' , '26']
numeros_linha = ['#' ,'1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11', '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' , '26']
tabuleiro = list()
tamanho = 8
cont = int(0)

while cont < (tamanho + 1):
   tabuleiro.append(['*']*(tamanho+1))
   cont += 1
cont = int(0)

while cont < tamanho:
   for coluna in tabuleiro[0]:
      tabuleiro[0][cont] = letras_coluna[cont]
      cont += 1
cont = int(0)

while cont < tamanho:
   for linha in tabuleiro:
      tabuleiro[cont][0] = numeros_linha[cont]
      cont += 1
cont = int(0)


#Printando o tabuleiro
for l in tabuleiro:
    print('')
    for c in l:
      print(c , end=' - ')
print('')

#Primeira jogada p1
p1linha = int(input('P1 - Digite a linha que você quer jogar: '))
while(p1linha>8 or p1linha<1):
  p1linha = int(input('P1 - Digite uma linha válida'))
p1coluna= int(input('P1 - Digite a coluna que você quer jogar: '))
while(p1coluna>8 or p1coluna<1):
  p1coluna = int(input('P1 - Digite uma coluna válida: '))
tabuleiro[p1linha][p1coluna] = 'X'

p1linhaUltimaJogada = p1linha
p1colunaUltimaJogada = p1coluna

#Primeira jogada p2
p2linha = int(input('P2 - Digite a linha que você quer jogar: '))
while(p2linha>8 or p2linha<1):
  p2linha = int(input('P2 - Digite uma linha válida'))
p2coluna= int(input('P2 - Digite a coluna que você quer jogar: '))
while(p2coluna>8 or p2coluna<1):
  p2coluna = int(input('Digite uma coluna válida'))

#Validação se ele jogou na mesma posição do jogador 1
if(tabuleiro[p1linhaUltimaJogada][p1colunaUltimaJogada] == tabuleiro[p2linha][p2coluna]):
  print('Posição inválida, igual ao player 1')
  p2linha = int(input('P2 - Digite a linha que você quer jogar: '))
  while(p2linha>8 or p2linha<1):
    p2linha = int(input('P2 - Digite uma linha válida'))
  p2coluna= int(input('P2 - Digite a coluna que você quer jogar: '))
  while(p2coluna>8 or p2coluna<1):
    p2coluna = int(input('Digite uma coluna válida'))

p2linhaUltimaJogada = p2linha
p2colunaUltimaJogada = p2coluna
tabuleiro[p2linha][p2coluna] = 'O'

#print do tabuleiro após as jogadas
for l in tabuleiro:
  print('')
  for i in l:
    print(i, end=' - ')
print('')

#Começo do loop que irá acabar só quando alguem ganhar
while(player1 and player2):
  verifica = True
  while(verifica):
    #Validando se a linha está conhicidindo com o tamanho do tabuleiro
    p1linha = int(input('P1 - Digite a linha que você quer jogar: '))
    while(p1linha>8 or p1linha<1):
      p1linha = int(input('P1 - Digite uma linha válida: '))

    #Validando se a coluna está conhicidindo com o tamanho do tabuleiro
    p1coluna= int(input('P1 - Digite a coluna que você quer jogar: '))
    while(p1coluna>8 or p1coluna<1):
      p1coluna = int(input('P1 - Digite uma coluna válida: '))

    #Validação se o lugar escolhido já tinha sido escolhido anteriormente
    if  (tabuleiro[p1linha][p1coluna] == '*'):
      #Validando se a jogada foi ao lado da jogada anterior
      if ((p1linhaUltimaJogada == p1linha+1 and p1colunaUltimaJogada==p1coluna) or (p1linhaUltimaJogada == p1linha-1 and p1colunaUltimaJogada==p1coluna) or (p1colunaUltimaJogada == p1coluna+1 and p1linhaUltimaJogada==p1linha) or (p1colunaUltimaJogada == p1coluna-1 and p1linhaUltimaJogada==p1linha)):
        verifica = False
        p1linhaUltimaJogada = p1linha
        p1colunaUltimaJogada = p1coluna
        tabuleiro[p1linha][p1coluna] = 'X'
      else:
        print('[JOGADA INVÁLIDA] - A jogada tem de ser ao lado da ultima que você jogou')
    else:
      print('[JOGADA INVÁLIDA] - A jogada tem de ser em um lugar nunca jogado')

  for l in tabuleiro:
     print('')
     for i in l:
       print(i, end=' - ')
  print('')


  #Verificação se o p1 perdeu
  if(p1linha == 1 and p1coluna == 8):
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif(p1linha == 8 and p1coluna <= 7):
    if(tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna+1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif(p1linha == 8 and p1coluna == 8):
    if(tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif((p1linha>1 and p1linha<8) and p1coluna==8):
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  else:
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna+1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break

  #Verificação se o p2 perdeu
  if(p2linha == 1 and p2coluna == 8):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif(p2linha == 8 and p2coluna <= 7):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif(p2linha == 8 and p2coluna == 8):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif((p2linha>1 and p2linha<8) and p2coluna==8):
    if(tabuleiro[p2linha+1][p2coluna] != '*' and tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  else:
    if(tabuleiro[p2linha+1][p2coluna] != '*' and tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break

#VEZ DO P2----------------------------

  verifica = True
  while(verifica):
    #recebendo uma linha está conhicidindo com o tamanho do tabuleiro
    p2linha = int(input('P2 - Digite a linha que você quer jogar: '))
    while(p2linha>8 or p2linha<1):
      p2linha = int(input('P2 - Digite uma linha válida: '))

    #recebendo uma coluna está conhicidindo com o tamanho do tabuleiro
    p2coluna= int(input('P2 - Digite a coluna que você quer jogar: '))
    while(p2coluna>8 or p2coluna<1):
      p2coluna = int(input('P2 - Digite uma coluna válida: '))

    #Validação se o lugar escolhido já tinha sido escolhido anteriormente
    if  (tabuleiro[p2linha][p2coluna] == '*'):
      #Validando se a jogada foi ao lado da anterior
      if ((p2linhaUltimaJogada == p2linha+1 and p2colunaUltimaJogada == p2coluna) or (p2linhaUltimaJogada == p2linha-1 and p2colunaUltimaJogada == p2coluna) or (p2colunaUltimaJogada == p2coluna+1 and p2linhaUltimaJogada == p2linha) or (p2colunaUltimaJogada == p2coluna-1 and p2linhaUltimaJogada == p2linha)):
        verifica = False
        p2linhaUltimaJogada = p2linha
        p2colunaUltimaJogada = p2coluna
        tabuleiro[p2linha][p2coluna] = 'O'
      else:
        print('[JOGADA INVÁLIDA] - A jogada tem de ser ao lado da ultima que você jogou')
    else:
      print('[JOGADA INVÁLIDA] - A jogada tem de ser em um lugar nunca jogado')

    for l in tabuleiro:
      print('')
      for i in l:
        print(i, end=' - ')
    print('')



      #Verificação se o p1 perdeu
  if(p1linha == 1 and p1coluna == 8):
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif(p1linha == 8 and p1coluna <= 7):
    if(tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna+1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif(p1linha == 8 and p1coluna == 8):
    if(tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  elif((p1linha>1 and p1linha<8) and p1coluna==8):
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break
  else:
    if(tabuleiro[p1linha+1][p1coluna] != '*' and tabuleiro[p1linha-1][p1coluna] != '*' and tabuleiro[p1linha][p1coluna+1] != '*' and tabuleiro[p1linha][p1coluna-1] != '*'):
      player1 = False
      break

  #Verificação se o p2 perdeu
  if(p2linha == 1 and p2coluna == 8):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif(p2linha == 8 and p2coluna <= 7):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif(p2linha == 8 and p2coluna == 8):
    if(tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  elif((p2linha>1 and p2linha<8) and p2coluna==8):
    if(tabuleiro[p2linha+1][p2coluna] != '*' and tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break
  else:
    if(tabuleiro[p2linha+1][p2coluna] != '*' and tabuleiro[p2linha-1][p2coluna] != '*' and tabuleiro[p2linha][p2coluna+1] != '*' and tabuleiro[p2linha][p2coluna-1] != '*'):
      player2 = False
      break

for l in tabuleiro:
   print('')
   for i in l:
    print(i, end=' - ')
print('')
print('')

if(player1):
  print(f'TEMOS UM VENCEDOR, PARABÉNS PLAYER 1, VOCÊ GANHOU')
else:
  print('TEMOS UM VENCEDOR, PARABÉNS PLAYER 2, VOCE GANHOU')

