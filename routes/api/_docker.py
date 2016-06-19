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

config = Config(depth=3)
config_dict = config.raw
cli = Client(base_url=config.api['docker']['socketURL'])


#proxys docker ps
@app.route('/containers', methods=['GET'])
def containers():
    reply = cli.containers()
    return Response(json.dumps(reply), content_type='application/json')

@app.route('/container', methods=['POST'])
@app.route('/container/<string:container_id>', methods=['GET', 'REMOVE', 'PUT'])
def container(container_id=None):
    if request.method == 'POST':
        print 'POST REQUEST'
        #Create container logic
    elif request.method == 'PUT':
        print 'PUT REQUEST'
        #Update container logic
    elif request.method == 'REMOVE':
        #Remove container logic
        print 'REMOVE REQUEST'

    print 'GET REQUEST'
