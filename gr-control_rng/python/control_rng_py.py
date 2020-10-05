#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import serial
from gnuradio import gr

class control_rng_py(gr.basic_block):
    """
    docstring for block control_rng_py
    """
    def __init__(self, serialPort, state, attenuation, band):
        gr.basic_block.__init__(self,
            name="control_rng_py",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.port = serial.Serial(serialPort, baudrate=9600, timeout=3.0)
        if (self.port.isOpen()):
            print "RNG: Re-open serial port %s" % serialPort
            self.port.close()
            self.port.open()
        else:
            print "RNG: Open serial port %s" % serialPort
            self.port.open()
        self.act_state = state
        self.act_attenuation = attenuation
        self.act_band = band

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def set_state(self, state):
        if self.act_state != state:
            self.act_state = state
            cmd = """0%x""" % state
            self.port.write(cmd)

    def set_attenuation(self, attenuation):
        if self.act_attenuation != attenuation:
            self.act_attenuation = attenuation
            cmd = """1%x""" % attenuation
            self.port.write(cmd)

    def set_band(self, band):
        if self.act_band != band:
            self.act_band = band
            cmd = """2%x""" % band
            self.port.write(cmd)

    def general_work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
