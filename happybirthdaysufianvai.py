#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# Happy Birthday
# Bulls Eye: https://github.com/BullsEye0
# Created May, 20 2019
# Copyright (c) 2019 Jolanda de Koff, Bulls Eye.

import random
import time


banner1 = """

\033[1;31m
╔╗─╔╗─────────────╔══╗───╔╗╔╗───╔╗
║║─║║─────────────║╔╗║──╔╝╚╣║───║║
║╚═╝╠══╦══╦══╦╗─╔╗║╚╝╚╦╦╩╗╔╣╚═╦═╝╠══╦╗─╔╗
║╔═╗║╔╗║╔╗║╔╗║║─║║║╔═╗╠╣╔╣║║╔╗║╔╗║╔╗║║─║║
║║─║║╔╗║╚╝║╚╝║╚═╝║║╚═╝║║║║╚╣║║║╚╝║╔╗║╚═╝║
╚╝─╚╩╝╚╣╔═╣╔═╩═╗╔╝╚═══╩╩╝╚═╩╝╚╩══╩╝╚╩═╗╔╝
───────║║─║║─╔═╝║───────────────────╔═╝║
───────╚╝─╚╝─╚══╝───────────────────╚══╝
╔═══╦╗─╔╦═══╦══╦═══╦═╗─╔╗╔╗──╔╦═══╦══╗
║╔═╗║║─║║╔══╩╣╠╣╔═╗║║╚╗║║║╚╗╔╝║╔═╗╠╣╠╝
║╚══╣║─║║╚══╗║║║║─║║╔╗╚╝║╚╗║║╔╣║─║║║║
╚══╗║║─║║╔══╝║║║╚═╝║║╚╗║║─║╚╝║║╚═╝║║║
║╚═╝║╚═╝║║──╔╣╠╣╔═╗║║─║║║─╚╗╔╝║╔═╗╠╣╠╗
╚═══╩═══╩╝──╚══╩╝─╚╩╝─╚═╝──╚╝─╚╝─╚╩══╝                         ▀

\033[1;m

        Happy Birthday SUFIAN VAI

    From- MD FUAD HASAN AKIL... *** :)

        """

banner2 = """

\033[1;31m

╔╗─╔╗─────────────╔══╗───╔╗╔╗───╔╗
║║─║║─────────────║╔╗║──╔╝╚╣║───║║
║╚═╝╠══╦══╦══╦╗─╔╗║╚╝╚╦╦╩╗╔╣╚═╦═╝╠══╦╗─╔╗
║╔═╗║╔╗║╔╗║╔╗║║─║║║╔═╗╠╣╔╣║║╔╗║╔╗║╔╗║║─║║
║║─║║╔╗║╚╝║╚╝║╚═╝║║╚═╝║║║║╚╣║║║╚╝║╔╗║╚═╝║
╚╝─╚╩╝╚╣╔═╣╔═╩═╗╔╝╚═══╩╩╝╚═╩╝╚╩══╩╝╚╩═╗╔╝
───────║║─║║─╔═╝║───────────────────╔═╝║
───────╚╝─╚╝─╚══╝───────────────────╚══╝
╔═══╦╗─╔╦═══╦══╦═══╦═╗─╔╗╔╗──╔╦═══╦══╗
║╔═╗║║─║║╔══╩╣╠╣╔═╗║║╚╗║║║╚╗╔╝║╔═╗╠╣╠╝
║╚══╣║─║║╚══╗║║║║─║║╔╗╚╝║╚╗║║╔╣║─║║║║
╚══╗║║─║║╔══╝║║║╚═╝║║╚╗║║─║╚╝║║╚═╝║║║
║╚═╝║╚═╝║║──╔╣╠╣╔═╗║║─║║║─╚╗╔╝║╔═╗╠╣╠╗
╚═══╩═══╩╝──╚══╩╝─╚╩╝─╚═╝──╚╝─╚╝─╚╩══╝                         ▀

\033[1;m

        Happy Birthday SUFIAN VAI

    From- MD FUAD HASAN AKIL... *** :)

        """

stream = (banner1, banner2)

print random.choice(stream)
time.sleep(1)


def happy_birthday():

    first_name = raw_input("\n[+] Kemon lagtese?: ")
    print "\n"

    happy = "Happy Birthday SUFIAN VAI.."

    print "###########################################"
    print "\t" + "Happy Birthday SUFIAN VAI" 
    print "###########################################\n"
    time.sleep(2)

    for x in range(2):
        print(happy)
        time.sleep(2)
        print(happy)
        time.sleep(1.5)

        print "Happy Birthday SUFIAN VAI"
        time.sleep(1)
        print(happy) + "\n"
        time.sleep(1)

        for x in range(3):
            print "Allah apnake susto rakuk hayat dan koruk.!\n"
            time.sleep(1)

    print "\t###########################################"
    print "\t\tHappy Birthday SUFIAN VAI"
    print "\t\Enjoy :) "
    print "\t###########################################\n"


happy_birthday()
