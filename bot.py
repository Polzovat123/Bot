import telebot

API_TOKEN = '748088742:AAETJ2Hp4GCVoPU74hrsQFZ-BQ6ZqZ7GBb4'

bot = telebot.TeleBot(API_TOKEN, skip_pending= True)	



@bot.message_handler(commands = ['start'])
def send_welcome(message):
	im = message.chat.first_name
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.first_name)
	bot.send_message(chat_id = message.chat.id,
					text=message.from_user.id)



@bot.message_handler(func=lambda message:True)
def echo_Words(message):
	strin = str(message.text)
	word = 1;
	while strin.find(' ',0 ,len(strin)) != -1:		
		word=word+1
		strin.replace(' ','', 1)
	bot.send_message(chat_id = message.chat.id,
					text=word)

#bot.reply_to()
bot.polling()	
