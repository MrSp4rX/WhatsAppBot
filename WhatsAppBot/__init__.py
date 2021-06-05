#!/usr/bin/env python3
from flask import Flask, request, jsonify
from os import system, remove
from subprocess import getoutput
import requests, re
from random import choice, random
from time import sleep
import logging
import random

app = Flask(__name__)



log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def main(query):
    if " " in str(query):
        query = str(query).replace(' ', '%20')
    else:
        pass

    num = random.randint(0, 16)
    response = requests.get(f'https://api.unsplash.com/search/photos?client_id=iq6ZmfICfiWv8NNoobrG1vqCr6TOC5qBNR1FE4CvfDA&query={query}&order_by=latest&orientation=portrait').json()
    desc = response['results'][num]['description']
    url = response['results'][num]['urls']['regular']
    created_at = response['results'][num]['created_at']
    width = response['results'][num]['width']
    height = response['results'][num]['height']
    likes = response['results'][num]['likes']
    return {
        "desc":desc,
        "url":url,
        "created_at":created_at,
        "size":{"width":width, "height":height},
        "likes":likes
    }




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

def img_send(target, msg, url):
    data = {"from": { "type": "whatsapp", "number": "14157386170" }, "to": { "type": "whatsapp", "number": target }, "message": { "content": { "type": "image", "image": { "url": url, "caption": msg } } }}
    auth=("d1e77dfc", "qe6nQvRRQPq3HS6u")
    response = requests.post('https://messages-sandbox.nexmo.com/v0.1/messages', json=data, auth=auth)
    return 'Image sent'


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
	'Jada Shanpatti nahi warna, Shahtoot ki Patli dandi maar maar ke Chutad pr *Rockstart* likh dunga',
        'Yahi Patak ke chod denge, ab nikal madarchod'

]
banned_users = []

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    data = request.get_json()
    msg_uid = data['message_uuid']
    to_number = data['to']['number']
    time_stamp = data['timestamp']
    number = data['from']['number']
    msg = data['message']['content']['text']
    type = data['from']['type']
    with open('message.log', 'a+') as f:
        f.write(number+'  sent  '+msg+'  to  '+to_number+'  at  '+time_stamp+'  on  '+type+'  with Message UUID  '+msg_uid+'\n\n\n')
    print(f'>>> {number} sent {msg}\n')
    for i in range(1):
        if str(number) != '919519874704':
            send('919519874704', f"wa.me/{str(number)} sent *{str(msg)}*", type)
            
    if str(number) in banned_users:
        print(f'<<< Bhosada Trap sent {send(number, "You are Banned kiddo. Contact *MrSp4rX* to be Unban.", type)}\n')
        send('919519874704', f"wa.me/{str(number)} is a Banned User and he/she wanna send {str(msg)} to me.", type)
    else:
        if str(msg).lower()=='start':
            print(f'<<< Bhosada Trap sent {send(number, "Hiii bro whats up?", type)}\n')

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

                elif str(msg) == "/send status detail":
                    with open('status.log', 'r') as f:
                        status_log = f.read()
                        if status_log != "":
                            print(f"<<< Bhosada Trap sent {send('919519874704', status_log, type)}\n")
                        else:
                            print(f"<<< Bhosada Trap sent {send('919519874704', 'Status Logs are not Found', type)}\n")
                
                elif str(msg) == "/send message detail":
                    with open('message.log', 'r') as f:
                        message_log = f.read()
                        if message_log != "":
                            print(f"<<< Bhosada Trap sent {send('919519874704', message_log, type)}\n")
                        else:
                            print(f"<<< Bhosada Trap sent {send('919519874704', 'Message Logs are not Found', type)}\n")

                elif str(msg) == "/delete message log":
                    remove('message.log')
                    try:
                        open('message.log', 'r')
                        print(f"<<< Bhosada Trap sent {send('919519874704', 'Status Logs are not Deleted.', type)}\n")
                    except:
                        print(f"<<< Bhosada Trap sent {send('919519874704', 'Message Logs are Deleted.', type)}\n")
                        

                elif str(msg) == "/delete status log":
                    try:
                        with open('status.log', 'w') as f:
                            f.write('')
                        print(f"<<< Bhosada Trap sent {send('919519874704', 'Status Logs are Deleted.', type)}\n")

                    except:
                        print(f"<<< Bhosada Trap sent {send('919519874704', 'Status Logs are not Deleted.', type)}\n")

            else:
                print(f"<<< Bhosada Trap sent {send(number, 'You are not Allowed to Run Admin Commands.', type)}\n")
                print(f"<<< Bhosada Trap sent {send('919519874704', f'wa.me/{str(number)} wanna Run Admin Commands.', type)}\n")
            
        elif str(msg).lower()=='send courses':
            send(number, 'No courses now', type)
        
        elif 'image' in str(msg).lower():
            msg = str(msg).lower().replace('image ', '')
            try:
                data = main(str(msg))
                raw_caption, url, created_at, size, likes = data['desc'], data['url'], data['created_at'], data['size'], data['likes']
                main_caption = f"*Description:* {raw_caption}. This image is Created at {created_at}. Height and Width of this Image is {size['height']} X {size['width']}. This Image has {likes} Likes on https://Unsplash.com. *Note:* Searching method of this Website isn't Working Well, Images can be Non-Accurate."
                print(f'\n<<< Bhosada Trap sent {main_caption} with Corresponding Image. {img_send(number, main_caption, url)}\n')
            except Exception as e:
                print(e)
                print(f'\n<<< Bhosada Trap sent {send(number, "Please Write *Image* Command Clearly...", type)}\n')
                
        
        elif 'help' in str(msg).lower():
            print(f'\n<<< Bhosada Trap sent {send(number, "Hey, I am a Bot. My name is *Bhosada Trap*. I was created by *Mr. SparX*. He is my Owner.", type)}\n')
        
        elif str(msg).lower() == 'commands':
            print(f"\n<<< Bhosada Trap Sent {send(number, '*Ispammer* Command is used for Bombing on Indain numbers. *Help* Command is used to know about me. *Commands* Command is used to know All the commsnds. *Image* Command is used to Retrieve image of any Catagory. *Start* Command is used to check if Bot is Offline or Online. *Ping* Command is to Ping the Bot.', type)}\n")
        elif 'ispammer' in str(msg).lower():
            print(f"\n<<< Bhosada Trap Sent {send(number, 'This Command is unable due to some Reasons. Any query? Contact: wa.me/919519874704', type)}\n")
            
        elif str(msg).lower() == 'ping':
            if number=='919519874704':
                print(f"<<< Bhosada Trap sent {send(number, 'Pong Bappu!', type)}\n")
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

@app.route("/webhooks/inbound-status", methods=['POST'])
def inbound_status():
    data = request.get_json()
    msg_uid = data['message_uuid']
    from_number = data['from']['number']
    to_number = data['to']['number']
    time_stamp = data['timestamp']
    status = data['status']
    with open('status.log', 'a+') as f:
        f.write(msg_uid+'   ')
        f.write(from_number+'  sent reply to  '+to_number+'  at  '+time_stamp+'  and message is  '+status+'  with Message UUID  '+'\n\n\n')
    return ''

@app.route("/")
def index():
    return '''

<h3>Bhosada Trap</h3>
<br><br>
Introducing *Bhosada Trap* which is my New bot and I am glad to inform you that You guys can use my Bot via WhatsApp. To use this Bot first verify your Number by sending *Join theft lived* message on http://wa.me/14157386170 or You can verify your Number by just clicking on this link: http://wa.me/14157386170?text=Join%20theft%20lived and then use these HelpFul Commands:
<br><br>
1. Start<br><br>

2. Help<br><br>

3. Commands<br><br>

4. Image<br><br>

5. Ping<br><br>

<strong>Note:</strong> Don't Use Abuse Words there otherwise Bot will abuse you Hard. This Bot is Under Development<br><br>

* <strong>Credits:</strong> Name Credit Goes to <strong>R37r0.Gh057</strong><br><br>

* <strong>Source Code:</strong> <a href="https://github.com/MrSp4rX/WhatsAppBot">https://github.com/MrSp4rX/WhatsAppBot</a><br><br>

* <strong>Report Bugs:</strong> <a href="http://wa.me/919519874704">+91 95198 74704</a><br><br>

* <strong>Open Issue:</strong> <a href="https://github.com/MrSp4rX/WhatsAppBot/issues/new">https://github.com/MrSp4rX/WhatsAppBot/issues/new</a><br><br>

* For Protecting Your number from iSpammer tool for Lifetime contact  <a href="http://wa.me/919519874704">Here.</a><br><br>

* For Queries, Banning, UnBanning and Abusing Persons contact <a href="http://wa.me/919519874704">Here.</a><br><br>

'''

if __name__ == '__main__':
    app.run()
