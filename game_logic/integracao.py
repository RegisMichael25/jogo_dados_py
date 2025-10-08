# game_logic/integracao.py
import os
from colorama import init, Fore
init(autoreset=True)
from game_logic import roleta  

def clear_screen():
    """Limpa a tela do terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def debito(saldo, percentual):
    print("==========================================")
    valor_debito = saldo * (percentual / 100)
    saldo -= valor_debito
    return saldo, valor_debito

def credito(saldo, percentual):
    print("==========================================")
    valor_credito = saldo * (percentual / 100)
    saldo +=valor_credito
    return saldo, valor_credito

def rodada_auditada(saldo_atual, percentual, deve_ganhar):
    print(f"\n{Fore.GREEN}Saldo disponível: R$ {saldo_atual:.2f}")

    print("Faça sua aposta na roleta:")
    print(f"1. Apostar na Cor ({Fore.RED}Vermelho{Fore.WHITE}/{Fore.BLACK}Preto{Fore.WHITE})")
    print("2. Apostar em um Número Específico (0-36)")
    modo = input("Modo: ")

    resultado_real = False 

    if modo == '1':
        clear_screen()
        print("\nResultado da rodada (pré-definido): ", "Vitória" if deve_ganhar else "Derrota")
        resultado_real = roleta.apostar_cor(deve_ganhar)
    elif modo == '2':
        clear_screen()
        print("\nResultado da rodada (pré-definido): ", "Vitória" if deve_ganhar else "Derrota")
        if deve_ganhar:
            percentual *= 1.5
        resultado_real = roleta.apostar_numero(deve_ganhar)
    else:
        print("Modo inválido! Tente novamente.")
        return rodada_auditada(saldo_atual, percentual, deve_ganhar)

    ganho_ou_perda_rodada = 0
    if resultado_real:
        saldo_atual, valor_credito = credito(saldo_atual, percentual)
        ganho_ou_perda_rodada = valor_credito
        print(f"\n{Fore.GREEN}Você GANHOU R$ {valor_credito:.2f}")
    else:
        saldo_atual, valor_debito = debito(saldo_atual, percentual)
        print(f"\n{Fore.RED}Você PERDEU R$ {valor_debito:.2f}")

    print(f"{Fore.LIGHTBLACK_EX}Saldo Atual: R$ {saldo_atual:.2f}")

    return saldo_atual, ganho_ou_perda_rodada