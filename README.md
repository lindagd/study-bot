# StudyBot

O StudyBot é um bot do telegram que te ajuda nos seus estudos.
O bot foi desenvolvido com o objetivo de aprender a desenvolver chatbots e a integração e uso da Groq API.

## Funcionalidades

 Pomodoro           |  Resumo de tópicos
:-------------------------:|:-------------------------:
 ![Imagem do WhatsApp de 2024-12-15 à(s) 13 34 43_cb0a16e9](https://github.com/user-attachments/assets/fba56530-4cbd-4a60-8831-c9d2112ef75a) | ![Imagem do WhatsApp de 2024-12-15 à(s) 13 22 55_424f000a](https://github.com/user-attachments/assets/70279fc4-e873-47db-84a8-b9c2c0b13d7e)

## Setup

### Obtenha seu Token do telegram

Antes de iniciar, crie o seu bot no telegram e obtenha seu token para enviar requisições para a API do bot.

Utilize o BotFather para criar o seu bot e obter seu token. Siga as instruções no [guia do BotFather](https://core.telegram.org/bots/features#botfather) incluso na [documentação oficial do Telegram Bot API](https://core.telegram.org/bots/api)

### Obtenha sua chave para uso da Groq API seguindo os passos na [documentação oficial](https://console.groq.com/docs/quickstart)

### Clone este repositório:

    git clone https://github.com/lindagd/study-bot.git

### Instale as dependências

    pip install python-telegram-bot --upgrade

### Insira seus Token e Chave no código

1. Nas primeiras linhas do arquivo *main*, após os *imports*, inclua seu token do bot substituindo a string da variável `TOKEN = "seu-token"`
2. No arquivo *summary*, inclua sua chave da API Groq na variável `GROQ_KEY = "YOUR-GROQ-KEY"`

### Rode o projeto

    python3 main.py

Para interromper a execução e parar o bot utilize `ctrl+c`
