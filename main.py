#!/usr/bin/env python3
from flask import Flask, request, jsonify
from send_sms import send
from os import system
from time import sleep
from random import choice
import scrap
system('clear')

app = Flask(__name__)



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
	'Your Dady can only Abuse Samjha  Bhosadike'
]
banned_users = []

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    data = request.get_json()
    number = data['from']['number']
    msg = data['message']['content']['text']
    print(f'>>> {number} sent {msg}\n')
    # print(banned_users)
    if str(number) in banned_users:
        send(number, 'You are Banned kiddo. Contact *MrSp4rX* to be Unban.')
    else:
        if str(msg).lower()=='start':
            print(f'<<< Bhosada Trap sent {send(number, "Hiii bro whats up?")}')

        elif str(number) != '919519874704':
            send('919519874704', f'wa.me/{str(number)} sent _*{str(msg)}*_ to *Bhosada Trap*')

        elif str(msg).startswith('/'):
            if str(number) == '919519874704':
                if 'ban' in str(msg):
                    banned_users.append(str(msg).replace('/ban ', ''))
                    user = str(msg).replace('/ban ','')
                    print(f"<<< Bhosada Trap sent {send('919519874704', f'Congrats Daddy! We successfully Banned wa.me/{user}')}")

                elif 'remove' in str(msg):
                    unban_user = str(msg).replace('/remove ', '')
                    banned_users.remove(unban_user)
                    print(f"<<< Bhosada Trap sent {send('919519874704', f'Wow! wa.me/{unban_user} has been Unban Now')}")
                
                elif 'abuse' in str(msg):
                    victim = str(msg).replace("/abuse ", "")
                    print(f"<<< Bhosada Trap sent {send(victim, choice(abuse_reply))}")
                    

                else:
                    pass

            else:
                print(f"<<< Bhosada Trap sent {send(number, 'You are not Allowed to Run Admin Commands.')}")
                print(f"<<< Bhosada Trap sent {send('919519874704', f'wa.me/{str(number)} wanna Run Admin Commands.')}")
            
        elif str(msg).lower()=='send courses':
            send(number, 'No courses now')
        elif 'image' in str(msg).lower():
                msg = str(msg).split()
                msg = str(msg[1:])
                print(str(msg))
                if len(msg)>=1:
                    print(f'\n<<< Bhosada Trap sent {send(number, scrap.main(str(msg)))}')
                else:
                    print(f'\n<<< Bhosada Trap sent {send(number, "Please Write *Image* Command Clearly...")}')
                
        
        elif 'help' in str(msg).lower():
            print(f'\n<<< Bhosada Trap sent {send(number, "Hey, I am a Bot. My name is *Bhosada Trap*. I was created by *Mr. SparX*. He is my Owner.")}')
        
        elif str(msg).lower() == 'commands':
            print(f"\n<<< Bhosada Trap Sent {send(number, '*Ispammer* Command is used for Bombing on Indain numbers. *Help* Command is used to know about me. *Commands* Command is used to know All the commsnds. *Image* Command is used to Retrieve image of any Catagory. *Start* Command is used to check if Bot is Offline or Online. *Ping* Command is to Ping the Bot.')}")
        elif 'ispammer' in str(msg).lower():
            st = str(msg).lower().split()
            times, num = int(st[2]), str(st[-1])
            if times > 500:
                send(number, '500 se jada nahi bhej skte')
            elif len(str(num)) > 10:
                send(number, 'Sahi Number likho')
            elif len(str(num)) < 10:
                send(number, 'Sahi Number likho')
            elif len(str(num)) == 10 and times <= 500:
                if str(num)=='9519874704':
                    send(number, 'Baap Se Backchodi nahi beta. Teko kya lagta hai *MrSparX* chutiya hai? Abhi dekhna teri kaise gand marta hai vo.')
                    send('919519874704', f'wa.me/{number} wants to do SMS and Call Bombing on You. Be Careful Sir...')
                else:
                    send(number, 'Wow! Bombing Started...')
                    system(f'ispammer -m {str(times)} -t {str(num)}')
                    send(number, 'Congratulations! Bombing Successfull...')
            else:
                send(number, 'Something Went Wrong...')
            
        elif str(msg).lower() == 'ping':
            if number=='919519874704':
                print(f"<<< Bhosada Trap sent {send(number, 'Pong Daddy!')}")
            else:
                print(f"<<< Bhosada Trap sent {send(number, 'Pong!')}")
        else:
            msg = str(msg)
            for word in abuse:
                if word in str(msg).lower():
                    if number=='919519874704':
                        break
                    else:
                        print(f'\n<<< Bhosada Trap sent {send(number, choice(abuse_reply))}')
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
                            
