import os
import sys

import sys
import os

def get_dist_path():
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "_internal", "pynblogo.ico")
