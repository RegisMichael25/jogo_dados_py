#Sic Bo:
import random
num = [random.randint(1, 6) for _ in range(3)]

print("Bem-vindo ao Sic Bo!")
print("Escolha qual modo de jogo deseja jogar:")
print("1. Adivinhar a soma dos três dados")
print("2. Adivinhar se um dos dados será um número específico (1-6)")
print("3.Sair")

mode = input("Digite o número do modo de jogo que deseja jogar: ")
if mode not in ['1', '2', '3']:
    print("Escolha inválida. Tente novamente.")
    exit()

def game_mode(mode):
    match mode:
        case '1':
            guess_sum()
        case '2':
            guess_specific()
        case '3':
            print("Obrigado por jogar! Até a próxima.")
            exit()

def guess_sum():
    print("Tente adivinhar a soma dos três dados (entre 3 e 18).")
    palpite = input("Qual é o seu palpite para a soma dos três dados? ")
    if palpite.isdigit() and int(palpite) == sum(num):
        print("Parabéns! Você acertou o palpite.")
    else:
        print("Que pena! Você errou o palpite.")

def guess_specific():
    palpite = input("Qual é o seu palpite para o número de um dos três dados? ")
    if palpite.isdigit() and int(palpite) in num:
        print("Parabéns! Você acertou o palpite.")
        
    else:
        print("Que pena! Você errou o palpite.")

print("Números sorteados:", num)

game_mode(mode)