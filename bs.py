import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")

soup = bs(page)
# find all functions name
names = soup.body.find_all('dt')
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

# find all descriptions
description = soup.body.find_all('dd')
description_usage= []

for item in description:
    item = item.text
    item = item.replace('\n', ' ')
    description_usage.append(item)



print(description_usage)
