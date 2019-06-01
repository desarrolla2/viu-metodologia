#!/usr/bin/env python3.6
# coding=utf-8

import repositories.greenhouses
import repositories.orchids
import repositories.weathers

current_day = 0


def days(number):
    global current_day
    for day in range(0, number):
        current_day += 1
        print('')
        print('')
        print(' simulando el día %d' % current_day)
        print(' --------------------')

        allocate_orchids()
        print(' - comienza la simulación del día.')
        orchids = repositories.orchids.find_all()
        for orchid in orchids.values():
            if orchid.greenhouse.weather == 1:
                orchid.days_in_andes -= 1
                greenhouse = orchid.greenhouse
                print('    * el lote "%s" se encuentra en "andes", días restantes %d' % (
                    orchid.index, orchid.days_in_andes))
                if orchid.days_in_andes <= 0:
                    greenhouse.remove_orchid(orchid)
                    print('      > el lote ha sido retirado del invernadero.')
                    print('      > el invernadero "%s" se encuentra al %d/%d capacidad.' %
                          (greenhouse.index, greenhouse.available, greenhouse.capacity))
                    continue

            if orchid.greenhouse.weather == 2:
                orchid.days_in_coast -= 1
                greenhouse = orchid.greenhouse
                print('    * el lote "%s" se encuentra en "costa", días restantes %d' % (
                    orchid.index, orchid.days_in_coast))
                if orchid.days_in_coast <= 0:
                    orchid.greenhouse.remove_orchid(orchid)
                    print('      > el lote ha sido retirado del invernadero.')
                    print('      > el invernadero "%s" se encuentra al %d/%d capacidad.' %
                          (greenhouse.index, greenhouse.available, greenhouse.capacity))

        print(' - finaliza la simulación del día.')


def allocate_orchids():
    orchids_assigned = 0
    orchids = repositories.orchids.find_all()
    to_destroy = {}
    to_shell = {}
    print(' - comienza la asignación de lotes.')
    for orchid in orchids.values():
        print('    * evalundo el lote "%s"' % orchid.index)
        print('      > clima preferido "%s", días restantes en los andes "%d", días restantes en la costa "%d"' %
              (repositories.weathers.get_name(orchid.weather), orchid.days_in_andes, orchid.days_in_coast))

        if orchid.greenhouse:
            print('      > el lote ya tiene invernadero asignado.')
            continue

        allocate_orchid(orchid)
        orchids_assigned += 1

        if not orchid.greenhouse:
            if orchid.get_days() == 0:
                print('    * el lote está listo, así que será vendido.')
                to_shell.update({orchid.index: orchid})
            else:
                print('    * el lote no se puede asignar así que será destruido.')
                to_destroy.update({orchid.index: orchid})

    if orchids_assigned == 0:
        print(' - no hay lotes pendientes de asignar.')
        return

    for orchid in to_shell.values():
        repositories.orchids.sell(orchid)

    for orchid in to_destroy.values():
        repositories.orchids.destroy(orchid)

    print(' - asignados %d lotes.' % orchids_assigned)
    print('')


def allocate_orchid(orchid):
    if orchid.greenhouse:
        return True

    greenhouses = repositories.greenhouses.find_all()
    for greenhouse in greenhouses.values():
        print('      > evaluando el invernadero "%s", clima "%s".' %
              (greenhouse.index, repositories.weathers.get_name(greenhouse.weather)))
        if greenhouse.weather == orchid.weather and orchid.get_days_by_weather(greenhouse.weather) > 0:
            print('        + el clima del invernadero es correcto.')
            if greenhouse.has_availability(orchid):
                greenhouse.add_orchid(orchid)
                print('        + lote asignado. El invernadero se encuenta al %d/%d de su capacidad.' % (
                    greenhouse.available, greenhouse.capacity))
                return True
            print('        + el invernadero no tiene disponibilidad.')

    for greenhouse in greenhouses.values():
        if orchid.get_days_by_weather(greenhouse.weather) > 0:
            print('        + el clima del invernadero no es el correcto.')
            if greenhouse.has_availability(orchid):
                greenhouse.add_orchid(orchid)
                print('        + lote asignado. El invernadero se encuenta al %d/%d de su capacidad.' % (
                    greenhouse.available, greenhouse.capacity))
                return True

    print('      > no se ha podido asignar el lote.')
    return False


"""
This method is for testing purposes
"""


def load_default_data():
    repositories.orchids.clear()
    # index, number, weather, days_in_andes, days_in_coast
    # repositories.orchids.create('1_1_1_1', 1, 1, 1, 1)
    # repositories.orchids.create('1_2_1_1', 1, 2, 1, 1)
    # repositories.orchids.create('1_2_1_1_b', 1, 2, 1, 1)
    # repositories.orchids.create(2, 1, 1, 1, 1)
    # repositories.orchids.create(3, 1, 2, 1, 1)
    # repositories.orchids.create(4, 1, 2, 1, 1)
    # repositories.orchids.create(5, 1, 1, 1, 1)

    # index, weather, capacity
    # repositories.greenhouses.clear()
    # repositories.greenhouses.create('andes_1', 1, 1)
    # repositories.greenhouses.create('costa_1', 2, 1)
    # repositories.greenhouses.create(20, 2, 10)
    # repositories.greenhouses.create(3, 1, 1)
