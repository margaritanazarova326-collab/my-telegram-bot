import os
import telebot
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = os.getenv('BOT_TOKEN')
GROUP_ID = -1004227685910
RULES_TEXT = """📌 Пожалуйста, ознакомьтесь с правилами сообщества перед тем, как писать комментарии.

<b>‼️ ПРАВИЛА ‼️</b>

В чате запрещено:
1. Спамить, публиковать рекламу
2. Оскорблять других участников и администраторов, призывать к насилию
3. Присылать эротический контент

⚠️ За нарушение правил последует мут или бан.

Также, пожалуйста, думайте о том, что вы пишете: сообщения в интернете могут быть доступны третьим лицам."""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.is_automatic_forward)
def handle_new_post(message):
    try:
        bot.reply_to(message, RULES_TEXT)
    except Exception as e:
        print(f"Ошибка: {e}")

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_health_check():
    port = int(os.environ.get("PORT", 10000))  # Render передаёт порт в переменной PORT
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_health_check, daemon=True).start()

print("Бот запущен и следит за постами...")
bot.infinity_polling()
