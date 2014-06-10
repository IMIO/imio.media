# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('CHANGES.rst')

setup(
    name='imio.media',
    version='0.1.4.dev0',
    description="This package is used to view video from links. You can add video or photo from a link which accept oembeded protocol. This package has as dependecy collective.oembeded.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='Benoît Suttor',
    author_email='benoit.suttor@imio.be',
    url='http://pypi.python.org/pypi/imio.media',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imio'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'collective.oembed',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
