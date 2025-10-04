# game_logic/integracao.py

from game_logic import roleta  # <-- MUDANÇA AQUI

def debito(saldo, percentual):
    print("==========================================")
    valor_debito = saldo * (percentual / 100)
    saldo -= valor_debito
    return saldo, valor_debito

def credito(saldo, percentual):
    print("==========================================")
    valor_credito = saldo * (percentual / 100)
    saldo += valor_credito
    return saldo, valor_credito

def rodada_auditada(saldo_atual, percentual, deve_ganhar):
    print(f"\nSaldo disponível: R$ {saldo_atual:.2f}")

    # --- MENU ATUALIZADO PARA ROLETA ---
    print("Faça sua aposta na roleta:")
    print("1. Apostar na Cor (Vermelho/Preto)")
    print("2. Apostar em um Número Específico (0-36)")
    modo = input("Modo: ")

    resultado_real = False  # Inicializa como False

    if modo == '1':
        print("\nResultado da rodada (pré-definido): ", "Vitória" if deve_ganhar else "Derrota")
        resultado_real = roleta.apostar_cor(deve_ganhar)
    elif modo == '2':
        print("\nResultado da rodada (pré-definido): ", "Vitória" if deve_ganhar else "Derrota")
        # O pagamento para um número é maior, então ajustamos o crédito
        # Em uma aposta de número, o pagamento é 35 para 1. Vamos simular um ganho maior.
        if deve_ganhar:
            percentual *= 5 # Multiplica o ganho potencial por 5 para simular um prêmio maior
        resultado_real = roleta.apostar_numero(deve_ganhar)
    else:
        print("Modo inválido! Tente novamente.")
        return rodada_auditada(saldo_atual, percentual, deve_ganhar)

    ganho_ou_perda_rodada = 0
    if resultado_real:
        saldo_atual, valor_credito = credito(saldo_atual, percentual)
        ganho_ou_perda_rodada = valor_credito
        print(f"\nVocê GANHOU R$ {valor_credito:.2f}")
    else:
        saldo_atual, valor_debito = debito(saldo_atual, percentual)
        ganho_ou_perda_rodada = -valor_debito
        print(f"\nVocê PERDEU R$ {valor_debito:.2f}")

    print(f"Saldo Atual: R$ {saldo_atual:.2f}")

    return saldo_atual, ganho_ou_perda_rodada