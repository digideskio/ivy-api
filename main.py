#!/bin/python
# -*- coding: UTF-8 -*-

try: 
    import ujson as json
except:
    import json

import re

try: 
    import newrelic.agent
    newrelic.agent.initialize('config/newrelic.ini')
except:
    print "Newrelic Agent not configured"

######## 
#### Tasks & To-do

# Code like mad

from modules import database

from modules.common import Bunch
from modules.config import FileManager, Config

from logging.handlers import RotatingFileHandler
from flask import Flask, Response, make_response, render_template, request, redirect

####
## Initial setup

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

config = Config(1)
config_dict = config.raw

logHandler = RotatingFileHandler(config.logging['file'], maxBytes=config.logging['size'], backupCount=1) 
logHandler.setLevel(config.logging['level']) # Set logging level. See docs on 'logger' for what the level numbers mean. 
app.logger.addHandler(logHandler) # Add the logger to the Flask instance so we can get errors in a file. Remove if you don't want error logs

###
# Setup and Teardown

from views import generic

####
## API Endpoints

##
# Generic tools Blueprint Registration
#  - This should always be last.
app.register_blueprint(generic.app, url_prefix='/api')


##
# Debug Strings

if __name__ == "__main__":
    app.run(host=config.server['web_ip'],port=config.server['web_port'],debug=True)

