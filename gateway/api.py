from typing import Dict, Any

from flask import Flask, abort, Blueprint
from pyrogram import Client


class Meta:
    app: Blueprint = Blueprint('api_gateway', __name__)
    client: Client = None


meta_info = Meta()
api = meta_info.app


@api.route('/')
def index():
    try:
        me: Client = meta_info.client
        print(f'{me.get_me()}')
        return '.', 200
    except Exception as e:
        print(e)
        abort(404)
