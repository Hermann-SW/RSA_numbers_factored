#!/usr/bin/python
""" pylinted and edited with black """
import os
import random
import time
import stdiomask

s = stdiomask.getpass("factor: ")
random.seed(time.time_ns() * int(s))

L = 432

S = "[" + str(random.getrandbits(L)) + "," + str(random.getrandbits(L + 2)) + "]"
r = os.system("S='" + S + "' gp -q < challenge.gp")
