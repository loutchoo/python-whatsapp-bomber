#librairies
from twilio.rest import Client
import time

#comptes auth
account_sid = 'your twilio sid'
auth_token = 'your twilio token'
client = Client(account_sid, auth_token)

#Envoi du message
def envoi():
	while 1 != 2:
		time.sleep(1)
		message = client.messages.create(
			body=msg,
            from_='whatsapp:+14155238886',
            to=number
                          )



#Accueil
print("\n****************************************************")
print("Whatsapp Bomber ! Created by Loutcho_Q :pp")
print("****************************************************\n")

#Demandes message
number = input("Quel numéro de télephone (whatsapp:+336...) : ")
msg = input("Quel message à envoyer : ")
print("\n")
print("Le numéro à qui vous envoyez un message est : ", number)
print("******************************************************************************************")
print("Le message que vous envoyez est : ", msg)

envoi()