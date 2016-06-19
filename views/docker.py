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

app = Blueprint('docker_bp', __name__)

deep_config = Config(2)
config_dict = deep_config.raw


#proxys docker ps
@app.route('/containers', methods=['GET'])
def containers():

    reply = {'status': True, 'containers': ['test', 'test']}
    return Response(json.dumps(reply), content_type='application/json')

#proxys docker run
@app.route('/create', methods=['POST'])
def create():
    raw = request.get_data()
    req_parse = 'form'

    if raw:
        raw = json.loads(raw)
        req_parse = 'application/json'

    req_type = request.headers.get('Content-Type')

    reply = {'status': True, 'containers': ['test', 'test'], 'request_headers': req_type, 'body': raw}
    return Response(json.dumps(reply), content_type='application/json')

#proxys docker rm & rmi
@app.route('/remove', methods=['POST'])
def create():
    raw = request.get_data()
    req_parse = 'form'

    if raw:
        raw = json.loads(raw)
        req_parse = 'application/json'

    req_type = request.headers.get('Content-Type')

    reply = {'status': True, 'containers': ['test', 'test'], 'request_headers': req_type, 'body': raw}
    return Response(json.dumps(reply), content_type='application/json')
