# This work is licensed under the MIT license.
# Copyright (c) 2013-2024 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam. Attach pin
# P4 to the serial input of a serial LCD screen to see "Hello World!" printed
# on the serial LCD display.

import time
from machine import UART

# Always pass UART 1 for the UART number for your OpenMV Cam.
# The second argument is the UART baud rate.
uart = UART(1, 19200, timeout_char=200)

while True:
    uart.write("Hello World!\r")
    time.sleep_ms(1000)
