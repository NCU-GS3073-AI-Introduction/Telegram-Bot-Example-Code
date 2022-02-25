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
        print(update)
        chat_id = update.message.chat.id
        user_firstname = update.message.chat.first_name
        user_lastname = update.message.chat.last_name
        msg = update.message.text
        msg_id = update.message.message_id
        print(msg)
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='127.0.0.1', port=5000, debug=True)