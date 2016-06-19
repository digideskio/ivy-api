import re
import time

try:
    import ujson as json
except:
    import json

from modules import database
from modules.common import Bunch
from modules.config import FileManager, Config
from flask import Blueprint, Response, make_response, render_template, request, redirect

from engine.default import Trigger
from docker import Client

app = Blueprint('docker_bp', __name__)

deep_config = Config(2)
config_dict = deep_config.raw
cli = Client(base_url='tcp://192.168.46.130:2375')


#proxys docker ps
@app.route('/containers', methods=['GET'])
def containers():
    reply = cli.containers()
    return Response(json.dumps(reply), content_type='application/json')

@app.route('/container', methods=['POST'])
@app.route('/container/<string:container_id>', methods=['GET', 'REMOVE', 'PUT'])
def container(container_id=None):
    if request.method == 'POST':
        #Create container logic

    elif request.method == 'PUT':
        #Update container logic

    elif request.method == 'REMOVE':
        #Remove container logic

    #return info for container ID, logs etc
