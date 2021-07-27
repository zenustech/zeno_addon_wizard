#!/usr/bin/env python3

import os, sys

sys.exit(os.system('cmake -B build && cmake --build build --parallel'))
