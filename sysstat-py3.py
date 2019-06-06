#!/bin/env python3

import os, sys

#show current working directory
print("*" * 50)
print("current directory")
print("*" * 50)
os.system('pwd')
print("*" * 50)

#running time
print("*" * 50)
print("system is up for:")
print("*" * 50)
os.system('uptime')
print("*" * 50)

print("*" * 50)
print("disk info")
print("*" * 50)
os.system('df -hTi')

print("*" * 50)
