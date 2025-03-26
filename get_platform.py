#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform

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

__author__ = "Michael E. O'Connor"
__copyright__ = "Copyright 2018"

platform_data = {
    'system': platform.system(),
    'platform': platform.platform(),
    'nodename': platform.node(),
    'machine': platform.machine(),
    'architecture': platform.architecture(),
    'processor': platform.processor(),
    'python': platform.python_version()
    }

def main():
    for k, v in platform_data.items():
        print('{:15}: {}'.format(k,v))

if __name__ == '__main__':
    main()
