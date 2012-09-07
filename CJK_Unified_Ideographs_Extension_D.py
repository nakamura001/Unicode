#! /usr/bin/env python
# coding: utf-8

res = ""
for x in range(0x2B740, 0x2B81F):
	res = res + ("\U" + "%08x" % x).decode("unicode-escape").encode("utf_8")
print res