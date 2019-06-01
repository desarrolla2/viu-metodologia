#!/usr/bin/env python3.6
# coding=utf-8

"""
This module show different menus
"""

import os

import repositories.greenhouses
import repositories.orchids
import services.filesystem
import services.information
import services.input
import services.simulator

"""
Retrieve orchid data
"""


def introduce_orchid():
    print('')
    print(' INTRODUCIR LOTE DE ORQUIDEAS')
    print(' ############################')
    print('')
    print(' Introduce:')
    print(' a) identificador del lote')
    orchid_index = services.input.get_index_that_not_is_in_repository(repositories.orchids)

    print(' b) número de plantas')
    number = services.input.get_number()

    print(' c) clima inicial 1 => andes, 2 => costa')
    weather = services.input.get_weather()

    print(' d) número de días de crecimiento en andes')
    days_in_andes = services.input.get_number()

    print(' e) número de días de crecimiento en costa')
    days_in_coast = services.input.get_number()

    repositories.orchids.create(orchid_index, number, weather, days_in_andes, days_in_coast)

    return orchids()


"""
Retrieve greenhouse data
"""


def introduce_greenhouse():
    print('')
    print(' INTRODUCIR INVERNADERO')
    print(' ######################')
    print('')
    print(' Introduce:')
    print(' a) identificador del invernadero')
    greenhouse_index = services.input.get_index_that_not_is_in_repository(repositories.greenhouses)

    print(' b) clima 1 => andes, 2 => costa')
    weather = services.input.get_weather()

    print(' c) capacidad')
    capacity = services.input.get_number()

    repositories.greenhouses.create(greenhouse_index, weather, capacity)

    return greenhouses()


"""
Show wellcome message
"""


def welcome():
    os.system('clear')

    print('')
    print(' UNIVERSIDAD VIU')
    print(' ###############')
    print('')
    print(' Asignatura: Metodología de la programación')
    print(' Alumno: Daniel González Cerviño')
    print('')
    print(' Recuerda:')
    print(' [int] >> quiere decir que el sistema espera un número entero')
    print(' [str] >> quiere decir que el sistema espera una cadena de texto')
    print('')


"""
Show bye message
"""


def good_bye():
    print('')
    print(' Ha sido un placer.')
    return exit(0)


"""
Show orchid menu
"""


def orchids():
    print('')
    print(' 1) Introducir datos de otro lote.')
    print(' 2) Ir al menú principal')
    print('')

    menu = {
        1: introduce_orchid,
        2: main,
    }

    choice = services.input.get_choice(menu.keys())

    return menu[choice]()


"""
Show greenhose menu
"""


def greenhouses():
    print('')
    print(' 1) Introducir datos de otro invernadero.')
    print(' 2) Ir al menú principal.')
    print('')

    menu = {
        1: introduce_greenhouse,
        2: main,
    }

    choice = services.input.get_choice(menu.keys())

    return menu[choice]()


def allocate_orchids():
    services.simulator.allocate_orchids()

    return simulate()


"""
Show simulate days menu
"""


def simulate_days():
    print('')
    print(' SIMULAR')
    print(' #######')
    print('')
    print(' ¿Cuantos días quieres simular?.')
    print('')

    number = services.input.get_number()

    services.simulator.days(number)

    return simulate()


"""
Show simulate menu
"""


def simulate():
    print('')
    print(' SIMULAR')
    print(' #######')
    print('')
    print(' 1) Asignación de lotes.')
    print(' 2) Paso de los días.')
    print(' 3) Ir al menú princial.')
    print('')

    menu = {
        1: allocate_orchids,
        2: simulate_days,
        3: main,
    }

    choice = services.input.get_choice(menu.keys())

    return menu[choice]()


def show():
    services.information.show()
    return main()


"""
Show save data menu
"""


def save():
    print('')
    print(' GUARDAR')
    print(' ######')
    print('')
    print(' Indica el nombre del fichero.')

    services.filesystem.save(services.input.get_string())

    return main()


"""
Show load data menu
"""


def load():
    print('')
    print(' CARGAR')
    print(' ######')
    print('')
    print(' Indica el nombre del fichero.')

    services.filesystem.load(services.input.get_string())
    return main()


"""
Show main menu
"""


def main():
    print('')
    print(' MENÚ PRINCIPAL')
    print(' ##############')
    print('')
    print(' 1) Introducir un lote de orquideas.')
    print(' 2) Introducir datos de un invernadero.')
    print(' 3) Simular.')
    print(' 4) Información del sistema.')
    print(' 5) Guardar datos.')
    print(' 6) Cargar datos.')
    print(' 7) Salir.')
    print('')

    menu = {
        1: introduce_orchid,
        2: introduce_greenhouse,
        3: simulate,
        4: show,
        5: save,
        6: load,
        7: good_bye
    }

    choice = services.input.get_choice(menu.keys())

    return menu[choice]()
