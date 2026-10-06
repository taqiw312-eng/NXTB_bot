import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_ID = 7960402387

logging.basicConfig(level=logging.INFO)

SCRIPTS = [
    {"name": "Chilli Hub", "games": "Steal An Egg",
     "load": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/tienkhanh1/spicy/main/Chilli.lua"))()'},
    {"name": "Snowy Hub", "games": "Speed Keyboard",
     "load": 'loadstring(game:HttpGet("https://flowauth.net/v1/ui/a87f00d9adf63658655fcd02ab86a4ef.lua"))()'},
    {"name": "Decode Hub", "games": "متعدد",
     "load": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ItzYumi/Decode/refs/heads/main/DE%3ACODE.lua", true))()'},
]

async def start(update, ctx):
    u = update.effective_user
    txt = f"👋 أهلاً <b>{u.first_name}</b>\n\n🔑 <b>Delta Key Bot</b>\n━━━━━━━━━━━━━━\n\nاختر:"
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 احصل على مفتاح", callback_data="getkey")],
        [InlineKeyboardButton("📚 مكتبة السكربتات", callback_data="scripts")],
        [InlineKeyboardButton("📊 إحصائياتي", callback_data="stats")],
        [InlineKeyboardButton("🆘 مساعدة", callback_data="help")],
    ])
    await update.message.reply_text(txt, reply_markup=kb, parse_mode="HTML")

async def key_cmd(update, ctx):
    u = update.effective_user
    key = f"DELTA-{u.id}-{abs(hash(u.id)) % 100000:05d}"
    txt = f"🔑 <b>مفتاحك جاهز</b>\n━━━━━━━━━━━━━━\n\n<code>{key}</code>\n\n⏱️ صالح 24 ساعة"
    kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع", callback_data="back")]])
    await update.message.reply_text(txt, reply_markup=kb, parse_mode="HTML")

async def button_handler(update, ctx):
    q = update.callback_query
    await q.answer()
    d = q.data
    u = q.from_user
    if d == "getkey":
        key = f"DELTA-{u.id}-{abs(hash(u.id)) % 100000:05d}"
        txt = f"🔑 <b>مفتاحك</b>\n\n<code>{key}</code>\n\n⏱️ صالح 24 ساعة"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع", callback_data="back")]])
        await q.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
    elif d == "scripts":
        btns = [[InlineKeyboardButton(f"🎮 {s['name']}", callback_data=f"script_{i}")] for i, s in enumerate(SCRIPTS)]
        btns.append([InlineKeyboardButton("🔙 رجوع", callback_data="back")])
        await q.edit_message_text("📚 <b>مكتبة السكربتات</b>", reply_markup=InlineKeyboardMarkup(btns), parse_mode="HTML")
    elif d.startswith("script_"):
        i = int(d.split("_")[1])
        s = SCRIPTS[i]
        txt = f"🎮 <b>{s['name']}</b>\n🎯 {s['games']}\n\n<code>{s['load']}</code>"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 السكربتات", callback_data="scripts")]])
        await q.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
    elif d == "stats":
        txt = f"📊 <b>إحصائياتك</b>\n\n👤 {u.first_name}\n🆔 <code>{u.id}</code>"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع", callback_data="back")]])
        await q.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
    elif d == "help":
        txt = "🆘 <b>المساعدة</b>\n\n/start — البداية\n/key — مفتاح\n/scripts — السكربتات\n/stats — إحصائياتك"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع", callback_data="back")]])
        await q.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
    elif d == "back":
        txt = f"👋 أهلاً <b>{u.first_name}</b>\n\n🔑 <b>Delta Key Bot</b>"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔑 احصل على مفتاح", callback_data="getkey")],
            [InlineKeyboardButton("📚 مكتبة السكربتات", callback_data="scripts")],
            [InlineKeyboardButton("📊 إحصائياتي", callback_data="stats")],
            [InlineKeyboardButton("🆘 مساعدة", callback_data="help")],
        ])
        await q.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("key", key_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
