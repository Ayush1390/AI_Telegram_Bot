import logging
from aiogram import Dispatcher, Bot, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message:types.Message):
    """
    This handler recives message with `\start` or `\help` commands
    """
    await message.reply("Hi\nI am an echo bot\nPowerd by aiogram")
  
@dp.message_handler()
async def echo_handler(message:types.Message):
    """
    This handler returns the recevied message
    """
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

