import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'zope.interface']

setup(name='pyramid_dotcloud',
      version='0.1',
      description='pyramid_dotcloud',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Blaise Laflamme',
      author_email='blaise@kemeneur.com',
      url='http://github.com/blaflamme/pyramid_dotcloud',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_dotcloud',
      install_requires=requires,
      test_requires=['mock', 'nose', 'coverage'],
      paster_plugins=['pyramid'],
      )
