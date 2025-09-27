#ESTAGIO 1
credito_inicial = 100
valor_deposito = 0
saldo_aposta = credito_inicial

lista_de_jogadas = [0, 1, 1, 0, 1]

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

for jogadas in lista_de_jogadas:
        if jogadas == 0:
            print(f"saldo antes da aposta: {saldo_aposta:.2f}")
            saldo_aposta, valor_perdido = debito(saldo_aposta, 30           )
            print(f"Você perdeu {valor_perdido:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
            print(f"saldo depois da aposta: {saldo_aposta:.2f}")
        else:
            print(f"saldo antes da aposta: {saldo_aposta:.2f}")
            saldo_aposta, valor_ganho = credito(saldo_aposta, 10)
            print(f"Você ganhou {valor_ganho:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
            print(f"saldo depois da aposta: {saldo_aposta:.2f}")

#ESTAGIO 2
#valor_deposito = input("Digite o valor da aposta: ")
#deposito = bool(valor_deposito)
#if deposito is True:
#    saldo_aposta += valor_deposito
#    fichas = 5
#else:
#    fichas = 0


#ESTAGIO 3