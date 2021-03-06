from setuptools import setup, find_packages
import os
import re
from mycluster.version import get_git_version


classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Logging
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.6
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.2
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: POSIX :: Linux
"""
classifiers = [s.strip() for s in classes.split('\n') if s]


setup(
    name='ParaViewConnect',
    version=get_git_version(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    license='BSD',
    author='Zenotech',
    author_email='admin@zenotech.com',
    url='https://github.com/zenotech/ParaViewConnect',
    classifiers=classifiers,
    description='Library to help starting and connecting to remote ParaView servers',
    long_description=open('README.md').read(),
    install_requires=['fabric'],
    scripts=['scripts/mycluster'],
    include_package_data=True,
    package_data = {
        '': ['*.md','RELEASE-VERSION']
    },
    data_files = [('share/ParaViewConnect', ['RELEASE-VERSION']),
                  ('share/ParaViewConnect', ['share/mycluster-OF-simpleFoam.bsh',
                                       'share/mycluster-fluent.bsh',
                                       'share/mycluster-zcfd.bsh',
                                       'share/mycluster-paraview.bsh']),
                  ],
)
