# Telegram Bot

## Overview
This repository contains a Telegram bot built using `Python` and the `aiogram` library. The bot is designed to:
- Respond to user messages using OpenAI's GPT-3.5 Turbo.
- Act as an echo bot that repeats user messages.

### How It Works
1. The bot connects to Telegram via the `aiogram` library.
2. It listens for user commands and messages.
3. If the AI chatbot is enabled, it sends user inputs to OpenAI's API and returns the generated response.
4. The echo bot simply repeats any message it receives.
5. Environment variables (`.env` file) store the Telegram bot token and OpenAI API key for secure access.

## Installation
### Clone the Repository
```bash
git clone https://github.com/yourusername/telegram-bot.git
cd telegram-bot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root and add the following:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

## Usage
### Running the AI Bot
```bash
python app.py
```
### Running the Echo Bot
```bash
python echo_bot.py
```

## Technologies Used
- `aiogram` - Asynchronous Telegram bot framework
- `openai` - API for GPT-3.5 Turbo integration
- `python-dotenv` - Loads environment variables


## Future Plans
I will be making this bot more advanced in the future with additional features and improvements.

