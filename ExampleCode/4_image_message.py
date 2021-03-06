import configparser
import logging

import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters

# Load data from config.ini file
# config = configparser.ConfigParser()
# config.read('config.ini')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token='5205593719:AAGzPL1MlSJKmCSCVp1Jv6vvAWdjPw_wuA4')


@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        # text = update.message.text.encode('utf-8').decode()
        text = update.message.text
        # for debugging purposes only
        print("got text message :", text)
        if text == "/start":
            # print the welcoming message
            bot_welcome = """
            ๐้ปๆๅฟซ้ไธญๆๅ
๐๐ปhttps://t.me/setlanguage/zh-hant-beta

๐ดๆจๆญ้ๆผ้ ป็นๅฏ้้้็ฅใ

๐ๅไบซ้ๅๆธฌ่ฉฆๆฉๅจไบบ๐
https://t.me/Python0224testbot
            """
            # send the welcoming message
            bot.sendMessage(chat_id=chat_id, text=bot_welcome)
            # bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
        else:
            # ็ผ้ๅ็
            # ็ดๆฅ็ผ้็ถฒๅ
            # bot.sendPhoto(chat_id=chat_id, photo='https://buzzorange.com/techorange/wp-content/uploads/sites/2/2021/02/49033597737_8686b9b9d9_b20210220-1024x576.jpg')
            # ่ฎๅๆฌๆฉๅ็
            bot.sendPhoto(chat_id=chat_id, photo=open("./images/dogecoin.jpg", 'rb'))

        # Update dispatcher process that handler to process this message
        # dispatcher.process_update(update)
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='127.0.0.1', port=5000, debug=True)