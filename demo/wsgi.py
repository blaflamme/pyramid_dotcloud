# -*- coding: utf-8 -*-
import os.path
from pyramid.paster import get_app
from paste.script.util.logging_config import fileConfig


here = os.path.dirname(os.path.abspath(__file__))
conf = os.path.join(here, 'dotcloud.ini')
fileConfig(conf)

application = get_app(conf, 'main')
