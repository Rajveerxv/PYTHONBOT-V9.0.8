from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To PYTHONBOT String Session\nGenerator By @Legendl_Mr_Hacker\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it) \n\n `{session}` \n\n And Visit @Nothing_x_7 For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing PYTHONBOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +914352764556! Kindly Retry"
        )
        print("")
        continue
    break

    
