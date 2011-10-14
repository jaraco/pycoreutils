#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2010, 2011 Hans van Leeuwen.
# See LICENSE.txt for details.

from __future__ import print_function, unicode_literals
import pycoreutils
import time


@pycoreutils.addcommand
def tail(p):
    # TODO: Everything!!!!!!!!
    p.set_defaults(func=func)
    p.description = "Print the last 10 lines of each FILE to standard " + \
                    "output. With more than one FILE, precede each with a " + \
                    "header giving the file name. With no FILE, or when " + \
                    "FILE is -, read standard input."
    p.add_argument("files", nargs="*")
    p.add_argument("-f", "--follow", action="store_true",
            help="output appended data as the file grows")
    p.add_argument("-i", "--interval", default=1, type=float,
            help="When using 'follow', check the file every INTERVAL seconds")
    p.add_argument("-n", "--lines", default=10, metavar="N",
            help="output the last N lines, instead of the last 10", type=int)


def func(args):
    if args.follow:
        fds = pycoreutils.args2fds(args.files)
        while True:
            time.sleep(args.interval)
            for fd in fds:
                where = fd.tell()
                line = fd.readline()
                if not line:
                    fd.seek(where)
                else:
                    print(line, end='')
    else:
        for fd in pycoreutils.args2fds(args.files):
            pos, lines = args.lines + 1, []
            while len(lines) <= args.lines:
                try:
                    fd.seek(-pos, 2)
                except IOError:
                    fd.seek(0)
                    break
                finally:
                    lines = list(fd)
                pos *= 2
            for line in lines[-args.lines:]:
                print(line, end='')

    """
    if args.follow:
        # tail -f
        print('G'*99, args.interval)
        while 1:
            for fd in fdlist:
                fd.seek(0, 2)
                lines = fd.readlines()
                if lines:
                    for line in lines:
                        print(line)
                        yield line
                    time.sleep(1)
    """
