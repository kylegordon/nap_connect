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

logging.info('Starting cartracker')
logging.info('INFO MODE')
logging.debug('DEBUG MODE')

logging.info('About to connect from %s to %s' % (my_mac, nap_mac))


## Need to convert colon delimited mac to dbus/bluez/weird format (dev_blah:etc:foo:bar)

bus = dbus.SystemBus()
manager = dbus.Interface(bus.get_object("org.bluez", "/"), "org.bluez.Manager")
adapter = dbus.Interface(bus.get_object("org.bluez", manager.DefaultAdapter()), "org.bluez.Adapter")

print adapter

print ###########
print nap_mac
nap_mac = string.replace(nap_mac,":","_")
print nap_mac

## Take the 
network = dbus.Interface(bus.get_object("org.bluez", sys.argv[1]), "org.bluez.Network")

print "About to try connecting"
network.Connect("NAP")
print "Networking established."
time.sleep(60)
network.Disconnect()
