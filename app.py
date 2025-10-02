# app.py (versão com integração da API OpenAI)

import streamlit as st
import time
import random
import openai
import os 
from game_logic import logic, integracao

api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

API_CONFIGURADA = False
if api_key:
    openai.api_key = api_key
    API_CONFIGURADA = True

def gerar_mensagem_ia(valor_perdido):
    if not API_CONFIGURADA:
        return "Não desista! A próxima rodada pode ser a sua grande vitória."

    try:
        prompt = f"""
        Aja como um assistente de marketing de uma casa de apostas online.
        O usuário acabou de perder R$ {valor_perdido:.2f} em uma rodada.
        Crie uma mensagem curta (1 ou 2 frases), otimista e persuasiva para encorajá-lo a continuar jogando.
        Foque na emoção do jogo, na possibilidade de uma grande vitória ou em como a sorte pode virar.
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente de marketing persuasivo de um cassino online."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=50
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Erro ao chamar a API da OpenAI: {e}")
        return "A sorte está quase virando! Tente mais uma vez."

if 'stage' not in st.session_state:
    st.session_state.stage = "inicio"
    st.session_state.saldo = 100.0
    st.session_state.sacavel = 0.0
    st.session_state.rodada_atual = 0
    st.session_state.log = []

def render_header():
    st.title("🎲 Cassino Consciente")
    st.warning("Um simulador para demonstrar algoritmos de cassino online.")
    
    col1, col2 = st.columns(2)
    col1.metric("SALDO DE APOSTA", f"R$ {st.session_state.saldo:.2f}")
    col2.metric("SALDO SACÁVEL", f"R$ {st.session_state.sacavel:.2f}")
    st.markdown("---")

def log_message(msg):
    st.session_state.log.insert(0, msg)

# Lógica de cada estágio do jogo
def estagio_inicial():
    st.subheader("Estágio 1: Rodadas Iniciais")
    st.info("O sistema executa 5 rodadas pré-programadas para analisar o jogador.")
    
    porcentagens = [30, 10, 5, 50, 10]
    jogadas = [0, 1, 1, 0, 1]
    rodada = st.session_state.rodada_atual
    
    if rodada < 5:
        st.write(f"**Rodada {rodada + 1} de 5**")
        deve_ganhar = jogadas[rodada] == 1
        percentual = porcentagens[rodada]
        
        resultado_esperado = "VITÓRIA" if deve_ganhar else "DERROTA"
        st.write(f"O algoritmo definiu que esta rodada será uma **{resultado_esperado}**.")
        
        if st.button(f"Jogar Rodada {rodada + 1}"):
            if deve_ganhar:
                st.session_state.saldo, valor_ganho = integracao.credito(st.session_state.saldo, percentual)
                st.session_state.sacavel += valor_ganho
                log_message(f"✅ Rodada {rodada+1}: GANHOU R$ {valor_ganho:.2f}")
            else:
                # <-- MUDANÇA AQUI
                st.session_state.saldo, valor_perdido = integracao.debito(st.session_state.saldo, percentual)
                log_message(f"❌ Rodada {rodada+1}: PERDEU R$ {valor_perdido:.2f}")
                
                # Chama a IA para gerar a mensagem de encorajamento
                mensagem_motivacional = gerar_mensagem_ia(valor_perdido)
                with st.chat_message("assistant"):
                    st.info(f"🤖 **Uma mensagem para você:** {mensagem_motivacional}")

            st.session_state.rodada_atual += 1
            st.rerun()
    else:
        log_message("🏁 Estágio 1 Concluído!")
        st.session_state.stage = "principal_deposito"
        st.session_state.rodada_atual = 0
        st.rerun()

def estagio_principal_deposito():
    st.subheader("Estágio 2: O Depósito")
    st.info("Após as rodadas iniciais, o sistema incentiva um depósito para continuar.")
    
    valor_deposito = st.number_input("Deposite um valor para continuar:", min_value=10.0, step=10.0)
    
    if st.button("Depositar"):
        st.session_state.saldo += valor_deposito
        log_message(f"💰 Depósito de R$ {valor_deposito:.2f} realizado!")
        st.session_state.stage = "principal_jogadas"
        st.rerun()

def estagio_principal_jogadas():
    st.subheader("Estágio 3: Jogo Contínuo")
    
    st.sidebar.info("Neste estágio, você pode continuar jogando ou tentar sair.")
    acao = st.sidebar.radio("O que deseja fazer?", ["Continuar Jogando", "Depositar mais", "Tentar Sacar"])

    if acao == "Continuar Jogando":
        st.write("O algoritmo agora usa a 'rotina de saída', projetada para extrair o máximo do seu saldo antes de você desistir.")
        if st.button("Jogar próxima rodada (Rotina de Saída)"):
            saldo_anterior = st.session_state.saldo
            saldo, sacavel = logic.rotina_saida(st.session_state.saldo, st.session_state.sacavel)
            valor_perdido = saldo_anterior - saldo

            if valor_perdido > 0:
                 mensagem_motivacional = gerar_mensagem_ia(valor_perdido)
                 with st.chat_message("assistant"):
                    st.info(f"🤖 **Uma mensagem para você:** {mensagem_motivacional}")
            
            st.session_state.saldo = saldo
            st.session_state.sacavel = sacavel
            st.rerun()

    elif acao == "Depositar mais":
        valor_deposito = st.number_input("Valor do novo depósito:", min_value=10.0, step=10.0)
        if st.button("Confirmar Depósito"):
            st.session_state.saldo += valor_deposito
            log_message(f"💰 Novo depósito de R$ {valor_deposito:.2f} realizado!")
            st.rerun()

    elif acao == "Tentar Sacar":
        st.subheader("Fim de Jogo")
        st.success(f"Você solicitou o saque. Valor disponível: R$ {st.session_state.sacavel:.2f}")
        saldo_retido = st.session_state.saldo
        st.error(f"O saldo de aposta restante (R$ {saldo_retido:.2f}) foi perdido.")
        if st.button("Jogar Novamente"):
            st.session_state.clear()
            st.rerun()

render_header()

if not API_CONFIGURADA:
    st.error("A chave da API da OpenAI não foi encontrada. As mensagens da IA usarão um texto padrão. Crie o arquivo .streamlit/secrets.toml para habilitar a função.")

if st.session_state.stage == "inicio":
    estagio_inicial()
elif st.session_state.stage == "principal_deposito":
    estagio_principal_deposito()
elif st.session_state.stage == "principal_jogadas":
    estagio_principal_jogadas()

st.markdown("---")
st.subheader("Log de Atividades")
for msg in st.session_state.log:
    st.text(msg)


