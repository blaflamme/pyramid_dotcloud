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
        vars = {'env': self.request.dotcloud_env.__dict__}
        return self.render(
            'pyramid_dotcloud:dotcloud.dbtmako',
            vars,
            self.request
            )


def includeme(config):
    settings = config.registry.settings
    if 'debugtoolbar.panels' in settings:
        settings['debugtoolbar.panels'].append(DotCloudDebugPanel)
        if not 'mako.directories' in settings:
            settings['mako.directories'] = []
