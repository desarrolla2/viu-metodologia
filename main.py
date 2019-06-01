#!/usr/bin/env python3.6
# coding=utf-8

import services.menu as menu
import services.simulator as simulator


def main():
    menu.welcome()
    simulator.load_default_data()
    menu.main()


if __name__ == "__main__":
    main()
