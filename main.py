from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

TOKEN = os.environ("TELEGRAM_BOT_TOKEN")  # Get token from environment variable

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 Visit Website", url="https://pharmawizards.com/")],
        [
            InlineKeyboardButton(
                "📝 Registration Form",
                url="https://docs.google.com/forms/d/e/1FAIpQLSc-6D-b03fYuD9hR_OW2BAmJsA-TsZ6jxc-BVqzxtQJHHWUlQ/viewform?usp=dialog ",
            )
        ],
        [InlineKeyboardButton("💬 Chat on WhatsApp", url="https://wa.me/9817516640")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎉 *Welcome to PharmaWizards!* 🎉\n\n"
        "We're thrilled to have you here! 🚀\n\n"
        "*Recall at your will* — Affordable GPAT coaching brought to you by PU Alumni.\n\n"
        "👉 *Get started by choosing an option below:*\n\n"
        "- 🌐 Visit our website for resources and updates\n"
        "- 📝 Register now to unlock your potential\n"
        "- 💬 Chat with us on WhatsApp for instant support\n\n"
        "Thank you for joining the PharmaWizards community. Let's ace GPAT together! 💡✨",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Bot is running... Press Ctrl+C to stop.")
app.run_polling()
