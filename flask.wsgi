import sys
import os
DIR=os.path.dirname(__file__)
sys.path.append(DIR)
sys.path.insert(0, ’/home/s0000001/myapp/’)
from myapp import app as application