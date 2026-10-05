import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت الخاص بك
TOKEN = '8507821176:AAFeB87GiBqnJjnbv-UDbQ5RPorOgJVeyis'
bot = telebot.TeleBot(TOKEN)

# رسالة البداية والأقسام الرئيسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت السكربتات والهاكات الرسمي 🚀\n\n"
        "اختر القسم المناسب لك من الأزرار أدناه:"
    )
    
    markup = InlineKeyboardMarkup(row_width=2)
    btn_scripts = InlineKeyboardButton("📂 قسم السكربتات", callback_data="scripts_menu")
    btn_hub = InlineKeyboardButton("🔥 سكربتات Hub", callback_data="hub_menu")
    btn_dev = InlineKeyboardButton("👨‍💻 المطور", url="https://t.me/your_username")
    btn_channel = InlineKeyboardButton("📢 قناة التليجرام", url="https://t.me/your_channel")
    
    markup.add(btn_scripts, btn_hub, btn_dev, btn_channel)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# التعامل مع الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "scripts_menu":
        markup = InlineKeyboardMarkup(row_width=1)
        btn_blade = InlineKeyboardButton("⚔️ Blade Ball (أحدث إصدار)", callback_data="script_blade")
        btn_timebomb = InlineKeyboardButton("💣 Time Bomb (سكربت قوي)", callback_data="script_timebomb")
        btn_back = InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")
        markup.add(btn_blade, btn_timebomb, btn_back)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="اختر اللعبة لعرض السكربت الخاص بها:",
            reply_markup=markup
        )
        
    elif call.data == "hub_menu":
        markup = InlineKeyboardMarkup(row_width=1)
        btn_phoenix = InlineKeyboardButton("🦅 PHOENIX HUB (النسخة الشاملة)", callback_data="script_phoenix")
        btn_back = InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")
        markup.add(btn_phoenix, btn_back)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="السكربتات الشاملة (Hub):",
            reply_markup=markup
        )
        
    elif call.data == "script_blade":
        code_text = (
            "⚔️ **سكربت Blade Ball (آخر إصدار):**\n\n"
            "```lua\n"
            "loadstring(game:HttpGet('[https://raw.githubusercontent.com/taqiw312-eng/scripts/main/bladeball.lua](https://raw.githubusercontent.com/taqiw312-eng/scripts/main/bladeball.lua)'))()\n"
            "```"
        )
        bot.answer_callback_query(call.id, "تم جلب السكربت بنجاح!")
        bot.send_message(call.message.chat.id, code_text, parse_mode="Markdown")
        
    elif call.data == "script_timebomb":
        code_text = (
            "💣 **سكربت Time Bomb:**\n\n"
            "```lua\n"
            "loadstring(game:HttpGet('[https://raw.githubusercontent.com/taqiw312-eng/scripts/main/timebomb.lua](https://raw.githubusercontent.com/taqiw312-eng/scripts/main/timebomb.lua)'))()\n"
            "```"
        )
        bot.answer_callback_query(call.id, "تم جلب السكربت بنجاح!")
        bot.send_message(call.message.chat.id, code_text, parse_mode="Markdown")

    elif call.data == "script_phoenix":
        code_text = (
            "🦅 **PHOENIX HUB Script:**\n\n"
            "```lua\n"
            "loadstring(game:HttpGet('[https://raw.githubusercontent.com/taqiw312-eng/scripts/main/phoenixhub.lua](https://raw.githubusercontent.com/taqiw312-eng/scripts/main/phoenixhub.lua)'))()\n"
            "```"
        )
        bot.answer_callback_query(call.id, "تم جلب السكربت بنجاح!")
        bot.send_message(call.message.chat.id, code_text, parse_mode="Markdown")

    elif call.data == "main_menu":
        welcome_text = "أهلاً بك مرة أخرى في القائمة الرئيسية 🚀\nاختر القسم المناسب لك:"
        markup = InlineKeyboardMarkup(row_width=2)
        btn_scripts = InlineKeyboardButton("📂 قسم السكربتات", callback_data="scripts_menu")
        btn_hub = InlineKeyboardButton("🔥 سكربتات Hub", callback_data="hub_menu")
        btn_dev = InlineKeyboardButton("👨‍💻 المطور", url="https://t.me/your_username")
        btn_channel = InlineKeyboardButton("📢 قناة التليجرام", url="https://t.me/your_channel")
        markup.add(btn_scripts, btn_hub, btn_dev, btn_channel)
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=welcome_text,
            reply_markup=markup
        )

# تشغيل البوت
print("Bot is running...")
bot.infinity_polling()
