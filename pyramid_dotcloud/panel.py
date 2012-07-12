from operator import itemgetter

from pyramid_debugtoolbar.panels import DebugPanel

_ = lambda x: x


class DotCloudDebugPanel(DebugPanel):
    """
    DotCloud debug panel
    """
    name = 'DotCloud'
    has_content = True

    def nav_title(self):
        return _('DotCloud')

    def url(self):
        return ''

    def title(self):
        return _('DotCloud')

    def content(self):
        env = [(k, v) for k, v in vars(self.request.dotcloud_env).iteritems()]
        return self.render(
            'pyramid_dotcloud:dotcloud.dbtmako',
            {'env': sorted(env, key=itemgetter(0))},
            self.request
            )


def includeme(config):
    settings = config.registry.settings
    if 'debugtoolbar.panels' in settings:
        settings['debugtoolbar.panels'].append(DotCloudDebugPanel)
        if not 'mako.directories' in settings:
            settings['mako.directories'] = []
