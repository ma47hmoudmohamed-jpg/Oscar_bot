# Oscar_bot
import telebot TOKEN="8828660771:AAFrzqaH4ScJR8ZgGijxj4kxTE90uZxjVuc" bot=telebot.TeleBot(TOKEN, threaded=False)  @bot.message_handler(commands=['start']) def s(m):     bot.reply_to(m, "شغال صاروخ على Render ⚡")  print("Bot running") bot.infinity_polling(skip_pending=True, timeout=10)
