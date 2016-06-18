# -*- coding: UTF-8 -*-

import re
import json
import time
import copy
import random
import requests

import uuid as uuidgen

from modules import database
from modules.pooling import rdis
from modules.common import Bunch, sanitize, upsert
from modules.config import FileManager, Config

from datetime import datetime, timedelta
from huey import RedisHuey, crontab

c = Config(2)

huey = RedisHuey(c.db.redis['db_name'], host=c.db.redis['db_host'], port=c.db.redis['db_port'])

class Trigger(object):
    def __init__(self):
        pass

    @huey.task()
    def echo(msg):
        print msg


class Automatic(object):
    def __init__(self):
        pass

    @huey.periodic_task(crontab(minute=1))
    def autoEcho():
        print datetime.now()