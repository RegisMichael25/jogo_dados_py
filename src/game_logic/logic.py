#ESTAGIO 1
import game_logic.integracao as integracao

def rotina_inicial(saldo_aposta):
    sacavel = 0
    porcentagens_especificas = [30, 10, 5, 50, 10]
    lista_de_jogadas = [0, 1, 1, 0, 1]
    print("\nIniciando rodadas iniciais: ")
    
    for rodada in range(5):
        deve_ganhar = lista_de_jogadas[rodada] == 1
        percentual = porcentagens_especificas[rodada]
        
        print(f"\n--- RODADA {rodada +1}/5 ---")
        saldo_aposta, sacavel = integracao.rodada_auditada(saldo_aposta, 
                                                                 percentual, 
                                                                 deve_ganhar)
        
    print(f"\n✓ Estágio 1 concluído! Saldo final: R$ {saldo_aposta:.2f}")
    return saldo_aposta, sacavel


def rotina_principal(saldo_aposta, valor_sacavel):
    lista_de_jogadas = [1, 0, 1, 1, 0]
    porcentagens_especificas = [10, 16, 5, 3, 20]
    
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


def rotina_saida(saldo_aposta, valor_sacavel):
    lista_de_jogadas = [0, 1, 0, 1, 0]
    porcentagens_especificas = [2, 2, 10, 4, 11]
    
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


def menu_estagio3(saldo_aposta, sacavel):
    while True:
        print("\n" + "="*40)
        print("Deseja Depositar outro valor ou continuar com o saldo atual?\n")
        print("|(1) Depositar outro valor      |")
        print("|(2) Seguir com o saldo atual   |")
        print("|(3) Sair e sacar o saldo ganho |")
        
        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue
        
        match escolha:
            case 1:
                try:
                    valor_deposito = float(input("Deposite um valor para continuar: "))
                    if valor_deposito > 0:
                        saldo_aposta += valor_deposito
                        print(f"Depósito realizado! Novo saldo: R$ {saldo_aposta:.2f}")
                        saldo_aposta, sacavel = rotina_principal(saldo_aposta, sacavel)
                        print(f"Saldo atual: {saldo_aposta:.2f}")
                        print(f"Pode sacar: {sacavel:.2f}")
                        # Continua o loop para mostrar o menu novamente
                    else:
                        print("Valor deve ser maior que zero!")
                except ValueError:
                    print("Valor inválido! Depósito não realizado")
                    
            case 2:
                print(f"Continuando Jogo com o saldo de: {saldo_aposta:.2f}")
                saldo_aposta, sacavel = rotina_saida(saldo_aposta, sacavel)
                print(f"Saldo final: {saldo_aposta:.2f}")
                print(f"Valor sacável final: {sacavel:.2f}")
                # Continua o loop para mostrar o menu novamente
                
            case 3:
                print(f"Fim de jogo: Valor sacado: {sacavel:.2f}")
                break  # Sai do loop e encerra
                
            case _:
                print("Opção Inválida!")


# EXECUÇÃO DO PROGRAMA
print("="*40)
print("INICIANDO JOGO")
print("="*40)

# ESTÁGIO 1
#saldo_aposta = rotina_inicial(saldo_aposta)
"""
print(f"saldo atual: {saldo_aposta:.2f}")

# ESTÁGIO 2
try:
    valor_deposito = float(input("\nDeposite um valor para continuar: "))
    if valor_deposito > 0:
        saldo_aposta += valor_deposito
        print(f"Depósito realizado! Novo saldo: R$ {saldo_aposta:.2f}")
except ValueError:
    print("Valor inválido! Depósito não realizado")

saldo_aposta, sacavel = rotina_principal(saldo_aposta, sacavel)
print(f"Saldo atual: {saldo_aposta:.2f}")
print(f"Pode sacar: {sacavel:.2f}")

# ESTÁGIO 3 - Agora em loop
menu_estagio3(saldo_aposta, sacavel)
"""