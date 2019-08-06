import telebot



bot = telebot.TeleBot(API_TOKEN, skip_pending= True)	

@bot.message_handler(func=lambda message:True)
def echo_Words(message):
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.first_name)
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.id)

#bot.reply_to()
bot.polling()	
