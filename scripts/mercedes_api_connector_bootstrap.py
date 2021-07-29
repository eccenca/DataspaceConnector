
import requests
import pprint
import json

# Suppress ssl verification warning
requests.packages.urllib3.disable_warnings()

s = requests.Session()
s.auth = ("admin", "password")
s.verify = False

host = "localhost:8080"
apis = ["https://api.mercedes-benz.com/vehicledata/v2/vehicles", "https://api.mercedes-benz.com/vehicledata/v2/vehicles/" , "https://api.mercedes-benz.com/hazard_warnings/v2"]

licenses = [["Fuel Status", "https://developer.mercedes-benz.com/products/hazard_warnings/details" ], 
            ["Electric Vehicle Status", "https://developer.mercedes-benz.com/products/electric_vehicle_status/details" ], 
            ["Hazard Warnings", "https://developer.mercedes-benz.com/products/hazard_warnings/details" ]]

offers = [
        {
            "title": "Fuel Status",
            "description": "The Fuel Status data set provides fuel level and the remaining vehicle range of connected vehicles. Applications from fuel suppliers could give Mercedes-Benz drivers individual offers at the right time.",
            "keywords": [
                "Fuel Status"
            ],
            "publisher": "https://mercedes-benz.com",
            "language": "EN",
            "license": "https://developer.mercedes-benz.com/products/fuel_status/details",
            "sovereign": "https://mercedes-benz.com",
            "endpointDocumentation": "https://developer.mercedes-benz.com/products/fuel_status",
            "Mantainer": "http://eccenca.com",
            "Contact": "edgard.marx@eccenca.com"
        },
        {
            "title": "Electric Vehicle Status",
            "description": "The Electric Vehicle Status data set provides charge and remaining range of a specific electric vehicle. Knowing these current values, the next charging stop can be predicted.",
            "keywords": [
                "Electric Vehicle Status"
            ],
            "publisher": "https://mercedes-benz.com",
            "language": "EN",
            "license": "https://developer.mercedes-benz.com/products/electric_vehicle_status/details",
            "sovereign": "https://mercedes-benz.com",
            "endpointDocumentation": "https://developer.mercedes-benz.com/products/electric_vehicle_status",
            "Mantainer": "http://eccenca.com",
            "Contact": "edgard.marx@eccenca.com"
        },
        {
            "title": "Hazard Warnings",
            "description": "Benefit from aggregated event data from our connected vehicle fleet to alert your drivers ahead of any dangerous situation. The data set consists of different types of safety-related events, ranging from dangerous traffic events to weather conditions.",
            "keywords": [
                "Hazard Warnings"
            ],
            "publisher": "https://mercedes-benz.com",
            "language": "EN",
            "license": "https://developer.mercedes-benz.com/products/hazard_warnings/details",
            "sovereign": "https://mercedes-benz.com",
            "endpointDocumentation": "https://developer.mercedes-benz.com/products/hazard_warnings",
            "Mantainer": "http://eccenca.com",
            "Contact": "edgard.marx@eccenca.com"
        }
   ]

representations = [{
                        "title": "Fuel Status",
                        "description": "Data representation of Fuel Status data.",
                        "mediaType": "JSON",
                        "language": "EN",
                        "example": "https://github.com/eccenca/DaimlerDataspaceSharedData/blob/main/fuel-status.json"
                    },
                    {
                        "title": "Electric Vehicle Status",
                        "description": "Data representation of Electric Vehicle Status.",
                        "mediaType": "JSON",
                        "language": "EN",
                        "example": "https://github.com/eccenca/DaimlerDataspaceSharedData/blob/main/electric-vehicle-status.json"
                    },
                    {
                        "title": "Hazard Warnings",
                        "description": "Data representation of Hazard Warnings data.",
                        "mediaType": "JSON",
                        "language": "EN",
                        "example": "https://github.com/eccenca/DaimlerDataspaceSharedData/blob/main/harzard-warnings.json"
                    }]

def create_policy(title, desc):
    return s.post(
        "https://" + host + "/api/rules",
        json={
            "value": """{
            "@context" : {
                "ids" : "http://w3id.org/idsa/core/",
                "idsc" : "http://w3id.org/idsa/code/"
            },
            "@type": "ids:Permission",
            "@id": "http://w3id.org/idsa/autogen/permission/c0bdb9d5-e86a-4bb3-86d2-2b1dc9d226f5",
            "ids:description": [
              {
                "@value": """ + desc + """,
                "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML"
              }
            ],
            "ids:title": [
              {
                "@value": """ + title + """,
                "@type": "http://www.w3.org/2001/XMLSchema#string"
              }
            ],
            "ids:action": [
              {
                "@id": "idsc:USE"
              }
            ],
            "ids:postDuty": [
              {
                "@type": "ids:Duty",
                "@id": "http://w3id.org/idsa/autogen/duty/863d2fac-1072-476d-b504-9d6347fe4b6f",
                "ids:action": [
                  {
                    "@id": "idsc:NOTIFY"
                  }
                ],
                "ids:constraint": [
                  {
                    "@type": "ids:Constraint",
                    "@id": "http://w3id.org/idsa/autogen/constraint/c91e64ce-1fc1-44fd-bec1-6c6778603919",
                    "ids:rightOperand": {
                      "@value": "http://localhost:6060/api/ids/data",
                      "@type": "http://www.w3.org/2001/XMLSchema#anyURI"
                    },
                    "ids:leftOperand": {
                      "@id": "idsc:ENDPOINT"
                    },
                    "ids:operator": {
                      "@id": "idsc:DEFINES_AS"
                    }
                  }
                ]
              }
            ]
          }"""
        },
    ).headers["Location"]

def get_offers():
    return s.get(
        "https://" + host + "/api/offers?page=0&size=30"
    )

def create_remote_artifact(endpoint):
    return s.post(
        "https://" + host + "/api/artifacts",
        json={"accessUrl": endpoint }
    ).headers["Location"]

def create_offered_resource(resource):
    return s.post("https://" + host + "/api/offers", json=resource).headers["Location"]

def add_resource_to_catalog(catalog, resource):
    s.post(catalog + "/offers", json=[resource])

def add_catalog_to_resource(resource, catalog):
    s.post(resource + "/catalogs", json=[catalog])

def add_representation_to_resource(resource, representation):
    s.post(resource + "/representations", json=[representation])

def add_artifact_to_representation(representation, artifact):
    s.post(representation + "/artifacts", json=[artifact])

def add_contract_to_resource(resource, contract):
    s.post(resource + "/contracts", json=[contract])

def add_rule_to_contract(contract, rule):
    s.post(contract + "/rules", json=[rule])

def create_offered_resource(resource):
    return s.post("https://" + host + "/api/offers", json=resource).headers["Location"]

def create_representation(representation):
    return s.post("https://" + host + "/api/representations", json=representation).headers[
        "Location"
    ]

def create_contract():
    return s.post("https://" + host + "/api/contracts", json={}).headers["Location"]

def create_catalog():
    return s.post("https://" + host + "/api/catalogs", json={}).headers["Location"]

def remove_offer(offer_href):
    return s.delete(offer_href)

# Cleaning current offers

current_offers_response = get_offers()
current_offers = json.loads(current_offers_response.text)
for current_offer in current_offers["_embedded"]["resources"]:
    offer_href = current_offer["_links"]["self"]["href"]
    print("Removing offer " + offer_href)
    remove_offer(offer_href)

i = 0
catalog = create_catalog()
print("Adding APIS to IDS Catalog:" + catalog)
for api in apis:    
    offer = create_offered_resource(offers[i])
    representation = create_representation(representations[i])
    artifact = create_remote_artifact(api)
    contract = create_contract()
    notification_rule = create_policy(licenses[i][0] + " Usage Policy", licenses[i][1])

    add_resource_to_catalog(catalog, offer)
    add_representation_to_resource(offer, representation)
    add_artifact_to_representation(representation, artifact)
    add_contract_to_resource(offer, contract)
    add_rule_to_contract(contract, notification_rule)

    print("Registering " + licenses[i][0]  + " in " + artifact )
    i = i + 1
