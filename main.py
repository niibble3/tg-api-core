from typing import Dict, List, Any

from os import path
from pyrogram import Client, idle
from flask import Flask

from threading import Thread

from meta.meta import MetaInfo
from gateway.user_controller import GetMe


# verify if session exists
logged = True if path.exists('./session.session') \
    else False

# clients
clients: Dict[str, Client] = dict()

# API Gateway App
gateway = Flask(__name__)


def main():

    # Register Gateway Resources
    MetaInfo.api.add_resource(GetMe, '/me')

    # Register Blueprints
    gateway.register_blueprint(MetaInfo.app)

    # Initialize telegram session
    clients['main'] = MetaInfo.client
    main_account = clients['main']

    # share information
    MetaInfo.client = main_account

    # run client
    MetaInfo.client.start()
    # run api gateway in background
    Thread(target=gateway.run, daemon=True).start()

    # wait client actions
    idle()

    # when done, stop client
    MetaInfo.client.stop()


if __name__ == '__main__':
    main()