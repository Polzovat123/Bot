import telebot

API_TOKEN = '748088742:AAETJ2Hp4GCVoPU74hrsQFZ-BQ6ZqZ7GBb4'

bot = telebot.TeleBot(API_TOKEN, skip_pending= True)	

@bot.message_handler(func=lambda message:True)
def echo_Words(message):
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.first_name)
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.id)

#bot.reply_to()
bot.polling()	
