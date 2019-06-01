#!/usr/bin/env python3.6
# coding=utf-8

import entities.orchid

orchids = {}
destroyed = []
sold = []


def count_sold():
    return len(sold)


def count_destroyed():
    return len(destroyed)


def add(current):
    orchids.update({current.index: current})


def find_all():
    return orchids


def clear():
    orchids.clear()
    destroyed.clear()
    sold.clear()


def sell(current):
    greenhouse = current.greenhouse
    if greenhouse:
        greenhouse.orchids.pop(current.index)

    current.greenhouse = False
    orchids.pop(current.index)
    sold.append(current)


def destroy(current):
    greenhouse = current.greenhouse
    if greenhouse:
        greenhouse.orchids.pop(current.index)

    current.greenhouse = False
    orchids.pop(current.index)
    destroyed.append(current)


def create(index, number, weather, days_in_andes, days_in_coast, original_days_in_andes=False,
           original_days_in_coast=False):
    current = entities.orchid.Orchid()
    current.index = index
    current.number = number
    current.weather = weather
    current.days_in_andes = days_in_andes
    current.days_in_coast = days_in_coast

    current.original_days_in_andes = original_days_in_andes
    current.original_days_in_coast = original_days_in_coast

    if not original_days_in_andes:
        current.original_days_in_andes = days_in_andes

    if not original_days_in_coast:
        current.original_days_in_coast = days_in_coast

    add(current)

    return current
