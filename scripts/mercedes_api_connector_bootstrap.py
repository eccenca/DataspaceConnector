
import requests
import pprint
import json

# Suppress ssl verification warning
requests.packages.urllib3.disable_warnings()

s = requests.Session()
s.auth = ("user", "password")
s.verify = False

host = "localhost"
apis = ["https://api.mercedes-benz.com/vehicledata/v2/vehicles", "https://api.mercedes-benz.com/vehicledata/v2/vehicles" , "https://api.mercedes-benz.com/hazard_warnings/v2", "https://api.mercedes-benz.com/vehicledata_tryout/v2/vehicles", "https://api.mercedes-benz.com/vehicledata_tryout/v2/vehicles"]

licenses = [["Fuel Status", "https://developer.mercedes-benz.com/products/hazard_warnings/details" ], 
            ["Electric Vehicle Status", "https://developer.mercedes-benz.com/products/electric_vehicle_status/details" ], 
            ["Hazard Warnings", "https://developer.mercedes-benz.com/products/hazard_warnings/details" ],
            ["Fuel Status Tryout", "https://api.mercedes-benz.com/vehicledata_tryout/v2/vehicles" ],
            ["Electric Vehicle Status Tryout", "https://api.mercedes-benz.com/vehicledata_tryout/v2/vehicles" ]]
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
        },
        {
            "title": "Fuel Status Tryout",
            "description": "This is a sandbox for Fuel Status data set provides fuel level and the remaining vehicle range of connected vehicles. Applications from fuel suppliers could give Mercedes-Benz drivers individual offers at the right time.",
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
            "title": "Electric Vehicle Status Tryout",
            "description": "This is a sandbox for Electric Vehicle Status data set provides charge and remaining range of a specific electric vehicle. Knowing these current values, the next charging stop can be predicted.",
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
                    },
                    {
                        "title": "Fuel Status Tyout",
                        "description": "Data representation of Fuel Status data.",
                        "mediaType": "JSON",
                        "language": "EN",
                        "example": "https://github.com/eccenca/DaimlerDataspaceSharedData/blob/main/fuel-status.json"
                    },
                    {
                        "title": "Electric Vehicle Status Tryout",
                        "description": "Data representation of Electric Vehicle Status.",
                        "mediaType": "JSON",
                        "language": "EN",
                        "example": "https://github.com/eccenca/DaimlerDataspaceSharedData/blob/main/electric-vehicle-status.json"
                    }
                ]

def create_policy(title, desc):
    value = f'''{{
            "@context" : {{
                "ids" : "http://w3id.org/idsa/core/",
                "idsc" : "http://w3id.org/idsa/code/"
            }},
            "@type": "ids:Permission",
            "@id": "http://w3id.org/idsa/autogen/permission/c0bdb9d5-e86a-4bb3-86d2-2b1dc9d226f5",
            "ids:description": [
              {{
                "@value": "This polcy allows the usage of the API under the respective ",
                "@type": "http://www.w3.org/2001/XMLSchema#string"
              }}
            ],
            "ids:title": [
              {{
                "@value": "Free for usage",
                "@type": "http://www.w3.org/2001/XMLSchema#string"
              }}
            ],
            "ids:action": [
              {{
                "@id": "idsc:USE"
              }}
            ]
          }}'''

    svalue = {
          "value": """{
          "@context" : {
              "ids" : "https://w3id.org/idsa/core/",
              "idsc" : "https://w3id.org/idsa/code/"
          },
        "@type": "ids:Permission",
        "@id": "https://w3id.org/idsa/autogen/permission/154df1cf-557b-4f44-b839-4b68056606a2",
        "ids:description": [
          {
            "@value": "Free for Usage",
            "@type": "http://www.w3.org/2001/XMLSchema#string"
          }
        ],
        "ids:title": [
          {
            "@value": "This policy allows the data set usage by any third-party under the restrictions pre-established by the data provider Mercedes-Benz.",
            "@type": "http://www.w3.org/2001/XMLSchema#string"
          }
        ],
        "ids:action": [
          {
            "@id": "idsc:USE"
          }
        ]
      }"""
    }
    parsedJSON = json.loads(value)
    return s.post(
        "https://" + host + "/api/rules",
        json=svalue
    ).headers["Location"]

def get_objects(object):
    return s.get(
        "https://" + host + "/api/" + object + "s?page=0&size=30"
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

def remove(object_href):
    return s.delete(object_href)

def remove_uuid(offer_href, uuid):
    return s.delete(offer_href, json={'id' : uuid})

def remove(object, objects):
  current_objects = json.loads(objects.text)
  for current_object in current_objects["_embedded"][object + 's']:
    object_href = current_object["_links"]["self"]["href"]
    print("Removing " + object + " " + object_href)
    remove(object_href)

def remove_object_uuid(object, objects):
  current_objects = json.loads(objects.text)
  for current_object in current_objects["_embedded"][object + 's']:
    object_href = current_object["_links"]["self"]["href"]
    print("Removing " + object + " " + object_href)
    uuid = object_href.rindex("/",1)
    remove_uuid(object_href, uuid)

# Cleaning dataset

object_response = get_objects("catalog")
remove_object_uuid("catalog", object_response)

object_response = get_objects("offer")
remove_object_uuid("resource", object_response)

object_response = get_objects("artifact")
remove_object_uuid("artifact", object_response)

object_response = get_objects("representation")
remove_object_uuid("representation", object_response)

object_response = get_objects("contract")
remove_object_uuid("contract", object_response)

i = 0
catalog = create_catalog()
policy = create_policy(licenses[i][0] + " Usage Policy", "For more details visit " + licenses[i][1])
contract = create_contract()

print("Adding APIS to IDS Catalog:" + catalog)
for api in apis:    
    offer = create_offered_resource(offers[i])
    representation = create_representation(representations[i])
    artifact = create_remote_artifact(api)

    add_resource_to_catalog(catalog, offer)
    add_representation_to_resource(offer, representation)
    add_artifact_to_representation(representation, artifact)
    add_contract_to_resource(offer, contract)
    add_rule_to_contract(contract, policy)

    print("Registering " + licenses[i][0]  + " in " + artifact )
    i = i + 1
