import unittest
import mock

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_dotcloud_env_view(self):
        from . import dotcloud_env_view
        request = testing.DummyRequest()
        request.dotcloud_env = mock.Mock()
        info = dotcloud_env_view(request)
        assert info.body.startswith('<html><body><h2>DOTCLOUD ENV</h2>')

    def test_main(self):
        from pyramid.router import Router
        from . import main
        app = main({})
        assert isinstance(app, Router)
