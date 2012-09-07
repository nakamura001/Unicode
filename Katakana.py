#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x30A0, 0x30FF):
	res = res + unichr(x).encode('utf_8')
print res