from telegram import Bot

bot = Bot(token="8117917745:AAEBd2XdzBoTfZyLC_FG0NjnER6joVtto60")

updates = bot.get_updates()
for update in updates:
    print(update.message.chat.id)
