#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x20000, 0x2A6DF):
	res = res + ("\U" + "%08x" % x).decode("unicode-escape").encode("utf_8")
print res