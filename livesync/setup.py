# This file is part of the Indico plugins.
# Copyright (C) 2002 - 2021 CERN
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from setuptools import find_packages, setup


setup(
    name='indico-plugin-livesync',
    version='3.0-dev',
    description='Framework for pushing Indico event data to external services',
    url='https://github.com/indico/indico-plugins',
    license='MIT',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['indico>=3.0.dev0'],
    python_requires='~=3.9',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    entry_points={'indico.plugins': {'livesync = indico_livesync.plugin:LiveSyncPlugin'}}
)
