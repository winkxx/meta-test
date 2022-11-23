import aria2p
from pyrogram import Client
import sys
url = sys.argv[1]
#gpus = [int(gpus.split(','))]
print(url)
Aria2_host="ws://173.82.45.50"
Aria2_port="6800"
Aria2_secret="5b81c71f3ec03df97928"
#message = str(Aria2_secret)

Telegram_bot_api="1687970568:AAE4nCGaGnFL5NGjm1Zr9muHG3HgtMHmkp0"
Telegram_user_id="1367147811"
Api_hash="d694de0c87f7bee3ecc57da8d0eda7ea"
Api_id="2948911"


client = Client("my_bot", bot_token=Telegram_bot_api,
             api_hash=Api_hash, api_id=Api_id

             )

client.start()

aria2 = aria2p.API(
    aria2p.Client(
        host=Aria2_host,
        port=int(Aria2_port),
        secret=Aria2_secret
    )
)


def the_download(url):

    try:
        download = aria2.add_magnet(url)
    except Exception as e:
        print(e)
        if (str(e).endswith("No URI to download.")):
            print("No link provided!")
            return None
    prevmessagemag = None

the_download(url)
