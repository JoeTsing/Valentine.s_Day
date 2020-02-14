# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# Author:A Child of God
# File: Unnamed
# Time: 2020/01/01
# Description: 一行Python代码实现比心
print('\n'.join([''.join([('I'[(x-y) % len('I')]if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')for x in range(-30, 30)])for y in range(30, -30, -1)]))
