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

app = Blueprint('generic_bp', __name__)

deep_config = Config(2)
config_dict = deep_config.raw


@app.route('/test', methods=['GET', 'POST'])
def testEcho():
    raw = request.get_data()
    req_parse = 'form'

    if raw:
        raw = json.loads(raw)
        req_parse = 'application/json'

    req_type = request.headers.get('Content-Type')

    reply = {'status': True, 'request_type': req_parse, 'request_headers': req_type, 'body': raw}
    return Response(json.dumps(reply), content_type='application/json')