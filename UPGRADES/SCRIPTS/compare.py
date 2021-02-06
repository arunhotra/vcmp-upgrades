#!/usr/bin/env python3

import os
import json
import sys
from collections import OrderedDict


host = sys.argv[1]

os.chdir("..")
os.chdir("./TMP")

infile = host + '-active_standby_guest_pairs.json'
opfile = host + '-compare_status.json'



compare_status = {}

with open(infile, 'r') as guests_file:
    guests = json.load(
        guests_file, object_pairs_hook=OrderedDict)


for guest_pair in guests.keys():
    status_file_1 = guest_pair + '.json'
    status_file_2 = guests[guest_pair] + '.json'

    with open(status_file_1, 'r') as active_file:
        status_file_1_json = json.load(
            active_file, object_pairs_hook=OrderedDict)

    with open(status_file_2, 'r') as standby_file:
        status_file_2_json = json.load(
            standby_file, object_pairs_hook=OrderedDict)

    status = (status_file_1_json == status_file_2_json)
    compare_status[guest_pair + '-' + guests[guest_pair]] = status


with open(opfile, 'w') as outfile:
    json.dump(compare_status, outfile)
