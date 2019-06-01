#!/usr/bin/env python3.6
# coding=utf-8

import repositories.weathers

"""
This entity represents a orchid batch
"""


class Orchid:
    """
    Constructor
    """

    def __init__(self):
        self.index = 0
        self.number = 0
        self.weather = 0
        self.original_days_in_andes = 0
        self.days_in_andes = 0
        self.original_days_in_coast = 0
        self.days_in_coast = 0
        self.greenhouse = False

    """
    Retrieve the number of remaining days by weather
    """

    def get_days_by_weather(self, weather):
        if weather == 1:
            return self.days_in_andes

        if weather == 2:
            return self.days_in_coast

        return 0

    """
    Retrieve the number of remaining days
    """

    def get_days(self):
        return self.days_in_andes + self.days_in_coast;

    """
    Show main greenhouse info, useful for depuration
    """

    def info(self):
        greenhouse_index = 'not assigned'
        if self.greenhouse:
            greenhouse_index = self.greenhouse.index
        print('   - orchid id: "%s", greenhouse: "%s", weather: "%s" días en andes %d/%d, días en costa %d/%d' % (
            self.index, greenhouse_index, repositories.weathers.get_name(self.weather), self.days_in_andes,
            self.original_days_in_andes,
            self.days_in_coast, self.original_days_in_coast))
