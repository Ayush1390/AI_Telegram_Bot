import sys
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, executor, types
import os
import logging
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

openai.api_key=OPENAI_API_KEY

live_link='https://airecipegenerator-ssm3ivajhbr8dakzjlkdk9.streamlit.app/'
github='https://github.com/Ayush1390'

logging.basicConfig(level=logging.INFO)

class Reference:
    def __init__(self) -> None:
        self.response=''

refrence = Reference()
model_name='gpt-3.5-turbo'

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot=bot)

@dispatcher.message_handler(commands=['start'])
async def welcome(message:types.Message):
    await message.reply('Hi\nThis is a telebot\nCreated by anonymous\nHow can i assist you?')


@dispatcher.message_handler(commands=['recepie', 'food'])
async def command_recipie_handler(message:types.Message):
    """
    This handler recives message with `\food` or `\recepie` commands
    """
    await message.reply(f"Follow the link to find out innovative recipies that can be made form ypur available pantry.\n{live_link}")    

@dispatcher.message_handler(commands=['projects', 'github'])
async def command_start_handler(message:types.Message):
    """
    This handler recives message with `\github` or `\projects` commands
    """
    await message.reply(f"Hi\nThis is Ayush\nThis is my github link\n{github}")

@dispatcher.message_handler(commands=['help'])
async def helper(message:types.Message):
    help_command="""
    Hi There, I'm Telegram anonymous bot created by Bappy! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    /food or /recepie - to direct to recepie recommander
    /github or /projects - to direct to github account
    I hope this helps. :)
    """
    await message.reply(help_command)

@dispatcher.message_handler(commands=['clear'])
async def clear(message:types.Message):
    clear_past()
    await message.reply('I have cleared the prervious conversations')


@dispatcher.message_handler()
async def gpt(message:types.Message):
    response = openai.ChatCompletion.create(
        model_name=model_name,
        message=[
            {'role':'assistant', 'content':refrence.response},
            {'role':'user', 'content':message.text}
        ]
    )
    refrence.response = response['choices'][0]['message']['content']
    await bot.send_message(chat_id=message.chat.id, text=refrence.response)

def clear_past():
    refrence.response=''


if __name__ == "__main__":
    executor.start_polling(dispatcher,skip_updates=True)