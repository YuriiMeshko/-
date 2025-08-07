from fastapi import FastAPI, Request
import telegram
import asyncio
import config

bot = telegram.Bot(token=config.TELEGRAM_TOKEN)
app = FastAPI()

@app.post(f"/webhook/{config.TELEGRAM_TOKEN}")
async def telegram_webhook(req: Request):
    data = await req.json()
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if text and chat_id:
        if "start" in text.lower():
            await bot.send_message(chat_id=chat_id, text="👋 Бот активний і чекає сигналів!")
        elif "ping" in text.lower():
            await bot.send_message(chat_id=chat_id, text="📡 Я на зв’язку!")

    return {"ok": True}
