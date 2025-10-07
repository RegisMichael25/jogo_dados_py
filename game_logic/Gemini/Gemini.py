import os
import time
from dotenv import load_dotenv
from game_logic import integracao
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

