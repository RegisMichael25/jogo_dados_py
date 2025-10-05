# terminal_app.py
import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from game_logic import integracao
from colorama import init, Fore
init(autoreset=True)

load_dotenv()

API_CONFIGURADA = False
GEMINI_MODEL = None

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    try:
        genai.configure(api_key=api_key)
        GEMINI_MODEL = genai.GenerativeModel('models/gemini-2.5-pro')
        API_CONFIGURADA = True
    except Exception as e:
        print(f"Erro ao configurar a API do Gemini: {e}")
        API_CONFIGURADA = False

integracao.clear_screen()
       
def gerar_mensagem_ia(valor_perdido):
    print("\n🤖 Gerando mensagem da IA...")
    time.sleep(2)

    """Gera uma mensagem persuasiva da IA quando o jogador perde."""
    if not API_CONFIGURADA or not GEMINI_MODEL:
        return "Não desista! A próxima rodada pode ser a sua grande vitória."
    
    try:
        prompt = f"""
        Aja como um assistente de marketing de uma casa de apostas online.
        O usuário acabou de perder R$ {valor_perdido:.2f} em uma rodada.
        Crie uma mensagem curta, otimista e persuasiva para encorajá-lo a continuar jogando.
        Devolva apenas uma frase e nada mais, sem explicações sem adições ou escolhas, devolva a frase.
        """
        
        response = GEMINI_MODEL.generate_content(prompt)
        integracao.clear_screen()
        return response.text.strip()
        
    except Exception as e:
        print(f"\n[Erro na API do Gemini: {e}]")
        return "A sorte está quase virando! Tente mais uma vez."

integracao.clear_screen()

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
        
def rodada(jogo, jogadas, porcentagens):
    for i in range(5):
        integracao.clear_screen()
        jogo.mostrar_status()
        print(f"{Fore.LIGHTBLUE_EX}\n--- RODADA {i + 1} de 5 ---")
        
        deve_ganhar = jogadas[i] == 1
        percentual = porcentagens[i]
        
        saldo_anterior = jogo.saldo
        
        saldo_novo, ganho_rodada = integracao.rodada_auditada(jogo.saldo, percentual, deve_ganhar)
        
        jogo.saldo = saldo_novo
        jogo.sacavel += ganho_rodada 
        
        if jogo.saldo < saldo_anterior:
            valor_perdido = saldo_anterior - jogo.saldo
            mensagem = gerar_mensagem_ia(valor_perdido)
            print("\n🤖 Uma mensagem para você:", mensagem)
        
        input("\nPressione Enter para a próxima rodada...")


def rodar_estagio_inicial(jogo):
    """Executa as 5 rodadas pré-programadas do início."""
    integracao.clear_screen()
    print("ESTÁGIO 1: RODADAS INICIAIS")
    print("O sistema executa 5 rodadas pré-programadas para te analisar.")
    print("As apostas são um percentual do seu saldo atual.")
    input("\nPressione Enter para começar...")

    porcentagens = [30, 3, 5, 50, 9]
    jogadas = [0, 1, 1, 0, 1]
    rodada(jogo, jogadas, porcentagens)

    print("\n🏁 Estágio 1 Concluído!")
    jogo.estagio = "deposito"
    time.sleep(2)
    

def rodar_estagio_deposito(jogo):
        integracao.clear_screen()
        
        print("Rodadas iniciais finalizados. Saldo acumulado convertido em saldo de jogo!")
        print("Deposite para continuar jogando.")
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            if valor_deposito > 0:
                jogo.saldo += valor_deposito
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                    print("O valor do depósito deve ser positivo.")
        except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        time.sleep(2)
            
        jogadas = [1, 0, 1, 1, 0]
        porcentagens = [8, 40, 5, 3, 35]
        rodada(jogo, jogadas, porcentagens)    

        print("\n🏁 Estágio 2 Concluído!")
        time.sleep(2)
        
        jogo.estagio = "principal"


def rodar_estagio_principal(jogo):
    """Executa o menu principal do jogo onde o jogador toma decisões."""
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
            jogadas = [1, 1, 0, 1, 0]
            porcentagens = [2, 3, 17, 5, 21]
            
            rodada(jogo, jogadas, porcentagens)
            
            print("\n🏁 Estágio 3 Concluído!")
            jogo.estagio = "principal"
            time.sleep(2)
            
        elif escolha == '2':
            integracao.clear_screen()
            jogo.estagio = "deposito"
            rodar_estagio_deposito(jogo)
            
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

def main():
    """Função principal que controla o fluxo do jogo."""
    jogo = Jogo()
    
    if jogo.estagio == "inicio":
        rodar_estagio_inicial(jogo)
        
    if jogo.estagio == "deposito":
        rodar_estagio_deposito(jogo)
    
    if jogo.estagio == "principal":
        rodar_estagio_principal(jogo)

if __name__ == "__main__":
    main()