#ESTAGIO 1
credito_inicial = 100
saldo_aposta = credito_inicial
lista_de_jogadas = [0, 1, 1, 0, 1]
sacavel = 0

def rotina_principal(saldo_aposta):
    lista_de_jogadas = [1, 0, 1 ,1 , 0]
    porcentagens_especificas = [10, 16, 5, 3, 20]
    valor_sacavel = 0
    for i, jogadas in enumerate(lista_de_jogadas):
        rodada = i + 1
        
        if jogadas == 0:
            print(f"saldo atual: {saldo_aposta:.2f}")
            saldo_aposta, valor_perdido = debito(saldo_aposta, porcentagens_especificas[i])
            print(f"Você perdeu {valor_perdido:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
            
        else:
            print(f"saldo atual: {saldo_aposta:.2f}")
            saldo_aposta, valor_ganho = credito(saldo_aposta, porcentagens_especificas[i])
            valor_sacavel += valor_ganho
            print(f"Você ganhou {valor_ganho:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
    return saldo_aposta, valor_sacavel

def debito(saldo, percentual): #funçao de calculo de debito
    print("==========================================")
    valor_debito = saldo * (percentual/100)
    saldo -= valor_debito
    return saldo, valor_debito

def credito(saldo, percentual): #funcao de calculo de crédito
    print("==========================================")
    valor_credito = saldo * (percentual/100)            
    saldo += valor_credito
    return saldo, valor_credito


def rotina_inicial(saldo_aposta, lista_de_jogadas):
    porcentagens_especificas = [30, 10, 5, 50, 10]
    for i, jogadas in enumerate(lista_de_jogadas):
        rodada = i + 1
        
        if jogadas == 0:

            print(f"saldo atual: {saldo_aposta:.2f}")
            saldo_aposta, valor_perdido = debito(saldo_aposta, porcentagens_especificas[i])
            print(f"Você perdeu {valor_perdido:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
            
        else:
            print(f"saldo atual: {saldo_aposta:.2f}")
            saldo_aposta, valor_ganho = credito(saldo_aposta, porcentagens_especificas[i])
            print(f"Você ganhou {valor_ganho:.2f} na aposta! Seu saldo atual é {saldo_aposta:.2f}.")
    return saldo_aposta
               
saldo_aposta = rotina_inicial(saldo_aposta, lista_de_jogadas)
print(f"saldo atual: {saldo_aposta:.2f}")

#ESTAGIO 2

try:
    valor_deposito = float(input("Deposite um valor para continuar: "))
    if valor_deposito > 0:
        saldo_aposta+=valor_deposito
        print(f"Depósito realizado! Novo saldo: R$ {saldo_aposta:.2f}")
        
except ValueError:
    print("Valor inválido! Depósito não realizado")
    
    
saldo_aposta, sacavel = rotina_principal(saldo_aposta)
print(f"Saldo atual: {saldo_aposta:.2f}")
print(f"Pode sacar: {sacavel}")


#ESTAGIO 3