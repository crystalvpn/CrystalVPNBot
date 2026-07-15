from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8873771275:AAG41QbOdIj0iCAez1aMuL2D_VkLFRqVdmI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 خرید VPN", callback_data="buy")],
        [InlineKeyboardButton("💳 تعرفه‌ها", callback_data="prices")],
        [InlineKeyboardButton("🆘 پشتیبانی", callback_data="support")],
    ]

    await update.message.reply_text(
        "🌐 CrYsTaL VpN\n\nبه ربات فروش VPN خوش آمدید.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        keyboard = [
            [InlineKeyboardButton("📅 سرویس یک ماهه", callback_data="month1")],
            [InlineKeyboardButton("📅 سرویس دو ماهه", callback_data="month2")],
            [InlineKeyboardButton("📅 سرویس سه ماهه", callback_data="month3")],
        ]
        await query.edit_message_text(
            "مدت سرویس را انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "prices":
        await query.edit_message_text(
            "برای مشاهده قیمت‌ها ابتدا روی «خرید VPN» بزن."
        )

    elif query.data == "support":
        await query.edit_message_text(
            "پشتیبانی:\n@YourUsername"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot Started...")
app.run_polling()
