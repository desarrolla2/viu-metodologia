#!/usr/bin/env python3.6
# coding=utf-8

"""
This module allow work with a collection of greenhouses
"""

import entities.greenhouse

greenhouses = {}

"""
Retrieve greenhouse by index
"""


def find_by_index(index):
    for greenhouse in greenhouses:
        if greenhouse.index == index:
            return greenhouse

    return False


# Add greenhouse to collection
def add(current):
    greenhouses.update({current.index: current})


# Retrieve all greenhouses
def find_all():
    return greenhouses


# Clear all greenhouses from collections
def clear():
    greenhouses.clear()


# Create a new greenhouse and add it to collection
def create(index, weather, capacity):
    current = entities.greenhouse.Greenhouse()
    current.index = index
    current.weather = weather
    current.capacity = capacity
    current.available = capacity

    add(current)
