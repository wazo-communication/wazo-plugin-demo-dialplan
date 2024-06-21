#!/usr/bin/env python3
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='wazo-calld-onboarding',
    version='1.0',
    description='Wazo Onboarding Plugin',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    package_data={
        'wazo_calld.plugins': ['*/api.yml'],
    },
    entry_points={
        'wazo_calld.plugins': [
            'onboarding = wazo_onboarding.plugins.plugin:Plugin'
        ],
    },
)
