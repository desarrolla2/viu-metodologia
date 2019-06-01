# !/usr/bin/env python3.6
# coding=utf-8
"""
This module show current state of data
"""

import repositories.greenhouses
import repositories.orchids

"""
Show current state of data
"""


def show():
    orchids = repositories.orchids.find_all()
    greenhouses = repositories.greenhouses.find_all()

    print('')
    print(' INFORMACIÓN')
    print(' ###########')
    print('')
    print(' %d lotes de orquideas.' % (len(orchids)))
    print(' %d invernaderos.' % (len(greenhouses)))
    print('')
    print(' 1) Lotes de orquideas sin invernadero:')
    print('')
    orchids_without_greenhouse = 0
    for orchid in orchids.values():
        if orchid.greenhouse:
            continue
        print(' - lote: "%s".' % orchid.index)
        orchids_without_greenhouse += 1
    if orchids_without_greenhouse == 0:
        print(' no hay lotes sin invernadero.')

    print('')
    print(' 2) Lotes de orquideas por invernadero:')

    for greenhouse in greenhouses.values():
        print('')
        print(' - invernadero "%s":' % greenhouse.index)
        greenhouse_orchids = 0
        for orchid in greenhouse.orchids.values():
            print('  - lote: "%s".' % orchid.index)
            greenhouse_orchids += 1

        if greenhouse_orchids == 0:
            print(' no tiene lotes.')

    print('')
    print(' 3) Lotes de orquideas vendidos:')
    print('')

    count = repositories.orchids.count_sold()
    if count == 0:
        print(' no se ha vendido ningún lote.')
    else:
        print(' %d lotes de orquideas.' % count)

    print('')
    print(' 4) Lotes de orquideas destruidos:')
    print('')

    count = repositories.orchids.count_destroyed()
    if count == 0:
        print(' no se ha destruido ningún lote.')
    else:
        print(' %d lotes de orquideas.' % count)
