#!/usr/bin/env python3

import sys
import runpy

sys.path.insert(0, 'external/zeno')
try:
    runpy.run_module('zenqt')
except ImportError as e:
    raise ImportError('please run `git submodule update --init --recursive`') from e
