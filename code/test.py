#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:05:44 2018

@author: rajivranjan
"""

import re, os
import string 
import sys
#import twokenize
import csv
from collections import defaultdict
from os.path import basename
import ntpath
import codecs
import unicodedata

prccd_folder = "../data" #no backslashes in front of special characters like spaces
#prccd_folder = "/Users/Imran/Dropbox/AIDR-DA-ALT-SC/sigir2016/data/out-domain/gold_silver/"
prccd_folder = os.path.expanduser(prccd_folder)

print(prccd_folder)
