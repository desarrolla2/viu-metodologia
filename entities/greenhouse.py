#!/usr/bin/env python3.6
# coding=utf-8

"""
This entity represents a greenhouse
"""

import repositories.weathers


class Greenhouse:
    """
    Constructor
    """

    def __init__(self):
        self.index = 0
        self.weather = 0
        self.capacity = 0
        self.available = 0
        self.orchids = {}

    """
    Show if greenhouse has availability for a orchid bach
    """

    def has_availability(self, orchid):
        if self.available >= orchid.number:
            return True
        return False

    """
    Add orchid bach to greenhouse and update internal data.
    """

    def add_orchid(self, orchid):
        orchid.greenhouse = self

        self.orchids.update({orchid.index: orchid})
        self.available -= orchid.number

    """
    Remove orchid bach from greenhouse and update internal data.
    """

    def remove_orchid(self, orchid):
        orchid.greenhouse = False

        self.orchids.pop(orchid.index)
        self.available += orchid.number

    """
    Show main greenhouse info, useful for depuration
    """

    def info(self):
        print('   - greenhose id: "%s", weather: "%s", capacity: %d/%d, lotes: %d' % (
            self.index, repositories.weathers.get_name(self.weather), self.available, self.capacity, len(self.orchids)))
