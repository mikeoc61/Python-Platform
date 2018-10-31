#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
+-------------------------------------------------------------------------------
+
+ get_platform.py - query various platform attributes
+
+ Reference: https://docs.python.org/3/library/platform.html
+
+ Last update: 10/30/18
+
+-------------------------------------------------------------------------------
'''

__author__      = "Michael E. O'Connor"
__copyright__   = "Copyright 2018"
__email__       = "gmikeoc@gmail.com"

import platform

host_type = platform.system()
sys_platform = platform.platform()
node_name = platform.node()
mach_type = platform.machine()
sys_arch = platform.architecture()
proc_name = platform.processor()
py_version = platform.python_version()

platform_data = dict(
    system = host_type,
    platform = sys_platform,
    nodename = node_name,
    machine = mach_type,
    architecture = sys_arch,
    processor = proc_name,
    python = py_version
)

def main():

    for k, v in platform_data.items():
        print('{:15}: {}'.format(k,v))

if __name__ == '__main__': main()
