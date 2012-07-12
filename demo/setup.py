import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'pyramid',
    'waitress',
    'PasteScript'
    ]

setup(name='dotcloud_demo',
      version='0.0',
      description='A demo application for pyramid_dotcloud',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: Repoze Public License",
        ],
      keywords='web wsgi pylons pyramid',
      author="Blaise Laflamme",
      author_email="blaise@kemeneur.com",
      url="http://pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      py_modules=['demo'],
      entry_points="""\
      [paste.app_factory]
      main = demo:main
      """,
      )
