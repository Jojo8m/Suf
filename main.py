import requests,random,json,os,sys
import flask
import telebot
from telebot import types
from user_agent import generate_user_agent
from config import *
import logging
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

call  = types.InlineKeyboardButton(text = "StArT BoT", callback_data = 'Suf')
program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
@bot.message_handler(commands=['start'])
def start(message):
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 2
	Keyy.add(call,program)
	try:
		first = message.chat.first_name
		bot.send_message(message.chat.id,f"*- Hello {first}\n\n- The BoT HunT TikTok\n\n- HunT Domin HotMaiL\n\n- BY:- @MMPMMMM*",parse_mode="markdown",reply_markup=Keyy)
		pass
	except:
		print('Error Token')
		exit()
@bot.callback_query_handler(func=lambda call: True)
def bin_mos(call):
	if call.data =="Suf":
		check10(call.message)
	if call.data =="getmy1":
		getcheck1(call.message)
	if call.data =="getmy11":
		getcheck11(call.message)
	if call.data =="getmy21":
		getcheck21(call.message)
	if call.data =="getmy31":
		getcheck31(call.message)
	#tiktok

					
def getcheck31(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(7))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		


def getcheck21(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(6))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)

def getcheck11(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(5))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		
			
def getcheck1(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(4))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")

			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		

def check10(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'getmy1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'getmy11')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'getmy21')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'getmy31')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://suftool.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.polling()