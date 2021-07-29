#### Example Harzard Warnings

An example of consuming Harzard Warnings data from the connector is available under the file at ```mercedes_hazard.py```.

To be able to consume the data, you should first customize three parameters ```connectorURL```,  ```client_credentials``` and ```hazzard_artifact```.
Where the ```connectorURL``` is the url of the Mercedes-Benz IDS Connector,  the ```client_credentials``` is your Merces-Benz Hazard Warnings client credentials encoded in BASE64 and ```hazzard_artifact``` is the reference to the Hazard Warning artifact published at the Mercedes-Benz IDS Connector.

```
# Connector Address
connectorUrl = "https://localhost:8080"

# Mercedes-Benz Client Credentials in BASE64
client_credentials = "<credentials>"

# Artifact
hazzard_artifact = "https://localhost:8080/api/artifacts/?????-????-????-????-????????????"
´´´

#### Example POST request using CURL

It is also possible to consume data from the IDS Connector using CURL.

The example below shows an example of curl request:

```
curl -d '{ 
               "headers": 
               { 
                 "authorization": " Bearer <bearer_token>", 
                 "accept": "application/json;charset=utf-8" 
               }, 
               "params": { "radius": "2000" }, 
               "optional": "@48.723413,9.169551" 
          }' 
          -u 'user:password' 
          -k  
          -H "Content-Type: application/json" 
          -X POST "<artifact_url>/data"
```
