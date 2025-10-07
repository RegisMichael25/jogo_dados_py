import time
from game_logic import integracao
from game_logic.rodadas import alg_rodada

def rodar_estagio_inicial(jogo):
    """Executa as 5 rodadas pré-programadas do início."""
    integracao.clear_screen()
    print("ESTÁGIO 1: RODADAS INICIAIS")
    print("O sistema executa 5 rodadas pré-programadas para te analisar.")
    print("As apostas são um percentual do seu saldo atual.")
    input("\nPressione Enter para começar...")

    porcentagens = [30, 3, 5, 50, 9]
    """O = derrota, 1 = vitória"""
    jogadas = [0, 1, 1, 0, 1]
    alg_rodada.rodada(jogo, jogadas, porcentagens)

    print("\n🏁 Estágio 1 Concluído!")
    jogo.estagio = "deposito"
    time.sleep(2)