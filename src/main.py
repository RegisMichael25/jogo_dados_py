"""
def menu():
    print("Bem-vindo ao cassino!")
    print("Escolha um jogo:")
    print("1. Sic Bo")
    print("2. Sair")
    escolha = input("Digite o número do jogo que deseja jogar: ")
    if escolha not in ['1', '2']:
        print("Escolha inválida. Tente novamente.")
        return menu()
    return escolha

escolha = menu()
print(f"Você escolheu a opção {escolha}.")
if escolha == '1':
    import sicbo.sicbo as sicbo
else:
    print("Obrigado por jogar! Até a próxima.")
    exit()
"""

import game_logic.logic as lg