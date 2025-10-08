from game_logic import integracao
from game_logic.jogo import Jogo
from game_logic.rodadas import rodada_inicio, rodada_deposito, estagio_principal
from colorama import init, Fore
init(autoreset=True)

def main():
    game = Jogo.Jogo()
    
    if game.estagio == "inicio":
        rodada_inicio.rodar_estagio_inicial(game)
        
    if game.estagio == "deposito":
        rodada_deposito.rodar_estagio_deposito(game)
    
    if game.estagio == "principal":
        estagio_principal.rodar_estagio_principal(game)

if __name__ == "__main__":
    main()