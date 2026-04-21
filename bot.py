import telebot
import random
import time
import os
import yaml

# Загружаем конфиг и языки
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

with open('lang.yaml', 'r', encoding='utf-8') as f:
    lang = yaml.safe_load(f)

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("❌ TOKEN не найден!")

bot = telebot.TeleBot(TOKEN)

# ←←←← ЭТО САМОЕ ВАЖНОЕ ←←←←
bot.delete_webhook(drop_pending_updates=True)
print("✅ Webhook удалён, старые процессы сброшены")

print("✅ Бот запущен на Railway | Профит с Уолл-Стрит")

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = lang.get('welcome', 'Добро пожаловать!')
    bot.send_message(
        message.chat.id, 
        welcome_text.format(first_name=message.from_user.first_name), 
        parse_mode='HTML'
    )

@bot.message_handler(commands=['signals'])
def send_signal(message):
    signals = {
        "Lucky Jet": ["Выходи на ×1.75 – 2.1", "Жди ×3.0+", "Сейчас безопасно до ×1.6"],
        "Mines": ["Открывай углы: 1-2-4", "Избегай центра"],
        "Aviator": ["Вылетай на ×2.0 – 2.6"]
    }
    game = random.choice(list(signals.keys()))
    signal = random.choice(signals[game])
    
    text = f"""
🚀 **Новый сигнал от AI**

🎮 Игра: **{game}**
💡 Рекомендация: **{signal}**
⏰ Время: {time.strftime('%H:%M:%S')}
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

print("Бот готов к работе")
bot.infinity_polling(timeout=30, long_polling_timeout=30)
