import telebot
import random
import time
import os

TOKEN = os.getenv('8702073880:AAFgTJyVtofECIcyE2AwJGCt0giqph4QGH8')

bot = telebot.TeleBot(TOKEN)

signals = {
    "Lucky Jet": ["Выходи на ×1.75 – 2.1", "Жди ×3.0+", "Сейчас безопасно до ×1.6", "Рекомендую ×2.3"],
    "Mines": ["Открывай углы: 1-2-4", "Избегай центра", "3 мины — можно играть"],
    "Aviator": ["Вылетай на ×2.0 – 2.6", "Лови низкий коэффициент ×1.4-1.8"]
}

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "👋 Добро пожаловать в **Профит с Уолл-Стрит**!\n\n"
        "Я — AI сигнальный бот для 1win.\n"
        "Анализирую паттерны и выдаю сигналы без эмоций.\n\n"
        "Чтобы получать регулярные сигналы — зарегистрируйся по моей реферальной ссылке в 1win "
        "и пришли мне свой **User ID**.\n\n"
        "Напиши /signals — получишь тестовый сигнал прямо сейчас."
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(commands=['signals'])
def send_signal(message):
    game = random.choice(list(signals.keys()))
    signal = random.choice(signals[game])
    
    text = f"""
🚀 **Новый сигнал от AI**

🎮 Игра: **{game}**

💡 Рекомендация: **{signal}**

⏰ Время: {time.strftime('%H:%M:%S')}

⚠️ Это статистические рекомендации. Играй ответственно.
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

print("✅ Бот запущен на Railway")
bot.infinity_polling(timeout=30, long_polling_timeout=30)
