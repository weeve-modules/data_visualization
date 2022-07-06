# -*- coding: utf-8 -*-
import os
import re
import sys
import time


ky001_filename = None
dev_path = '/sys/bus/w1/devices/'

if len(os.listdir(dev_path)) < 1:
    sys.exit('Have you updated config.txt and run modprobe?')

pattern = '^[1-9][1-9]-[A-Za-z0-9]*$'  # File pattern like 28-20320c40bf7c

for filename in os.listdir(dev_path):
    if re.match(pattern, filename):  # If filename match the pattern
        print("Using file '{}'".format(filename))
        ky001_filename = filename

if not ky001_filename:
    sys.exit("Couldn't find any file matching requirements.")

try:
    while True:
        ky001_file = open("{}{}/w1_slave".format(dev_path, ky001_filename))
        data = ky001_file.read()
        ky001_file.close()
        temp_c = float(data.split(" t=")[1].strip()) / 1000
        temp_f = round(temp_c * 1.8 + 32, 2)
        print('Temp:  {}ºC  {}ºF  (CTRL+C to exit)'.format(temp_c, temp_f))
        time.sleep(1.5)
except KeyboardInterrupt:
    pass

