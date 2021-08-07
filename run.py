#!/usr/bin/env python3

import os
import sys
import runpy

sys.path.insert(0, 'external/zeno')
os.environ['PYTHONPATH'] = 'external/zeno' + os.pathsep + os.environ.get('PYTHONPATH', '')
try:
    from zenqt.main import main
    sys.exit(main())
except ImportError as e:
    raise ImportError('please run `git submodule update --init --recursive`') from e
