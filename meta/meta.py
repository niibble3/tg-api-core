from flask import Blueprint
from flask_restful import Api
from pyrogram import Client


import toml
from os import path

# Set telegram client varibles for auth
config = toml.load('./config.toml') \
    if path.exists('./config.toml') \
    else exit('Please set ./config.toml')

api_id = config['telegram_client']['api_id']
api_hash = config['telegram_client']['api_hash']


class Meta:
    app: Blueprint = Blueprint('api_gateway', __name__)
    api: Api = Api(app)
    client: Client = Client(config['sessions']['main'], api_id=api_id, api_hash=api_hash)


# initialize variable
MetaInfo = Meta()
