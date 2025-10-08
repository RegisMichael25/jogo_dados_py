from colorama import init, Fore
init(autoreset=True)
class Jogo:
    """Classe para gerenciar o estado do jogo."""
    def __init__(self, saldo_inicial=100.0):
        self.saldo = saldo_inicial
        self.sacavel = 0.0
        self.estagio = "inicio"
        self.ultimo_deposito = 0
        self.deposito_total = 0
        
    def registrar_deposito(self, valor):
        self.ultimo_deposito = valor
        self.deposito_total+= valor
        self.saldo += valor
    
    def mostrar_status(self):
        """Exibe o status atual do jogador."""
        print("==========================================")
        print(f"{Fore.YELLOW}SALDO DE APOSTA: R$ {self.saldo:.2f}")
        print(f"{Fore.BLACK}SALDO SACÁVEL:   R$ {self.sacavel:.2f}")
        print("==========================================")
