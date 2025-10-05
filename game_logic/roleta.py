# game_logic/roleta.py
import random
import time

# Dicionário representando as cores dos números na roleta europeia
ROULETTE_POCKETS = {
    0: 'verde', 1: 'vermelho', 2: 'preto', 3: 'vermelho', 4: 'preto', 5: 'vermelho',
    6: 'preto', 7: 'vermelho', 8: 'preto', 9: 'vermelho', 10: 'preto', 11: 'preto',
    12: 'vermelho', 13: 'preto', 14: 'vermelho', 15: 'preto', 16: 'vermelho', 17: 'preto',
    18: 'vermelho', 19: 'vermelho', 20: 'preto', 21: 'vermelho', 22: 'preto', 23: 'vermelho',
    24: 'preto', 25: 'vermelho', 26: 'preto', 27: 'vermelho', 28: 'preto', 29: 'preto',
    30: 'vermelho', 31: 'preto', 32: 'vermelho', 33: 'preto', 34: 'vermelho', 35: 'preto',
    36: 'vermelho'
}

def spin_wheel():
    """Simula o giro da roleta e retorna o número e a cor."""
    print("\nA roleta está girando...")
    time.sleep(1.5)
    numero_sorteado = random.randint(0, 36)
    cor_sorteada = ROULETTE_POCKETS[numero_sorteado]
    print(f"A bola caiu no... {numero_sorteado} ({cor_sorteada.upper()})!")
    return numero_sorteado, cor_sorteada

def apostar_cor(deve_ganhar):
    """
    O jogador aposta em Vermelho ou Preto.
    O resultado é manipulado pela variável 'deve_ganhar'.
    """
    while True:
        aposta_cor = input("Qual cor você escolhe (vermelho/preto)? ").lower()
        if aposta_cor in ['vermelho', 'preto']:
            break
        else:
            print("Escolha inválida. Por favor, digite 'vermelho' ou 'preto'.")

    # Lógica de manipulação do resultado
    numero_final, cor_final = 0, ''

    if deve_ganhar:
        # Força uma vitória, garantindo que a cor sorteada seja a da aposta
        while True:
            num, cor = spin_wheel()
            if cor == aposta_cor:
                numero_final, cor_final = num, cor
                break
    else:
        # Força uma derrota, garantindo que a cor sorteada NÃO seja a da aposta
        while True:
            num, cor = spin_wheel()
            if cor != aposta_cor:
                numero_final, cor_final = num, cor
                break
    
    return cor_final == aposta_cor

def apostar_numero(deve_ganhar):
    """
    O jogador aposta em um número específico.
    O resultado é manipulado pela variável 'deve_ganhar'.
    """
    while True:
        try:
            aposta_numero = int(input("Qual número você escolhe (0-36)? "))
            if 0 <= aposta_numero <= 36:
                break
            else:
                print("Número inválido. Deve ser entre 0 e 36.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Lógica de manipulação do resultado
    if deve_ganhar:
        # Força uma vitória, o resultado é o número apostado
        numero_final = aposta_numero
        cor_final = ROULETTE_POCKETS[numero_final]
        print("\nA roleta está girando...")
        time.sleep(1.5)
        print(f"Resultado manipulado! A bola caiu no... {numero_final} ({cor_final.upper()})!")
    else:
        # Força uma derrota, garantindo que o número sorteado seja diferente
        while True:
            num, cor = spin_wheel()
            if num != aposta_numero:
                numero_final, cor_final = num, cor
                break
                
    return numero_final == aposta_numero