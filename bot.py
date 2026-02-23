import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = 'YOUR_API_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

# Commands
@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Use /help to see available commands.")

@dispatcher.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Available commands: /start, /help, /pay")

@dispatcher.message_handler(commands=['pay'])
async def process_payment(message: types.Message):
    # Implementation for payment processing
    await message.reply("Payment processing not implemented yet")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)