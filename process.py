#!/usr/bin/python

import re
import operator
import sys

top_n = 20

data = {}
counts = {}

class Link:
    def __init__(self, source, target): 
            self.source=source
            self.target=target

with open('raw.txt') as fp:
  for line in fp:
    temp = re.split("\t", line.rstrip())
    arr = []
    for idx, val in enumerate(temp):
      arr.append(val.replace(" ", ""))
    date = arr[0]
    source = arr[1]
    target = arr[2]
    count = int(arr[3])
    link = Link(source, target)

    prev = 0
    if link in data:
        prev = data[link]
    data[link] = prev + count

sys.stdout.write("source")
sys.stdout.write(",")
sys.stdout.write("target")
sys.stdout.write(",")
sys.stdout.write("count\n")

for link, count in data.iteritems():
  sys.stdout.write(link.source)
  sys.stdout.write(",")
  sys.stdout.write(link.target)
  sys.stdout.write(",")
  sys.stdout.write(str(data[link]))
  sys.stdout.write("\n")

