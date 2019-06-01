# !/usr/bin/env python3.6
# coding=utf-8

"""
This module allow to work with filesystem
"""

import json

import repositories.greenhouses
import repositories.orchids
import services.simulator

"""
Save greenhouses and orchids data to filename
"""


def save(filename):
    filename = 'data/%s.json' % filename
    orchids = {}
    greenhouses = {}

    for greenhouse in repositories.greenhouses.find_all().values():
        greenhouses.update({greenhouse.index: {
            'index': greenhouse.index,
            'weather': greenhouse.weather,
            'capacity': greenhouse.capacity,
            'available': greenhouse.available,
        }})

    for orchid in repositories.orchids.find_all().values():
        greenhouse_index = False
        if orchid.greenhouse:
            greenhouse_index = orchid.greenhouse.index

        orchids.update({orchid.index: {
            'index': orchid.index,
            'number': orchid.number,
            'weather': orchid.weather,
            'original_days_in_andes': orchid.original_days_in_andes,
            'days_in_andes': orchid.days_in_andes,
            'original_days_in_coast': orchid.original_days_in_coast,
            'days_in_coast': orchid.days_in_coast,
            'greenhouse_index': greenhouse_index
        }})

    open(filename, 'w+')
    try:
        with open(filename, 'w+') as fp:
            json.dump({'greenhouses': greenhouses, 'orchids': orchids, 'current_day': services.simulator.current_day},
                      fp)
    except:
        print(' [ERROR]: ha ocurrido un error al guardar los datos')
        return

    print('')
    print(' Los datos han sido guardados.')


"""
Load greenhouses and orchids data from filename
"""


def load(filename):
    filename = 'data/%s.json' % filename
    services.simulator.current_day = 0
    repositories.orchids.clear()
    repositories.greenhouses.clear()

    try:
        with open(filename, 'r') as fp:
            data = json.load(fp)
    except:
        print(' [ERROR]: ha ocurrido un error al leer los datos')
        return

    try:
        services.simulator.current_day = data['current_day']
        for item in data['greenhouses'].values():
            repositories.greenhouses.create(item['index'], item['weather'], item['capacity'])

        for item in data['orchids'].values():
            orchid = repositories.orchids.create(
                item['index'], item['number'], item['weather'], item['days_in_andes'],
                item['days_in_coast'], item['original_days_in_andes'],
                item['original_days_in_coast'])

            greenhouse = repositories.greenhouses.find_by_index(item['greenhouse_index'])
            if greenhouse:
                greenhouse.add_orchid(orchid)

    except:
        print(' [ERROR]: ha ocurrido un error al leer los datos')
        return

    print('')
    print(' Los datos han sido cargados.')
