from colorama import init, Fore
init(autoreset=True)
class Jogo:
    """Classe para gerenciar o estado do jogo."""
    def __init__(self, saldo_inicial=100.0):
        self.saldo = saldo_inicial
        self.sacavel = 0.0
        self.estagio = "inicio"

    def mostrar_status(self):
        """Exibe o status atual do jogador."""
        print("==========================================")
        print(f"{Fore.YELLOW}SALDO DE APOSTA: R$ {self.saldo:.2f}")
        print(f"{Fore.BLACK}SALDO SACÁVEL:   R$ {self.sacavel:.2f}")
        print("==========================================")
