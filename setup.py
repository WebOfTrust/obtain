#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
$ python setup.py register sdist upload

First Time register project on pypi
https://pypi.org/manage/projects/


More secure to use twine to upload
$ pip3 install twine
$ python3 setup.py sdist
$ twine upload dist/obtain-0.0.1.tar.gz


Update sphinx /docs
$ cd /docs
$ sphinx-build -b html source build/html
or
$ sphinx-apidoc -f -o source/ ../src/
$ make html

Best practices for setup.py and requirements.txt
https://caremad.io/posts/2013/07/setup-vs-requirement/
"""


from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup



setup(
    name='obtain',
    version='0.0.1',  #  also change in src/obtain/__init__.py
    license='Apache Software License 2.0',
    description='Securely Attributed Resource Resolver',
    long_description=("Securely Attributed Resource Resolver."),
    author='Samuel M. Smith',
    author_email='smith.samuel.m@gmail.com',
    url='https://github.com/WebOfTrust/obtain',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        # uncomment if you test on these interpreters:
        #'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/WebOfTrust/obtain/issues',
    },
    keywords=[ "secure attribution",
               "authentic data",
               "discovery",
               "resolver",
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.9.5',
    install_requires=[
        'netifaces>=0.10.9',
        'lmdb>=1.2.1',
        'pysodium>=0.7.9',
        'blake3>=0.1.8',
        'msgpack>=1.0.2',
        'simplejson>=3.17.2',
        'cbor2>=5.2.0',
        'multidict>=5.1.0',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    tests_require=[
                    'coverage>=5.5',
                    'pytest>=6.2.4',
                  ],
    setup_requires=[
    ],
    entry_points={
        'console_scripts': [
            'obtain = obtain.cli:main',
            'obtaind = obtain.daemon:main'
        ]
    },
)
