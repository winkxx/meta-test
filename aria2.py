import aria2p
from pyrogram import Client
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',type=str,help='磁力链接或者直链')
args=parser.parse_args()

if not args.url:
    parser.print_help()
    sys.exit(0)

Aria2_host="http://173.82.45.50"
Aria2_port="6800"
Aria2_secret="5b81c71f3ec03df97928"
message = str(Aria2_secret)
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
        print(args.url)
        print(f"成功添加{args.url}")
        client.send_message(chat_id=int(Telegram_user_id),text=f"成功添加{args.url}")
        #print(download)
    except Exception as e:
        print(e)
        print(url)
        if (str(e).endswith("No URI to download.")):
            print(f"No link provided!{args.url}")
            client.send_message(chat_id=int(Telegram_user_id),text=f"No link provided!{args.url}")
            return None

the_download(args.url)
