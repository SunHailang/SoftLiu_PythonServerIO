'''
    author: Sun Hai Lang
    date: 2019-09-09

'''

import requests
import ssl
import json
import urllib3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import LeftqueryUtil.LeftqueryUtil

# don't show warning information
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
req = requests.Session()

if __name__ == "__main__":
    print(len(req.cookies))

    # query = LeftqueryUtil()
    # query.query('' '2019-09-10')
