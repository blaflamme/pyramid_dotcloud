# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.response import Response


def dotcloud_env_view(request):
    env = request.dotcloud_env
    return Response('<h2>DOTCLOUD ENV</h2>{0}'.format(env.__dict__))


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_view(dotcloud_env_view)
    return config.make_wsgi_app()
