# Example of POST request

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
