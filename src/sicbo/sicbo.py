#Sic Bo:
import random
numeros = [random.randint(1, 6) for _ in range(3)]

palpite = input("Qual é o seu palpite para a soma dos três dados? ")

for _ in numeros:
    if palpite.isdigit() and int(palpite) in numeros:
        print("Parabéns! Você acertou o palpite.")
        break
    else:
        print("Que pena! Você errou o palpite.")

print("Números sorteados:", numeros)
print("Soma dos números:", sum(numeros))

if palpite.isdigit() and int(palpite) == sum(numeros):
    print("Parabéns! Você acertou o palpite.")
else:
    print("Que pena! Você errou o palpite.")
