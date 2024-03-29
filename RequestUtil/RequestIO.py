'''
    author: Sun Hai Lang
    date: 2019-09-09

'''

import sys

import os, json
o_path = os.getcwd()
sys.path.append(o_path)

import requests
import ssl
import urllib3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from RequestUtil.LeftqueryUtil import LeftqueryUtil

# don't show warning information
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
req = requests.Session()

if __name__ == "__main__":
    print(len(req.cookies))

    query = LeftqueryUtil(req)
    from_station = '徐州东'
    to_station = '上海'
    date = '2019-09-24'
    info = query.query(from_station, to_station, date)
    # info = query.station_name(from_station)
    print(info)
    print(req.cookies)