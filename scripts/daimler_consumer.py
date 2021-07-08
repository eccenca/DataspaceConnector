import requests
import pprint
import json
import tqdm
import os
import urllib.request

# Suppress ssl verification warning
requests.packages.urllib3.disable_warnings()

connector = "https://ids.eccenca.dev:9090/admin/api/resources/"

s = requests.Session()
s.auth = ('admin', 'password')
s.verify = False

def data(resourceID):
    url =  connector + resourceID
    params = {}
    return s.get(url, params=params)

response = data("3c34a668-89c2-4d58-aa43-28a96d560158")
resource = json.loads(response.text)
representations = resource["representations"]
representation = resource["representations"][0]
source = representation["source"]
url = source["url"]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
   content = response.read()
   json_data = json.loads(content)
   print(json_data)