
import requests
import pprint
import json

# Suppress ssl verification warning
requests.packages.urllib3.disable_warnings()

s = requests.Session()
s.auth = ("user", "password") # consumer credentials
s.verify = False

provider = "https://host1"
consumer = "https://host2"

def descriptionRequest(recipient, elementId):
    params = {}
    if recipient is not None:
        params["recipient"] = recipient
    if elementId is not None:
        params["elementId"] = elementId

    return s.post(consumer + "/api/ids/description", params=params)

def get_list(uri):
    params = {}
    params["page"] = 0
    params["size"] = 30
    return s.get(uri, params=params)


def contractRequest(recipient, resourceId, artifactId, download, contract):
    params = {}
    if recipient is not None:
        params["recipient"] = recipient
    if resourceId is not None:
        params["resourceIds"] = resourceId
    if artifactId is not None:
        params["artifactIds"] = artifactId
    if download is not None:
        params["download"] = download

    return s.post(consumer + "/api/ids/contract", params=params, json=[contract])

response = descriptionRequest(provider + "/api/ids/data", elementId=None)
descriptionResponse = json.loads(response.text)
catalogs = descriptionResponse["ids:resourceCatalog"]
catalogID = catalogs[0]["@id"]
response = descriptionRequest(provider + "/api/ids/data", catalogID)
catalogResponse = json.loads(response.text)

for offer in catalogResponse["ids:offeredResource"]:
    resourceId = offer["@id"]
    resourceLabel = offer["ids:title"][0]["@value"]
    contract = offer["ids:contractOffer"][0]
    contractId = contract["@id"]
    representation = offer["ids:representation"][0]
    artifact = representation["ids:instance"][0]
    artifactId = artifact["@id"]

    response = descriptionRequest(provider + "/api/ids/data", contractId)
    contractResponse = json.loads(response.text)
    obj = contractResponse["ids:permission"][0]
    obj["ids:target"] = artifactId

    response = contractRequest(provider + "/api/ids/data", resourceId, artifactId, False, obj)
    agreementResponse = json.loads(response.text)
    artifactsURI = agreementResponse["_links"]["artifacts"]["href"]
    response = get_list(artifactsURI.replace("{?page,size}", ""))
    agreementArtifactsResponse = json.loads(response.text)
    for agreedArtifacts in agreementArtifactsResponse["_embedded"]["artifacts"]:
        print("Agreement " + agreementResponse["_links"]["self"]["href"] + " registered for " + resourceLabel + " Artifact:" + agreedArtifacts["_links"]["self"]["href"])