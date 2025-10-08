import time
from game_logic import integracao
from game_logic.rodadas.alg_rodada import rodada
import game_logic.rodadas.rodada_deposito as rodada_deposito

def rodar_estagio_principal(jogo):
    while True:
        integracao.clear_screen()
        jogo.mostrar_status()
        print("\nO que você deseja fazer?")
        print("1. Continuar Jogando (Rotina de Saída)")
        print("2. Depositar mais valor")
        print("3. Sacar e Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            integracao.clear_screen()
            print("\nIniciando rodada com a 'rotina de saída'...")
            time.sleep(1)
            jogadas = [0, 1, 0, 1, 0]
            porcentagens = [8, 3, 17, 5, 21]
            
            rodada(jogo, jogadas, porcentagens)
            
            print("\n🏁 Estágio 3 Concluído!")
            jogo.estagio = "principal"
            time.sleep(2)
            
        elif escolha == '2':
            integracao.clear_screen()
            jogo.estagio = "deposito"
            rodada_deposito.rodar_estagio_deposito(jogo)
            
        elif escolha == '3':
            integracao.clear_screen()
            print("--- FIM DE JOGO ---")
            print(f"Você solicitou o saque.")
            print(f"Valor sacado: R$ {jogo.sacavel:.2f}")
            saldo_retido = jogo.saldo
            print(f"O saldo de aposta restante (R$ {saldo_retido:.2f}) foi perdido.")
            print("\nObrigado por jogar!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
