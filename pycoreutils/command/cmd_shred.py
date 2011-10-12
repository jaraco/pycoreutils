#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2010, 2011 Hans van Leeuwen.
# See LICENSE.txt for details.

from __future__ import print_function, unicode_literals
import pycoreutils
import logging
import os
import random
import sys


@pycoreutils.addcommand
def shred(p):
    p.set_defaults(func=func)
    p.description = "Overwrite the specified FILE(s) repeatedly, in order " + \
                    "to make it harder for even very expensive hardware " + \
                    "probing to recover the data."
    p.epilog = "This program acts as GNU 'shred -x', and doesn't round " + \
               "sizes up to the next full block"
    p.add_argument('files', nargs='*')
    p.add_argument("-n", "--iterations", dest="iterations", default=3,
            help="overwrite ITERATIONS times instead of the default (3)")
    p.add_argument("-v", "--verbose", action="store_true", dest="verbose",
            help="show progress")


def func(args):
    for arg in args.files:
        for i in range(args.iterations):
            size = os.stat(arg).st_size
            fd = open(arg, mode='w')
            logging.debug('Size:', size)
            fd.seek(0)
            for i in range(size):
                # Get random byte
                b = "".join(chr(random.randrange(0, 256)))
                fd.write(b)
            fd.close()
