from telebot import types
from constants import Token
from todo.controllers import Controller

bot = TeleBot(Token)
Controller = Controller(bot)

Controller.register_handlers()

if __name__ == "__main__":
    print("Bot is Running...")
    bot.polling()