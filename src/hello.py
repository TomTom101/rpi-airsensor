#!/usr/bin/env python3

import sys
from time import sleep
from struct import unpack_from, calcsize
import usb.core
import usb.util

vendor = 0x03eb
product = 0x2013
# find our device
print("Find device")
dev = usb.core.find(idVendor=vendor, idProduct=product)
print("Found")
