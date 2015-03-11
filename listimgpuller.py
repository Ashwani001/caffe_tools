#Script to read all names from database and pull their images from google
#Images willl be stored in respective folder names in /home/ash/caffe/examples/images/Non-Processed
#edited from https://gist.github.com/crizCraig/2816295#file-gistfile1-py
#Uncomment filespliter() if running for first time; line 69

import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

def go(query):
  path='/home/ash/caffe/examples/images/Non-Processed'

  BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query + '&start=%d'

  BASE_PATH = os.path.join(path, query)

  if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

  start = 0 # Google's start query string parameter for pagination.
  while start < 5: # Google will only return a max of 56 results.
    r = requests.get(BASE_URL % start)
    for image_info in json.loads(r.text)['responseData']['results']:
      url = image_info['unescapedUrl']
      try:
        image_r = requests.get(url)
      except ConnectionError, e:
        print 'could not download %s' % url
        continue

      # Remove file-system path characters from name.
      title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')

      file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
      try:
        Image.open(StringIO(image_r.content)).save(file, 'JPEG')
      except IOError, e:
        # Throw away some gifs...blegh.
        print 'could not save %s' % url
        continue
      finally:
        file.close()

    print start
    start += 4 # 4 images per page.

    time.sleep(5)

def filespliter(): #splits up csv to rows
	text_file = open("/home/ash/datatopull.csv", "r")
	lines = text_file.read().split(',')
	text_file.close()

	f = open("rowonlydata.txt","w")

	for line in lines:
		if len(line)!=0:
			if line[0]=='\n':
				f.write((line).strip()+'\n')
			elif line[0]==' ':
				f.write((line).strip()+'\n')
	f.close()

#filespliter()# !!!	Uncomment if running this for the first time !!!
s=open("rowonlydata.txt","r")
slines= s.read().split('\n')
for line in slines:
	go(line)
