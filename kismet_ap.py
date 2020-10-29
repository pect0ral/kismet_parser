#!/usr/bin/env python
import json
import sys

with open(sys.argv[1]) as f:
    k_dict = json.load(f)
print("Chan\tBSSID\tType\tESSID")
for d in k_dict:
  if d['kismet.device.base.type'] == 'Wi-Fi AP':
    print("{}\t{}\t{}\t{}\t{}".format(d['kismet.device.base.channel'],
    d['kismet.device.base.macaddr'],
    d['kismet.device.base.type'],
    d['kismet.device.base.name'],
    d['kismet.device.base.signal']['kismet.common.signal.last_signal']
    ))
