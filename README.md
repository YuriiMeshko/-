# 🚀 Telegram Webhook Forex Bot

Цей бот працює через FastAPI + Webhook і може запускатись на безкоштовному тарифі Render.

---

## 🔧 Як розгорнути

1. Залий вміст цього репозиторію на GitHub
2. Перейди на: [https://render.com/deploy](https://render.com/deploy)
3. Встав лінк на GitHub-репозиторій

---

## ⚙️ Налаштування

У файлі `config.py` встав свій Telegram токен:
```python
TELEGRAM_TOKEN = "тут_твій_токен"
```

---

## 🌐 Установка Webhook

Після деплою Render надасть тобі URL, наприклад:
```
https://your-bot-name.onrender.com
```

Твій webhook:
```
https://your-bot-name.onrender.com/webhook/ТВОЙ_ТОКЕН
```

🔗 Щоб активувати webhook, встав у браузері (1 раз):
```
https://api.telegram.org/botТВОЙ_ТОКЕН/setWebhook?url=https://your-bot-name.onrender.com/webhook/ТВОЙ_ТОКЕН
```
