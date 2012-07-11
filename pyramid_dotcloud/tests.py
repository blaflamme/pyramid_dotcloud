# -*- coding: utf-8 -*-
import os
import unittest

import mock


class TestDotCloudEnv(unittest.TestCase):

    def test_dotcloudenv_init(self):
        from pyramid_dotcloud import DotCloudEnv

        here = os.path.dirname(os.path.abspath(__file__))
        envfile = os.path.join(here, 'test.json')
        env = DotCloudEnv(envfile)
        assert env.key == 'value'

    def test_get_dotcloud_env(self):
        from pyramid_dotcloud import IDotCloudEnv
        from pyramid_dotcloud import get_dotcloud_env

        config = mock.Mock()
        config.registry = mock.Mock()
        queryUtility = mock.Mock()

        config.registry.queryUtility = queryUtility

        env = get_dotcloud_env(config)
        queryUtility.assert_called_with(IDotCloudEnv)

        assert env != None

    def test_get_dotcloud_env_from_request(self):
        from pyramid_dotcloud import IDotCloudEnv
        from pyramid_dotcloud import get_dotcloud_env_from_request

        request = mock.Mock()
        request.registry = mock.Mock()
        queryUtility = mock.Mock()
        request.registry.queryUtility = queryUtility

        env = get_dotcloud_env_from_request(request)
        queryUtility.assert_called_with(IDotCloudEnv)

        assert env != None

    def test_includeme(self):
        from pyramid_dotcloud import includeme
        from pyramid_dotcloud import get_dotcloud_env
        from pyramid_dotcloud import get_dotcloud_env_from_request

        config = mock.Mock()
        add_directive = mock.Mock()
        registerUtility = mock.Mock()
        set_request_property = mock.Mock()

        config.registry = mock.Mock()
        config.registry.registerUtility = registerUtility
        config.add_directive = add_directive
        config.set_request_property = set_request_property

        includeme(config)

        assert add_directive.call_args_list[0][0] == \
            ('get_dotcloud_env', get_dotcloud_env)

        assert set_request_property.call_args_list[0][0] == \
            (get_dotcloud_env_from_request, 'dotcloud_env')
