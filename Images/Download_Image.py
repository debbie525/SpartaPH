# https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564

# https://www.kite.com/python/answers/how-to-add-leading-zeros-to-a-number-in-python

import urllib.request
from time import sleep
import time

for x in range(0, 9999):

   zero_filled_number = str(x).zfill(4)
   print(zero_filled_number)

   url_address= f'https://www.larvalabs.com/public/images/cryptopunks/punk{zero_filled_number}.png'
   headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
   request_ = urllib.request.Request(url_address,None,headers)       #The assembled request
   response = urllib.request.urlopen(request_)                       # store the response

   zero_filled_number_2 = zero_filled_number.zfill(5)

   #create a new file and write the image

   f = open('cryptopunk.'+ str(zero_filled_number_2) +'.png','wb')
   f.write(response.read())
   f.close()
   time.sleep(1)