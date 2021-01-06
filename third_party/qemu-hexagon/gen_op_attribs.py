#!/usr/bin/env python3

##
##  Copyright(c) 2019-2020 Qualcomm Innovation Center, Inc. All Rights Reserved.
##
##  This program is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program; if not, see <http://www.gnu.org/licenses/>.
##

import sys
import re
import string
from io import StringIO

from hex_common import *


def main():
  read_semantics_file(sys.argv[1])
  read_attribs_file(sys.argv[2])
  calculate_attribs()

  ##
  ## Generate the op_attribs_generated.h file
  ##     Lists all the attributes associated with each instruction
  ##
  f = StringIO()
  for tag in tags:
    f.write('OP_ATTRIB(%s,ATTRIBS(%s))\n' % \
        (tag, ','.join(sorted(attribdict[tag]))))
  realf = open(sys.argv[3], 'wt')
  realf.write(f.getvalue())
  realf.close()
  f.close()


if __name__ == "__main__":
  main()