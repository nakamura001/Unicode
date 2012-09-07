#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x3400, 0x4DBF):
	res = res + unichr(x).encode('utf_8')
print res