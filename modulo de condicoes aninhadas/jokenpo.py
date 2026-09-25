from random import randint
from time import sleep

itens = ('PEDRA','PAPEL','TESOURA')

computador = randint(0,2) #Computador joga
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura
 ''')

jogador = int(input("Qual é a sua jogada? ")) #Jogador joga

print('-='*12)
print("Pedra...")
sleep(1)
print("Papel...")
sleep(1)
print("e Tesoura!!!")
sleep(2)

print('-='*12)
print("Computador jogou {}" .format(itens[computador]))
print("Jogador jogou {}" . format(itens[jogador]))
print('-='*12)

if computador == 0: #Computador jogou Pedra
    if jogador == 1:
        print("Jogador venceu!")
    elif jogador == 2:
        print("Computador venceu!")
    elif jogador == 0:
        print("Eita, empatou!")
    else:   
             print("Jogada Inválida")
             
elif computador == 1: #Computador jogou Papel
    if jogador == 1:
        print("Eita, empatou!")
    elif jogador == 2:
        print("Jogador venceu!")
    elif jogador == 0:
        print("Computador venceu!")
    else:   
             print("Jogada Inválida")
             
elif computador == 2: #Computador jogou Tesoura
    if jogador == 1:
        print("Computador venceu!")
    elif jogador == 2:
        print("Eita, empatou!")
    elif jogador == 0:
         print("Jogador venceu!")
    else:   
         print("Jogada Inválida")
