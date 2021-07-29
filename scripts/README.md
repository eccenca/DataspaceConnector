
#### Bootstraping the IDS Connector

To bootstrap the three APIs in the IDS Mercedes-Benz Connector replace the variable ```host``` at ```mercedes_api_connector_bootstrap.py``` by your connector address:

```
...
host = "localhost:8080"
...
```

And execute the the ```mercedes_api_connector_bootstrap.py``` script as follows:

```
python mercedes_api_connector_bootstrap.py
```

#### Example Harzard Warnings

An example of consuming Harzard Warnings data from the connector is available under the file at ```mercedes_hazard.py```.

To be able to consume the data, you should first customize three parameters ```connectorURL```,  ```client_credentials``` and ```hazzard_artifact```.
Where the ```connectorURL``` is the url of the Mercedes-Benz IDS Connector,  the ```client_credentials``` is your Merces-Benz Hazard Warnings client credentials encoded in BASE64 and ```hazzard_artifact``` is the reference to the Hazard Warning artifact published at the Mercedes-Benz IDS Connector.

```
...
# Connector Address
connectorUrl = "https://localhost:8080"

# Mercedes-Benz Client Credentials in BASE64
client_credentials = "<credentials>"

# Artifact
hazzard_artifact = "https://localhost:8080/api/artifacts/?????-????-????-????-????????????"
...
```

After changing these parameters, one can execute the script as follows:

```
python mercedes_hazard.py
```

If everything goes alright, you may see something like:

```
Starting script
Getting Access Token...
eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiY3R5IjoiSldUIiwia2lkIjoiQ0lBTVNZTSIsInBpLmF0bSI6Imh4M2UifQ..sVe1ZBe0tyNYa9d1KEregw.g4rHllvScWuN
1ronWcv25TLv-P5Wv4hFFdJU2u2L7nET46f16Paesvk-6vz2kNjmMKIGT9_ggkn3pyKMjL8yF5YidUPjsOQ-zE-QOtTfX8K_jUXAVmm9-cZ7fbpsT1lZmteGL4Gue0iUG6qz7elN7TO0UqwthU6UDYjoKuEOpeGsaPWf4nwSt79UJK0JqrddHA_Tz7-qK9j1NmpUT8zLpA9tTZry
7TvK9vHo1JnPoGKfhuIazgrSKmk8ocBabizZAbLX121s2dlruP4ZlQSv8DK-1wAvpXtNNYOCalopa9AqDbtiiwFKdd2Z0x2oQtP5C-VAbNUT1vStjdFf39Bvx3550oyRC0TwMy6Mq6nMIPjQlD0-0q5F5B3teU4c86E0dy6xSstGJidvtHbh6UbhrTjvUi4kdkqecTBBL1uxem7L87SUsKkmJ_IbGAbcAteF0O-E7l9uVUkQcJ
yHjfEG68sTCW7K2-rlWp7JY2PUmfAHhn_5y8TpGE8_HawRY8ApQ66-ObnVmv5vOw-q2JKBYP_OgTSgt7LoXq1GvxMbJs4ZeEOIvLfBJ2-KNHvIBUHSnOLpQoZjUcGI_z7RwuiWdPiQiGbP5qRO0zg26osHc1DnBoatHBpHo6MBOmPrPKQxrT8KIwVqvh9svcnPQ82sGGifrb2pWeslEv1xAEeY4SccF5F2bTy-GcwOW5HP_u2dqxYmKe8HIJ0T0rfVLvxSGWmttn1qpH4UfNnowQGRpPd245tbfKmgIfNk65gnUJVM.H0PWJpx5#
EO3hyHIh1vkUYzVhJgkYRyyNoVGlutcPjK4
'{"result":[{"cancelled":true,"cause":"HL","heading":0,"location":[9.192255699999999,48.7237248],"ts":1627500467055,
"uuid":"3a5cf27e-2d22-4b43-acab-0cb772d016b1"},{"cancelled":false,"cause":"FOG","heading":58,"location":[9.1775267,48.7401501],"ts":1627532843001,"uuid":"41aa424d-c2d6-4112-9a8c-6076c4a1185b"},{"cancelled":false,"cause":"CW","heading":350,"location":
[9.162348999999999,48.740389799999996],"trace":[[9.162506899999999,48.739719199999996],
[9.162915299999998,48.738329099999994],[9.163371899999998,48.73750859999999],[9.164657199999997,48.73593839999999]],"ts":1627494700001,"uuid":"47608812-a27e-4bcf-80c0-b9ad157f71b0"},{"cancelled":false,"cause":"HL","heading":257,"location":[9.1460618,48.7293205],"trace":[[9.1442346,48.7290802],[9.1415567,48.728733],[9.1398878,48.7280235],[9.137647600000001,48.7280197]],"ts":1627525317362,
"uuid":"645ce31a-71aa-4dc0-a4ac-d952ddedc970"},{"cancelled":false,"cause":"HL","heading":165,"location":[9.146386099999999,48.7288284],"trace":[[9.1469955,48.729492099999995],[9.149906099999999,48.72990789999999],
[9.1504745,48.730148299999996],[9.150711,48.731063799999994]],"ts":1627494635316,"uuid":"6aff5cbb-dfc4-4ecc-bb95-50c65eacb3ea"},{"cancelled":false,"cause":"CW","heading":355,"location":[9.163257399999999,48.715576999999996],"trace":[[9.1635868,48.714011199999995],[9.1641202,48.712243199999996],[9.164879399999998,48.710528],[9.165867099999998,48.708844199999994]],
"ts":1627504915001,"uuid":"ab78d562-bd4d-4388-9eb6-a5da4e5e38fd"},{"cancelled":true,"cause":"HL",
"heading":172,"location":[9.1463422,48.7260437],"trace":[[9.1477861,48.7260627],[9.1490621,48.7264747],
[9.1497507,48.726844699999994],[9.1505689,48.72676839999999]],"ts":1627528506797,"uuid":"db4b9dba-82c9-4271-97d0-4083cd42b589"},{"cancelled":true,"cause":"HL","heading":348,"location":[9.1923816,48.7236738],"trace":[[9.1925081,48.723339],[9.1924879,48.723243200000006],[9.1923763,48.72326150000001],[9.1924221,48.723319800000006]],"ts":1627500567060,"uuid":"f08edd14-6ebd-48a1-86e6-7904668086be"}]}'
```

#### Example Hazard Warning with POST request using CURL

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


#### Example Fuel Status Tryout with POST request using CURL

The example below shows an example of Fuel Status POST request call which does not require authentication:


```
curl -d '{ "headers": { "authorization": " Bearer 7c7c777c-f123-4123-s123-7c7c777c7c77", "accept": "application/json;charset=utf-8" }, "optional": "WDB111111ZZZ22222/resources" }' -u 'user:password' -k -H "Content-Type: application/json" -X POST "<artifact_url>/data"
```

Example of reponse:

```
[
  {
    "name": "tanklevelpercent",
    "version": "1.0",
    "href": "/vehicles/WDB111111ZZZ22222/resources/tanklevelpercent"
  },
  {
    "name": "rangeliquid",
    "version": "1.0",
    "href": "/vehicles/WDB111111ZZZ22222/resources/rangeliquid"
  }
]

```



#### Example Eletric Vehicle Status Tryout with POST request using CURL

The example below shows an example of Eletric Vehicle StatusTryout which does not require authentication:

```
curl -d '{ "headers": { "authorization": "Bearer 2c2c222c-e123-4123-v123-2c2c222c2c22", "accept": "application/json;charset=utf-8" }, "optional": "WDB111111ZZZ22222/resources" }' -u 'user:password' -k -H "Content-Type: application/json" -X POST <artifact_url>/data"
```

Example of reponse:

```
[
  { "name": "soc", "version": "1.0", "href": "/vehicles/WDB111111ZZZ22222/resources/soc" },
  { "name": "rangeelectric", "version": "1.0", "href": "/vehicles/WDB111111ZZZ22222/resources/rangeelectric" }
]
```



