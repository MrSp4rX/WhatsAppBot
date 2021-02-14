import os

def send(target, msg):
	os.system('''
	curl -X POST https://messages-sandbox.nexmo.com/v0.1/messages \
	-u 'd1e77dfc:qe6nQvRRQPq3HS6u' \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d '{
	    "from": { "type": "whatsapp", "number": 	"14157386170" },
	    "to": { "type": "whatsapp", "number": "'''+target+'''" },
	    "message": {
	      "content": {
	        "type": "text",
	        "text": "'''+msg+'''"
	      }
	    }
	  }'  > /dev/null 2>&1
	''')
	return msg