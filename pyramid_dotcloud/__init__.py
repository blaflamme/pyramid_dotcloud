# -*- coding: utf-8 -*-
import json
import os
from zope.interface import Interface

DOTCLOUD_FILE_PATH = '/home/dotcloud/environment.json'


class IDotCloudEnv(Interface):
    pass


class DotCloudEnv(object):
    """DotCloud environment for Pyramid"""
    def __init__(self):
        if os.path.isfile(DOTCLOUD_FILE_PATH):
            with open(DOTCLOUD_FILE_PATH) as f:
                self.env = json.load(f)
                for item in self.env:
                    self.setattr(item, self.env[item])


def get_dotcloud_env(config):
    return config.registry.getUtility(IDotCloudEnv)


def get_dotcloud_env_from_request(request):
    """Obtain a DotCloudEnv object previously registered via
    ``config.include('pyramid_dotcloud')``
    """
    return request.registry.getUtility(IDotCloudEnv)


def includeme(config):
    config.registry.registerUtility(DotCloudEnv(), IDotCloudEnv)
    config.add_directive('get_dotcloud_env', get_dotcloud_env)
    config.set_request_property(
        get_dotcloud_env_from_request,
        'dotcloud_env',
        reify=True
        )