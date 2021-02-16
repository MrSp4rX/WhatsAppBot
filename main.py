#!/usr/bin/env python3
from flask import Flask, request, jsonify
from os import system
from subprocess import getoutput
import requests, re
from random import choice
from time import sleep
#system('clear')

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def extract_url(string):
    f = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",string)[0][0].strip("('").split('?')[0]
    return f

def main(query):
    url = 'https://unsplash.com/s/photos/'+query
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url,headers=headers)
    collected = []
    for i in r.content.decode().split(' '):
        if 'images.unsplash.com/photo-' in i:
            collected.append(i)
    return extract_url(choice(collected))



def send(target, msg, type):
    if str(type) == 'viber_message_service':
    	data = {"from": { "type": "viber_service_msg", "id": "16273" }, "to": { "type": "viber_service_msg", "number": target }, "message": {"content": {"type": "text","text": msg}}}
    	
    elif str(type) == 'messenger':
    	data = {"from": { "type": "messenger", "id": "107083064136738" },"to": { "type": "messenger", "id": "3437957822994300" },"message": {"content": {"type": "text","text": msg}}}
    else:
        data = {
        "from": {"type": type, "number": "14157386170"},
        "to": {"type": type, "number": target},
        "message": {"content": {"type": "text", "text": msg}},
    }

    requests.post(
        "https://messages-sandbox.nexmo.com/v0.1/messages",
        json=data,
        auth=("d1e77dfc", "qe6nQvRRQPq3HS6u"),
    )
    return msg



abuse = ['lavda','bhosadike','bsdk', 'bhsdk', 'chod', 'lund', 'gand', 'jerk', 'lode', 'loda', 'chut', 'bc', 'mc','mkc','jhat','suwar','kutte','randi','bhosadi', 'loda', 'lawda', 'ashole','fuck'
]

abuse_reply = [
	'Bhosadi ke aisa thappad marunga tere muh ke dant gad se hoker girenge.',
	'Jija se bkchodi krta hai maderchod tamiz sikh lowde.',
	'Gand mei tere salayi ghusa ke swetter bna dunga.',
	'Jhant khayega mera behen ke lowda.',
	'Teri ammy ka asiq hun wo v khufiya asiq ati hai mujhse chummiya lene apne chut pe.',
	'Teri ammy ke gand ko mukka marke tod dunga maderchod baap se bakchodi',
	'Bhagg maderchod teri ammy toh nukkad ki randi hai re.',
	'300 rs wali randi ke aulad.',
	'Teri behn ko utha ke salwar ke sath hi pelunga.',
	'Hahahaha gandu tera baal pakad ke diwal se lada lada ke tera seer phod ke teri ammy ka mang bharunga',
	'Madarchod Zuban pe conrol karo warna gand faad denge',
	'Your Dady can only Abuse Samjha  Bhosadike',
	'Jada Shanpatti nahi warna, Shahtoot ki Patli dandi maar maar ke Chutad pr *Rockstart* likh dunga'

]
banned_users = []

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    data = request.get_json()
    number = data['from']['number']
    msg = data['message']['content']['text']
    type = data['from']['type']
    print(data)
    print(f'>>> {number} sent {msg}\n')
    for i in range(1):
        if str(number) != '919519874704':
            send('919519874704', f"wa.me/{str(number)} sent *{str(msg)}*", type)
        
    # print(banned_users)
    if str(number) in banned_users:
        print(f'<<< Bhosada Trap sent {send(number, "You are Banned kiddo. Contact *MrSp4rX* to be Unban.", type)}\n')
        send('919519874704', f"wa.me/{str(number)} is a Banned User and he/she wanna send {str(msg)} to me.", type)
    else:
        if str(msg).lower()=='start':
            print(f'<<< Bhosada Trap sent {send(number, "Hiii bro whats up?", type)}\n')

        # elif str(number) != '919519874704':
        #     send('919519874704', f'wa.me/{str(number)} sent _*{str(msg)}*_ to *Bhosada Trap*')

        elif str(msg).startswith('/'):
            if str(number) == '919519874704':
                if 'ban' in str(msg):
                    banned_users.append(str(msg).replace('/ban ', ''))
                    user = str(msg).replace('/ban ','')
                    print(f"<<< Bhosada Trap sent {send('919519874704', f'Congrats Daddy! We successfully Banned wa.me/{user}', type)}\n")
                
                elif 'run' in str(msg).lower():
                    temp = str(msg).lower().split()
                    temp = getoutput(str(temp[1:]))
                    print(f"<<< Bhosada Trap sent {send('919519874704', temp, type)}")

                elif 'remove' in str(msg):
                    try:
                        unban_user = str(msg).replace('/remove ', '')
                        banned_users.remove(unban_user)
                        print(f"<<< Bhosada Trap sent {send('919519874704', f'Wow! wa.me/{unban_user} has been Unban Now', type)}\n")

                    except:
                        print(f"<<< Bhosada Trap sent {send('919519874704', 'Something Went Wrong...', type)}\n")
                
                elif 'abuse' in str(msg):
                    victim = str(msg).replace("/abuse ", "")
                    print(f"<<< Bhosada Trap sent {send(victim, choice(abuse_reply), type)}\n")
                    
                else:
                    pass

            else:
                print(f"<<< Bhosada Trap sent {send(number, 'You are not Allowed to Run Admin Commands.', type)}\n")
                print(f"<<< Bhosada Trap sent {send('919519874704', f'wa.me/{str(number)} wanna Run Admin Commands.', type)}\n")
            
        elif str(msg).lower()=='send courses':
            send(number, 'No courses now', type)
        
        elif 'image' in str(msg).lower():
                msg = str(msg).split()
                msg = str(msg[1:])
                print(str(msg))
                if len(msg)>=1:
                    print(f'\n<<< Bhosada Trap sent {send(number, main(str(msg)), type)}\n')
                else:
                    print(f'\n<<< Bhosada Trap sent {send(number, "Please Write *Image* Command Clearly...", type)}\n')
                
        
        elif 'help' in str(msg).lower():
            print(f'\n<<< Bhosada Trap sent {send(number, "Hey, I am a Bot. My name is *Bhosada Trap*. I was created by *Mr. SparX*. He is my Owner.", type)}\n')
        
        elif str(msg).lower() == 'commands':
            print(f"\n<<< Bhosada Trap Sent {send(number, '*Ispammer* Command is used for Bombing on Indain numbers. *Help* Command is used to know about me. *Commands* Command is used to know All the commsnds. *Image* Command is used to Retrieve image of any Catagory. *Start* Command is used to check if Bot is Offline or Online. *Ping* Command is to Ping the Bot.', type)}\n")
        elif 'ispammer' in str(msg).lower():
            try:
                st = str(msg).lower().split()
                times, num = int(st[2]), str(st[-1])
                if times > 500:
                    print(f"\n<<< Bhosada Trap Sent {send(number, '500 se jada nahi bhej skte', type)}\n")
                elif len(str(num)) > 10:
                    print(f"\n<<< Bhosada Trap Sent {send(number, 'Sahi Number likho', type)}\n")
                elif len(str(num)) < 10:
                    print(f"\n<<< Bhosada Trap Sent {send(number, 'Sahi Number likho', type)}\n")
                elif len(str(num)) == 10 and times <= 500:
                    if str(num)=='9519874704':
                        print(f"\n<<< Bhosada Trap Sent {send(number, 'Baap Se Backchodi nahi beta. Teko kya lagta hai *MrSparX* chutiya hai? Abhi dekhna teri kaise gand marta hai vo.', type)}\n")
                        print(f"\n<<< Bhosada Trap Sent {send('919519874704', f'wa.me/{number} wants to do SMS and Call Bombing on You. Be Careful Sir...', type)}\n")
                    else:
                        print(f"\n<<< Bhosada Trap Sent {send(number, 'Wow! Bombing Started...', type)}\n")
                        system(f'ispammer -m {str(times)} -t {str(num)}')
                        print(f"\n<<< Bhosada Trap Sent {send(number, 'Congratulations! Bombing Successfull...', type)}\n")
            except:
                print(f"\n<<< Bhosada Trap Sent {send(number, 'Something Went Wrong...', type)}\n")
            
            # else:
            #     send(number, 'Something Went Wrong...')
            
        elif str(msg).lower() == 'ping':
            if number=='919519874704':
                print(f"<<< Bhosada Trap sent {send(number, 'Pong Daddy!', type)}\n")
            else:
                print(f"<<< Bhosada Trap sent {send(number, 'Pong!', type)}\n")
        else:
            msg = str(msg)
            for word in abuse:
                if word in str(msg).lower():
                    if number=='919519874704':
                        break
                    else:
                        print(f'\n<<< Bhosada Trap sent {send(number, choice(abuse_reply), type)}\n')
    return ''

@app.route("/")
def index():
    return '''

# Bhosada Trap

Introducing *Bhosada Trap* which is my New bot and I am glad to inform you that You guys can use my Bot via WhatsApp. To use this Bot first verify your Number by sending *Join theft lived* message on http://wa.me/14157386170 or You can verify your Number by just clicking on this link: http://wa.me/14157386170?text=Join%20theft%20lived and then use these HelpFul Commands:

1. *Start*

2. *Help*

3. *Commands*

4. *Image*

5. *Ping*

*Note: Don't Use Abuse Words there otherwise Bot will abuse you Hard. This Bot is Under Development*

*Credits: Name Credit Goes to R37r0.Gh057*

*Source Code:* https://github.com/MrSp4rX/WhatsAppBot

*Report Bugs:* http://wa.me/919519874704

*Open Issue:* https://github.com/MrSp4rX/WhatsAppBot/issues/new

*For Protecting Your number from iSpammer tool for Lifetime contact http://wa.me/919519874704* 

*For Queries, Banning, UnBanning and Abusing Persons contact http://wa.me/919519874704*
'''

if __name__ == '__main__':
    app.run(debug=True)
