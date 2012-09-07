#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x4e00, 0x9FFF):
	res = res + unichr(x).encode('utf_8')
print res