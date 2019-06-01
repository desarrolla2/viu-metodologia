#!/usr/bin/env python3.6
# coding=utf-8

"""
This module handle with data retrieved from user
"""

import repositories.weathers

"""
Show invalid option message
"""


def was_invalid():
    print(' opción no válida, intentalo de nuevo')


"""
Retrieve a valid string from input
"""


def get_string():
    try:
        value = str(input(" [str] >> "))
        print(' > "%s"' % value)
        return value
    except:
        was_invalid()

    return get_string()


"""
Retrieve a valid number from input
"""


def get_number():
    try:
        value = int(input(" [int] >> "))
        print(' > %d' % value)
        return value
    except:
        was_invalid()

    return get_number()


"""
Retrieve a valid weather from input
"""


def get_weather():
    number = get_number()
    weathers = repositories.weathers.find_all()
    if number not in weathers:
        was_invalid()
        return get_weather()

    return number


def get_choice(choices):
    number = get_number()
    if number not in choices:
        was_invalid()
        return get_choice(choices)

    return number


def get_index_that_not_is_in_repository(repository):
    orchid_index = get_string()
    if orchid_index in repository.find_all():
        print(' El indentificador ya existe, introduce otro identificador.')
        return get_index_that_not_is_in_repository(repository)

    return orchid_index
