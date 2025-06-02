import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

piadas_prontas = [
    "Por que o computador foi ao médico? Porque estava com um vírus.",
    "Eu ia contar uma piada sobre pizza, mas ela é meio sem graça.",
    "O que o peixe disse para o outro? Nada.",
    "Programador não morre, ele faz um commit final.",
    "O que o zero falou para o oito? Belo cinto!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎭 Olá! Eu sou o Piadista, seu bot de humor duvidoso.
Use /piada para rir!")

async def piada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from random import choice
    resposta = choice(piadas_prontas)
    await update.message.reply_text(f"😂 {resposta}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("piada", piada))
    print("Bot rodando... 🤡")
    app.run_polling()
