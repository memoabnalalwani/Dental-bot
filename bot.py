from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from config import TOKEN

keyboard = [
    ["🦷 الخدمات", "📅 حجز موعد"],
    ["📍 الموقع", "📞 التواصل"],
    ["💡 نصائح الأسنان", "⏰ أوقات الدوام"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 أهلاً وسهلاً بكم في\n\n"
        "🦷 المجمع الاستشاري الأول لطب الأسنان\n"
        "الدكتور إبراهيم أحمد العلواني\n\n"
        "اختر الخدمة التي تريدها من الأزرار بالأسفل."
    )
    await update.message.reply_text(text, reply_markup=reply_markup)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🦷 الخدمات":
        msg = (
            "🦷 خدماتنا:\n\n"
            "• حشوات تجميلية\n"
            "• علاج العصب\n"
            "• تركيبات ثابتة ومتحركة\n"
            "• تنظيف وتلميع الأسنان\n"
            "• علاج اللثة\n"
            "• قلع الأسنان"
        )

    elif text == "📅 حجز موعد":
        msg = (
            "📅 لحجز موعد أرسل:\n\n"
            "• الاسم\n"
            "• رقم الهاتف\n"
            "• الخدمة المطلوبة\n"
            "• اليوم المناسب"
        )

    elif text == "📍 الموقع":
        msg = "📍 ذمار - شارع رداع - سوق عنس - فوق بوفية الريان"

    elif text == "📞 التواصل":
        msg = "📞 782684900"

    elif text == "💡 نصائح الأسنان":
        msg = "💡 نظف أسنانك مرتين يومياً واستخدم خيط الأسنان بانتظام."

    elif text == "⏰ أوقات الدوام":
        msg = "⏰ السبت إلى الخميس\n9:00 صباحاً - 8:00 مساءً"

    else:
        msg = "اختر أحد الأزرار الموجودة بالأسفل."

    await update.message.reply_text(msg)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Bot is running...")
app.run_polling()
