#!/usr/bin/env python3

import os
import json
import re
import sys

manifest_out = {}
with open('manifest.json.template') as f:
    manifest_out = json.load(f)

try:
    with open('key.txt') as f:
        manifest_out['key'] = f.read().strip()
except:
    print("*** [WARNING] Developer key was not loaded. \
           Does 'key.txt' exist in the project root?")

with open('manifest.json', 'w') as f:
    json.dump(manifest_out, f, indent=2, separators=(',', ': '), sort_keys=True)
    f.write('\n')
