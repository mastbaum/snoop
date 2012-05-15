from setuptools import setup

setup(
    name = 'snoop',
    version = '0.7',
    description = 'sno(plus) online processing',
    author = 'Andy Mastbaum',
    author_email = 'mastbaum@hep.upenn.com',
    url = 'http://github.com/mastbaum/snoop',
    packages = ['snoop'],
    scripts = ['bin/snoop'],
    install_requires = ['python-daemon', 'lockfile']
)

