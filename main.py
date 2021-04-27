from typing import Dict, List, Any

import toml
from os import path
from pyrogram import Client, idle
from flask import Flask

from threading import Thread

from gateway.api import api, meta_info


# Set telegram client varibles for auth
config = toml.load('./config.toml') \
    if path.exists('./config.toml') \
    else exit('Please set ./config.toml')

api_id = config['telegram_client']['api_id']
api_hash = config['telegram_client']['api_hash']


# verify if session exists
logged = True if path.exists('./session.session') \
    else False

# clients
clients: Dict[str, Client] = dict()

# API Gateway App
gateway = Flask(__name__)


def main():

    # Register Blueprints
    gateway.register_blueprint(api)

    # Initialize telegram session
    clients['main'] = Client(config['sessions']['main'], api_id=api_id, api_hash=api_hash)
    main_account = clients['main']

    # share information
    meta_info.client = main_account

    # run client
    main_account.start()
    # run api gateway in background
    Thread(target=gateway.run, daemon=True).start()

    # wait client actions
    idle()

    # when done, stop client
    main_account.stop()


if __name__ == '__main__':
    main()
