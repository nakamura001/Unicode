#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0xF900, 0xFAFF):
	res = res + unichr(x).encode('utf_8')
print res