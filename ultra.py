import ctypes
from typing import List, Any, Union

class Sonic (object):
    def __init__(self):
        self.sonic = ctypes.CDLL ("/usr/local/lib/libsonic.so")
        self.sonic.measure.restype = ctypes.c_double
        self.sonic.initialize()

    def getDistance(self):
        results = []
        # FIXME: How many sonic devices have you plugged in? default: 7
        for i in range (7):
            returnValue = self.sonic.measure (ctypes.c_uint (i))
            if returnValue == 0:
                i -= 1
            else:
                results.append (round (returnValue, 2))
        return results