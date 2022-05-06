import requests
from bs4 import BeautifulSoup
import os
import json

# ingest a json file containing data for theater sites to scrape
theaters = open('theaters.json')
domains = json.load(theaters)
theaters.close()

# list to keep track of all urls
all_urls=[]

# Create a file to hold the new JSON
filea = open('url_list.json', 'w')
filea.close() 

# list of files to ignore
def word_list(href):
    words = ['/aboutus','/about-us','/auditions','/archive','/contactus','/contact-us','/donate','/discount','/gallery','/get-involved','/groups','/info','/location','/faq','/media','/news','/newsletter','/staff','/subscription','/support','/tickets','/volunteer']
    for word in words:
        if word in href:
            return True
    return False

# Analyze links and push to list of urls if fit criteria
def find_urls(soup,original_url,new_url,domain):
    urls=[]
    for link in soup.find_all("a"):
        href = link.get("href")
        
        if href==None or href=='/' or href=="" or href=="#":
            # ignore self-referencial urls
            continue
        if href.startswith("/") or not href.startswith("http"):
            # if url is relative, add the domain to the string
            href=original_url[:-1]+href
        if href in urls or href in all_urls:
            # check if url is already in list
            continue
        ignore = word_list(href) or href.endswith(".pdf") or href.endswith(".png") or href.endswith(".jpg") or href.endswith("jpeg") or original_url not in href        
        if not ignore:
            # if does not contain key terms to ignore, push to url list
            urls.append(href)
            all_urls.append(href)
    
    # recursive check for more urls on sub-linked pages
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            find_urls(soup,original_url,url,domain)
        except Exception:
            continue
    
    return urls
    
for domain in domains:
    # loop through each url in the list of domains
    url=domain['url']
    try:
        response=requests.get(url)
    except Exception:
        continue
    # add the url to the full list
    all_urls.append(url)  
    # get the page content
    soup = BeautifulSoup(response.text, "html.parser")
    # run content through url analyzer
    new_urls = find_urls(soup,url,url,domain)
    # add the base url to the url list
    new_urls.append(url)
    # update domain object
    domain['urls']=new_urls
    # print domain object to file
    filea = open('url_list.json', 'a') 
    filea.write(json.dumps(domain))
    filea.close() 

# once analysis is complete - go to the json file and remove any urls that are clearly not relevant
# then run get_pages.py script
