#Sic Bo:
import random
num = [random.randint(1, 6) for _ in range(3)]

def guess_sum(resultado = None):
    num = [random.randint(1, 6) for _ in range(3)]
    print("Tente adivinhar a soma dos três dados (entre 3 e 18).")
    palpite = input("Qual é o seu palpite para a soma dos três dados? ")
    
    if resultado is not None:
        print(resultado)
        if resultado == '1':
             if num[0] < 1:
                num[0] = 1
                num[1] = (palpite - num[0]) // 2
                num[2] = palpite - num[0] - num[1]
             elif num[0] > 6:
                num[0] = 6
                num[1] = (palpite - num[0]) // 2
                num[2] = palpite - num[0] - num[1]
        else:
            print(resultado)
            while sum(num) == int(palpite):
                num = [random.randInt(1,6) for _ in range(3)]
    
    print(f"Dados: {num} | Soma: {sum(num)}")
    
    ganhou = (palpite.isdigit() and int(palpite) == sum)

def guess_specific():
    num = [random.randint(1, 6) for _ in range(3)]
    palpite = input("Qual é o seu palpite para o número de um dos três dados? ")
    if palpite.isdigit() and int(palpite) in num:
        print("Parabéns! Você acertou o palpite.")
        
    else:
        print("Que pena! Você errou o palpite.")

print("Números sorteados:", num)
