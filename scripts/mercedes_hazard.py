#!/usr/bin/env python3
#
# Copyright 2021 http://eccenca.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from resourceapi import ResourceApi
from idsapi import IdsApi
import requests
import pprint
import json
import sys

s = requests.Session()
s.auth = ("admin", "password")
s.verify = False

# Suppress ssl verification warning
requests.packages.urllib3.disable_warnings()

# Connector Address
connectorUrl = "https://localhost:8080"

# Mercedes-Benz Client Credentials in BASE64
client_credentials = "<credentials>"

# Artifact
hazzard_artifact = "https://localhost:8080/api/artifacts/?????-????-????-????-????????????"

def postArtifact(artifactID, auth_token):
  url =  connectorUrl + "/api/artifacts/" + artifactID + "/data"
  params = {}

  data = {
    "headers": {
        "authorization": " Bearer " + auth_token,
        "accept": "application/json;charset=utf-8"
    },
    "params": {
      "radius": "2000"
    },
    "optional": "@48.723413,9.169551"
  }

  return s.post(url, headers={
    "accept-encoding": "no"
  }, json=data)

def getToken():
  token_url = "https://id.mercedes-benz.com/as/token.oauth2"
  data = {"grant_type": "client_credentials"}
  api_call_headers = {"Authorization": "Basic " + client_credentials, "content-type": "application/x-www-form-urlencoded"}
  return requests.post(token_url, data=data, verify=False, allow_redirects=False, headers=api_call_headers)

print("Getting Access Token...")
# Getting Access Token
get_token_response = getToken()
json_token_reponse = json.loads(get_token_response.text)
auth_token = json_token_reponse["access_token"]
print(auth_token)

artifactUUID = hazzard_artifact.replace(connectorUrl + "/api/artifacts/",'')

# Getting Artifact Data
response = postArtifact(artifactUUID, auth_token)
pprint.pprint(str(response.text))
