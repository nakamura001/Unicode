#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0xFF00, 0xFFEF):
	res = res + unichr(x).encode('utf_8')
print res