import requests
from bs4 import BeautifulSoup
import json
import os
import re


# read in url list from json file
pages = open('url_list.json')
url_list = json.load(pages)
pages.close()

#Create a file to hold the new JSON
filename = 'pages.json'
filea = open(filename, 'w')
filea.close() 

async def get_body(url):
    # try to get url and create soup
    try:
        response=requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception:
        return ''
    page_text = soup.body
    
    # remove unneeded elements
    for data in soup(['style','script','form','input']):
        # Remove tags
        data.decompose()
    
    # make string of stripped text
    string = '\n'.join(soup.stripped_strings)
    
    # replace quotes
    s2 = string.replace('"', '&quot;')
    s3 = s2.replace("'","&apos;")
    s4 = s3.replace("\u00B4","&rsquo;")
    s5 = s4.replace("\u2019","&rsquo;")
    s6 = s5.replace("\u2019","&rsquo;")
    s7 = s6.replace("\u2018","&ldquo;")
    s8 = s7.replace("\u2019","&rsquo;")
    s9 = s8.replace("\u201C","&ldquo;")
    s10 = s9.replace("\u201D","&rdquo;")
        
    # return string
    return s10
    
for theater in url_list: 
    theater['pages']=[]
    urls = theater['urls']
    for url in urls:
        body = await get_body(url)
        theater['pages'].append(body)

# save json to file
filea = open(filename, 'a') 
filea.write(json.dumps(url_list))
filea.close()    

print('DONE')
    