# -*- coding: utf-8 -*-
import json
import os
from zope.interface import Interface

DOTCLOUD_FILE_PATH = '/home/dotcloud/environment.json'


class IDotCloudEnv(Interface):
    pass


class DotCloudEnv(object):
    """DotCloud environment for Pyramid"""
    def __init__(self, path=DOTCLOUD_FILE_PATH):
        if os.path.isfile(path):
            with open(path) as f:
                env = json.load(f)
                for item in env:
                    setattr(self, item, env[item])


def get_dotcloud_env(config):
    return config.registry.queryUtility(IDotCloudEnv)


def get_dotcloud_env_from_request(request):
    """Obtain a DotCloudEnv object previously registered via
    ``config.include('pyramid_dotcloud')``
    """
    return request.registry.queryUtility(IDotCloudEnv)


def includeme(config):
    config.registry.registerUtility(DotCloudEnv(), IDotCloudEnv)
    config.add_directive('get_dotcloud_env', get_dotcloud_env)
    config.set_request_property(
        get_dotcloud_env_from_request,
        'dotcloud_env',
        reify=True
        )
    config.include('.panel')