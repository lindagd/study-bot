# StudyBot

O StudyBot é um bot do telegram que te ajuda nos seus estudos.
O bot foi desenvolvido com o objetivo de aprender a desenvolver chatbots e a integração e uso da Groq API.

## Funcionalidades

- Técnica Pomodoro, com o comando `/pomodoro`
- Resumo de tópicos, com o comando `/resumir` + tópico de escolha

## Setup

### Obtenha seu Token do telegram

Antes de iniciar, crie o seu bot no telegram e obtenha seu token para enviar requisições para a API do bot.

Utilize o BotFather para criar o seu bot e obter seu token. Siga as instruções no [guia do BotFather](https://core.telegram.org/bots/features#botfather) incluso na [documentação oficial do Telegram Bot API](https://core.telegram.org/bots/api)

### Obtenha sua chave para uso da Groq API seguindo os passos na [documentação oficial](https://console.groq.com/docs/quickstart)

### Clone este repositório:

    git clone https://github.com/lindagd/telegram-study-bot

### Instale as dependências

    pip install python-telegram-bot --upgrade

### Insira seus Token e Chave no código

Nas primeiras linhas do arquivo *main*, após os *imports*, inclua seu token do bot substituindo a string da variável `TOKEN = "seu-token"`

No arquivo *summary*, inclua sua chave da API Groq na variável `self.client = "YOUR-GROQ-API-KEY-HERE"`

### Rode o projeto

    python3 main.py

Para interromper a execução e parar o bot utilize `ctrl+c`