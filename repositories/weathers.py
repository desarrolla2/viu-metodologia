#!/usr/bin/env python3.6
# coding=utf-8

"""
This module allow to work with weathers
"""

availables = {1: 'andes', 2: 'costa'}

"""
Retrieve weather name
"""


def get_name(weather):
    if weather in availables:
        return availables[weather]

    raise Exception('weather "%s" not exist' % weather)


"""
Retrieve all weathers
"""


def find_all():
    return availables
