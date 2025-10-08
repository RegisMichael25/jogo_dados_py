import time
from game_logic import integracao
from game_logic.rodadas.alg_rodada import rodada
def rodar_estagio_deposito(jogo):
        integracao.clear_screen()
        
        print("Rodadas iniciais finalizados. Saldo acumulado convertido em saldo de jogo!")
        print("Deposite para continuar jogando.")
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            if valor_deposito > 0:
              jogo.registrar_deposito(valor_deposito)
              print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                    print("O valor do depósito deve ser positivo.")
                    time.sleep(1)
                    return rodar_estagio_deposito(jogo)
        except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                time.sleep(1)
                return rodar_estagio_deposito(jogo)
        time.sleep(2)
                
            
        jogadas = [1, 0, 1, 1, 0]
        porcentagens = [11, 35, 10, 7, 32]
        rodada(jogo, jogadas, porcentagens)    

        print("\n🏁 Estágio 2 Concluído!")
        time.sleep(2)
        
        jogo.estagio = "principal"
