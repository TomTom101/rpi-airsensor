#!/usr/bin/env python3

import sys
from time import sleep
from struct import unpack_from, calcsize

class Airsensor:
    def __init__(self):
        try:
            import usb.core
            import usb.util
        except:
            print("Import failed")
            return None

        vendor = 0x03eb
        product = 0x2013
        # find our device
        print("Find device")
        try:
            self.dev = usb.core.find(idVendor=vendor, idProduct=product)
        except Exception as e:
            print(e)
        else:
            print("OK")

        # was it found?
        if self.dev is None:
            raise ValueError('Device not found')

        if self.dev.is_kernel_driver_active(0):
            try:
                self.dev.detach_kernel_driver(0)
                print ("kernel driver detached")
            except usb.core.USBError as e:
                sys.exit("Could not detach kernel driver: %s" % str(e))

        #self.dev.set_configuration()

        usb.util.claim_interface(self.dev, 0)

        # get an endpoint instance
        cfg = self.dev.get_active_configuration()

        intf = cfg[(0,0)]

        ep = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match = \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)

        assert ep is not None

    def test(self):
        return "OK"

    def read(self):
        try:
            return self.dev.read(0x81, 0x10, 1000)
        except usb.core.USBError:
            return "?"

        def mapNum(value, in_min, in_max, out_min, out_max):
            return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

        #Flush
        read()

        ret = self.dev.write(0x02, "\x40\x68\x2a\x54\x52\x0a\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40", 1000)
        #print("USB returns {} on write".format(ret))

        data = read()
        #print("USB returns {} with length {} on read".format(data, len(data)))

        toc, = unpack_from('<H', data, 2)

        toc = max(450, min(2000, toc))
        return mapNum(toc, 450, 2000, 100, 0)
