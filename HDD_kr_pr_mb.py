from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from Hdd import Hdd

headers = {'User-Agent': 'Totally ie5 for mac'}
url = 'https://www.proshop.dk/Harddisk'

hdds = []
pos_count = 1
page_count = 0
more_pages = True
# while here
while more_pages:
    page_count += 1
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    hdd_search = re.compile(r"<a class=\"site-product-link\" href=\"(.+?)\">" +     # find link
                            r"<h2 product-display-name=\"\">(.+?)</h2>" +           # find name
                            r"(\s|.)*?((\d|\.){1,4})(\s|-)(GB|TB)(\s|.)*?"+         # find GB/TB
                            r"site-currency-lg\">(.+?)<\/span>")                    # find price

    next_page = re.compile(r"href=\"(.+?)\"><span>»",re.I)

    try:
        url = "https://www.proshop.dk/"+re.findall(next_page, str(soup))[0]
        url = url.replace("amp;",'')
    except:
        more_pages= False
        url = None
    hdd_finder = re.findall(hdd_search, str(soup))
    for hdd_info in hdd_finder:
        gb=0
        if "TB" in hdd_info[6].upper():
            gb = float(hdd_info[3])*1000
        elif "GB" in hdd_info[6].upper():
            gb = float(hdd_info[3])
        price = int(hdd_info[8].replace(" kr","").replace(".","").replace(",",""))/100
        hdd = Hdd(name=hdd_info[1], url=hdd_info[0], gb=gb, price=price)
        hdds.append(hdd)
    sleep(1)


hdds.sort(key=lambda x: x.price/x.gb)

print("from top")
for i in range(20):
    print(hdds[i])
print("from bottom")
for i in range(1,20):
    print(hdds[-i])

input()