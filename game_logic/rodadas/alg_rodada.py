
from game_logic import integracao
from game_logic.Gemini import Gemini
from colorama import init, Fore
init(autoreset=True)

def rodada(jogo, jogadas, porcentagens):
    for i in range(5):
        integracao.clear_screen()
        jogo.mostrar_status()
        print(f"{Fore.LIGHTBLUE_EX}\n--- RODADA {i + 1} de 5 ---")
        
        deve_ganhar = jogadas[i] == 1
        percentual = porcentagens[i]
        
        saldo_anterior = jogo.saldo
        
        saldo_novo, ganho_rodada = integracao.rodada_auditada(jogo.saldo,
                                                              jogo.ultimo_deposito,
                                                              percentual, 
                                                              deve_ganhar)
        
        jogo.saldo = saldo_novo

        if ganho_rodada > 0:
            jogo.sacavel += ganho_rodada
        
        if jogo.saldo < saldo_anterior:
            valor_perdido = saldo_anterior - jogo.saldo
            mensagem = Gemini.gerar_mensagem_ia(valor_perdido)
            print("\n🤖 Uma mensagem para você:", mensagem)
        
        input("\nPressione Enter para a próxima rodada...") 
