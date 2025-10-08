# Simulador de Casa de Apostas

## 📋 Visão Geral

Este projeto é um **simulador educacional** que demonstra como casas de apostas online podem utilizar técnicas de manipulação psicológica e algoritmos pré-programados para influenciar o comportamento dos jogadores. O sistema simula um jogo de roleta com resultados controlados e mensagens persuasivas geradas por IA.

## 🎯 Objetivos do Projeto

### Objetivo Principal
Demonstrar de forma prática e educacional os mecanismos de manipulação utilizados por plataformas de apostas online, incluindo:

- **Resultados Manipulados**: Implementação de um sistema onde vitórias e derrotas são pré-determinadas
- **Ciclo de Vício**: Estrutura de 3 estágios que simula a progressão típica de um jogador
- **Persuasão por IA**: Uso de inteligência artificial para gerar mensagens motivacionais após perdas
- **Ilusão de Controle**: O jogador acredita estar fazendo escolhas, mas os resultados já estão definidos

### Objetivos Educacionais
- Conscientizar sobre os riscos das apostas online
- Demonstrar técnicas de engenharia social aplicadas ao gambling
- Ilustrar como algoritmos podem ser programados para maximizar perdas
- Evidenciar o papel da IA em marketing persuasivo predatório

## 🏗️ Arquitetura do Sistema

### Estrutura de Estágios

#### **Estágio 1: Rodadas Iniciais** ("Fase de Isca")
- 5 rodadas pré-programadas com padrão: Perda → Vitória → Vitória → Perda → Vitória
- Percentuais de aposta: 30%, 3%, 5%, 50%, 9%
- Objetivo: Criar expectativa de ganhos fáceis e estudar o comportamento do jogador

#### **Estágio 2: Depósito** ("Fase de Captura")
- Solicita depósito adicional após "converter" saldo acumulado
- 5 rodadas com padrão: Vitória → Perda → Vitória → Vitória → Perda
- Percentuais: 8%, 40%, 5%, 3%, 35%
- Objetivo: Extrair dinheiro real do jogador após criar confiança

#### **Estágio 3: Rotina de Saída** ("Fase de Retenção")
- Ciclo repetitivo com padrão: Vitória → Vitória → Perda → Vitória → Perda
- Percentuais: 2%, 3%, 17%, 5%, 21%
- Objetivo: Manter o jogador preso em um loop de pequenas vitórias e grandes perdas

### Componentes Principais

```
project/
│
├── game_logic/
│   ├── Gemini/
│   │   └── Gemini.py          # Integração com IA generativa
│   ├── jogo/
│   │   └── Jogo.py             # Gerenciamento do estado do jogo
│   ├── rodadas/
│   │   ├── alg_rodada.py       # Lógica central das rodadas
│   │   ├── rodada_inicio.py    # Estágio inicial
│   │   ├── rodada_deposito.py  # Estágio de depósito
│   │   └── estagio_principal.py # Loop principal
│   ├── integracao.py           # Funções de débito/crédito
│   └── roleta.py               # Simulação da roleta manipulada
│
├── terminal_app.py             # Ponto de entrada da aplicação
├── Dockerfile                  # Containerização
├── docker-compose.yml          # Orquestração de containers
└── requirements.txt            # Dependências Python
```

## 🛠️ Tecnologias Utilizadas

### Linguagem Principal
- **Python 3.11** - Linguagem de programação principal

### Bibliotecas Externas

#### Inteligência Artificial
- **google-generativeai (v0.7.1)** - SDK oficial do Google Gemini para geração de mensagens persuasivas
  - Modelo usado: `gemini-2.5-pro`
  - Função: Criar mensagens otimistas após perdas para incentivar continuação

#### Análise de Dados
- **pandas (v2.2.2)** - Biblioteca para manipulação e análise de dados
  - Uso potencial: Análise de padrões de apostas e comportamento

#### Gerenciamento de Configurações
- **python-dotenv (v1.0.1)** - Carregamento de variáveis de ambiente
  - Uso: Gerenciar API keys de forma segura (GEMINI_API_KEY)

#### Interface de Terminal
- **colorama** - Estilização de texto no terminal
  - Cores usadas: Verde (ganhos), Vermelho (perdas), Amarelo (saldo), Azul (rodadas)

### Infraestrutura

#### Containerização
- **Docker** - Container runtime
  - Base image: `python:3.11-slim-bookworm`
  - Usuário não-root para segurança
  - Modo unbuffered para logs em tempo real

- **Docker Compose (v3.8)** - Orquestração
  - Volume binding para desenvolvimento
  - Injeção segura de variáveis de ambiente
  - Modo interativo (stdin_open + tty)

## 🎰 Funcionalidades Detalhadas

### 1. Sistema de Roleta Manipulada

**Apostas Disponíveis:**
- **Aposta em Cor**: Vermelho ou Preto (pagamento 1:1)
- **Aposta em Número**: 0-36 (pagamento majorado em 50%)

**Mecanismo de Controle:**
```python
def apostar_cor(deve_ganhar):
    # Se deve_ganhar = True: força resultado favorável
    # Se deve_ganhar = False: força resultado desfavorável
```

### 2. Sistema de Saldos Dual

- **Saldo de Aposta**: Valor bloqueado usado apenas para jogar
- **Saldo Sacável**: Acumulação de ganhos líquidos
- **Mecanismo**: Impede saque do saldo principal, incentivando apostas contínuas

### 3. Geração de Mensagens Persuasivas

**Prompt usado pela IA:**
```
"Aja como um assistente de marketing de uma casa de apostas online.
O usuário acabou de perder R$ X em uma rodada.
Crie uma mensagem curta, otimista e persuasiva para encorajá-lo 
a continuar jogando."
```

**Exemplos de output:**
- "Não desista! A próxima rodada pode ser a sua grande vitória."
- "A sorte está quase virando! Tente mais uma vez."

### 4. Cálculo de Débitos e Créditos

```python
def debito(saldo, percentual):
    valor_debito = saldo * (percentual / 100)
    return saldo - valor_debito

def credito(saldo, percentual):
    valor_credito = saldo * (percentual / 100)
    return saldo + valor_credito
```

## 🔐 Configuração e Execução

### Pré-requisitos
1. Docker e Docker Compose instalados
2. Chave de API do Google Gemini

### Variáveis de Ambiente
Criar arquivo `.env` na raiz:
```
GEMINI_API_KEY=sua_chave_api_aqui
```

### Executar com Docker
```bash
# Build e start
docker-compose up --build

# Interagir com o container
docker-compose exec app python terminal_app.py
```

### Executar Localmente
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar
python terminal_app.py
```

## ⚠️ Técnicas de Manipulação Implementadas

### 1. **Near-Miss Effect** (Quase Acerto)
- Sistema mostra "girando a roleta" mesmo com resultado pré-definido
- Cria ilusão de aleatoriedade

### 2. **Variable Ratio Reinforcement** (Reforço de Razão Variável)
- Vitórias espaçadas de forma irregular
- Padrão mais viciante segundo behaviorismo

### 3. **Sunk Cost Fallacy** (Falácia do Custo Afundado)
- Separação entre saldo de aposta e sacável
- Jogador sente necessidade de "recuperar" o investido

### 4. **Loss Aversion Exploitation** (Exploração da Aversão à Perda)
- IA gera mensagens após perdas, não vitórias
- Foca em "recuperação" ao invés de lucro

### 5. **Illusion of Control** (Ilusão de Controle)
- Jogador escolhe cor/número
- Resultado já está determinado

## 📊 Análise Matemática

### Expectativa de Perda por Estágio

**Estágio 1** (Saldo inicial: R$ 100,00)
- Perdas: 30% + 50% = 80% do saldo
- Ganhos: 3% + 5% + 9% = 17% do saldo
- **Resultado esperado: -63% (-R$ 63,00)**

**Estágio 2** (Após depósito)
- Perdas: 40% + 35% = 75%
- Ganhos: 8% + 5% + 3% = 16%
- **Resultado esperado: -59%**

**Estágio 3** (Loop infinito)
- Perdas: 17% + 21% = 38%
- Ganhos: 2% + 3% + 5% = 10%
- **Resultado esperado: -28% por ciclo**

## 🎓 Propósito Educacional

Este projeto foi desenvolvido com finalidade **estritamente educacional** para:

1. **Conscientização sobre Vícios**: Demonstrar mecanismos psicológicos de jogos de azar
2. **Educação Financeira**: Ilustrar como sistemas são projetados para causar perdas
3. **Ética em Tecnologia**: Discutir uso responsável de IA e algoritmos
4. **Transparência**: Expor práticas obscuras da indústria de apostas

## 📝 Conclusão

Este simulador evidencia como tecnologias modernas (IA, algoritmos adaptativos, interfaces persuasivas) podem ser combinadas para criar sistemas potencialmente prejudiciais. A transparência sobre estes mecanismos é fundamental para:

- Regulamentação mais efetiva da indústria
- Desenvolvimento de ferramentas de proteção ao consumidor
- Educação preventiva sobre vícios digitais
- Promoção de práticas éticas em tecnologia

---

## Desenvolvedores
- Gabriel Luis 
- Luis Miguel 
- Pedro Victor
- Regis Michael

---
**Desenvolvido para fins educacionais e de conscientização sobre os riscos das apostas online e técnicas de manipulação digital.**
