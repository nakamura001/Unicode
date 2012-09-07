#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x3040, 0x309F):
	res = res + unichr(x).encode('utf_8')
print res