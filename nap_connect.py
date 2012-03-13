#!/usr/bin/python

## From http://wiki.openmoko.org/wiki/Manually_using_Bluetooth#Connection_establishing

import dbus
import sys
import os
import time
import ConfigParser
import logging
import string

config = ConfigParser.RawConfigParser()
config.read('nap_connect.cfg')
debug = config.getboolean('global', 'debug')
my_mac = config.get('global','my_mac')
nap_mac = config.get('global','nap_mac')
LOGFILE = config.get('global', 'logfile')

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

if debug == 0: logging.basicConfig(filename=LOGFILE,level=logging.INFO)
if debug == 1: logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)

logging.info('Starting nap_connect.py')
logging.info('INFO MODE')
logging.debug('DEBUG MODE')

logging.info('About to connect from %s to %s' % (my_mac, nap_mac))

bus = dbus.SystemBus()
manager = dbus.Interface(bus.get_object("org.bluez", "/"), "org.bluez.Manager")
adapter = dbus.Interface(bus.get_object("org.bluez", manager.DefaultAdapter()), "org.bluez.Adapter")

logging.debug("Connecting to " + adapter.FindDevice(nap_mac))

network = dbus.Interface(bus.get_object("org.bluez", adapter.FindDevice(nap_mac)), "org.bluez.Network")

print "About to try connecting"
network.Connect("NAP")
print "Networking established."
time.sleep(60)
network.Disconnect()
