import sys

from setuptools import setup, find_packages

setup(
    metadata_version    = '0.1',
    name                = 'pgshapely',
    version             = '0.1.0',
    description         = 'shapely geometry type integration with psycopg2 & PostGIS',
    author              = 'Josh Hansen',
    author_email        = 'josh@skwash.net',
    maintainer          = 'Josh Hansen',
    maintainer_email    = 'josh@skwash.net',
    packages            = ['pgshapely'],
    install_requires    = ['shapely>=1.2.0','psycopg2>=2.0.0'],
    platforms           = 'Posix; Mac OS X',
    url                 = 'http://www.github.com/skwash/pgshapely',
    test_suite          = 'pgshapelys.tests.test_suite'
)

