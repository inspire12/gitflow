# -*- coding: utf-8 -*-

# This file is part of `gitflow`.
# Copyright (c) 2015 Christian Assing
# Distributed under a BSD-like license. For full terms see the file LICENSE.txt
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from fabric.api import task, local


@task
def build():
    local("rm -rf dist; python setup.py sdist bdist_wheel")


@task
def publish():
    local("twine upload dist/*")
