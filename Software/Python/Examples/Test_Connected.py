#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for determining if a BrickPi3 is connected to the Raspberry Pi

from __future__ import print_function
from __future__ import division

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

try:
    manufacturer, merr = BP.get_manufacturer()
    board, berr = BP.get_board()
    
    if(merr == BP.SUCCESS and berr == BP.SUCCESS and manufacturer == "Dexter Industries" and board == "BrickPi3"):
        print("BrickPi3 connected and running")
    
    else:
        print("Communication with BrickPi3 unsuccessful")

except KeyboardInterrupt:
    pass
