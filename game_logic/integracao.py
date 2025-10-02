from game_logic import sicbo
sacavel = 0
def debito(saldo, percentual):
    print("==========================================")
    valor_debito = saldo * (percentual/100)
    saldo -= valor_debito
    return saldo, valor_debito


def credito(saldo, percentual):
    print("==========================================")
    valor_credito = saldo * (percentual/100)            
    saldo += valor_credito
    return saldo, valor_credito

def rodada_auditada(saldo_atual, percentual, deve_ganhar):
    
    print(f"Saldo disponivel: R$ {saldo_atual:.2f}")
    
    print("Escolha o modo: ")
    print("1. Advinhar soma")
    print("2. Adivinhar número específico")
    modo = input("Modo: ")
    
    match modo:
        case '1': 
            print("Resultado da rodada: ", deve_ganhar) #remover
            resultado_real = sicbo.guess_sum(deve_ganhar)
        case '2': 
            print("Resultado da rodada: ", deve_ganhar) #remover
            resultado_real = sicbo.guess_specific(deve_ganhar)
        case _:
            print("Modo inválido! Tente novamente.")
            return rodada_auditada(saldo_atual, percentual, deve_ganhar)
    
    if resultado_real == True:
       saldo_atual, valor_credito = credito(saldo_atual, percentual)
       print(f"Você GANHOU R$ {valor_credito:.2f}")
    else:
        saldo_atual, valor_debito = debito(saldo_atual, percentual)
        print(f"Você PERDEU R$ {valor_debito:.2f}")
    
    print(f"Saldo Atual: R$ {saldo_atual:.2f}")
    
    valor_credito = 0
    valor_debito = 0
    sacavel = valor_credito - valor_debito
    return saldo_atual, sacavel