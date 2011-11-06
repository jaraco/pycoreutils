# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2010, 2011 Hans van Leeuwen.
# See LICENSE.txt for details.

from __future__ import print_function, unicode_literals
import sys
import tempfile


def mktemp(p):
    # TODO: Templates, most of the options
    p.set_defaults(func=func)
    p.description = "Create a temporary file or directory, safely, and " + \
                    "print its name."
    p.add_argument("-d", "--directory", action="store_true", dest="directory",
                   help="create a directory, not a file")
    return p


def func(args):
    if args.directory:
        print(tempfile.mkdtemp(prefix='tmp.'))
    else:
        print(tempfile.mkstemp(prefix='tmp.')[1])
