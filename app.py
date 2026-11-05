import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')

GROUP_ID = -1004227685910

RULES_TEXT = "📌 Пожалуйста, ознакомьтесь с правилами сообщества перед тем, как писать комментарии.

‼️ПРАВИЛА‼️

В чате запрещено:
1. Спамить, публиковать рекламу
2. Оскорблять других участников и администраторов, призывать к насилию
3. Присылать эротический контент

⚠️ За нарушение правил последует мут или бан.

Также, пожалуйста, думайте о том, что вы пишете: сообщения в интернете могут быть доступны третьим лицам."

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.is_automatic_forward)
def handle_new_post(message):
    try:
        bot.reply_to(message, RULES_TEXT)
    except Exception as e:
        print(f"Ошибка: {e}")

print("Бот запущен и следит за постами...")
bot.infinity_polling()
