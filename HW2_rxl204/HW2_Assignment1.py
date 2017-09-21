Author: Rachel Lim, NYU, September 2017
##############################
# Code written for HW2 of PUI2016
#############################

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
# the next import allows me to read line input arguments
import pylab as pl
import sys
import json
import urllib2
import os
try: 
	import urllib2 as urllib
except ImportError: 
	import urllib.request as urllib
%pylab inline 
pl.rc('font', size=15)




