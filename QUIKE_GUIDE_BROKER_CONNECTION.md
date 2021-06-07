# Broker Connection Quick Guide

On this page, we break down the International Data Space (IDS) infrastructure and modus operandi.
This document is structured as follows.
Next section details all necessary steps to initiate a connection to an IDS Broker using the IDS Connector.
Following, there is a list of common IDS Broker Connection Addresses as well as Web Interfaces.
Lastly, there is a list of useful contacts for requesting access or reporting problems on different IDS components.

# Connecting to an IDS Broker

There are three steps for connecting to an IDS Broker: (1) request and register your trusted key, (2) Setting up a trusted key (certificate) in an IDS Connector, and (3) Requesting connection access to an IDS Broker. In the following, we elucidate each of those steps.

## Requesting a trusted key (certificate) and Connector ID

The communication between the different IDS components is performed using a secure communication channel. 
To be able to either connect or transfer data between an IDS component one may request a trusted key to the IDS Consortium.
To do so, you may contact 

## Configuring an IDS Connector with a trusted key and Connector ID

With the trusted key in your hands, it's time to set it up into your IDS Connector.
The IDS Connector comes with a default setup for connecting to the test.
In the image below, we show two configurations of the ```config.json``` file located in ```src/main/resources/conf``` directory.
You should customize it adding resp. your trusted key and Connector ID.
The customized configuration is shown on the left-hand side of the image while the default configuration on the right-hand side.
The customized fields are also highlighted for easy reading.

The customized fields are also highlighted for easy reading.
There are three fields that should be changed: (1) the ```@id``` of the ```ids:connectorDeployMode```, (2) the ```@id``` of the ```ids:connectorDescription```, (3) the ```@id``` of the ```ids:keyStore``` as follows: 
The customized fields are also highlighted for easy reading.
 * Change the ```@id``` of the ```ids:connectorDeployMode``` to ```idsc:PRODUCTIVE_DEPLOYMENT```;
 * Change the ```@id``` of the ```ids:connectorDescription``` by the id of your IDS Connector preserving the path ```https://w3id.org/idsa/autogen/baseConnector/``` (see the example below), provided by the International Dataspace in the previous step;
 * Change the ```@id``` of the ```ids:keyStore``` to the key provided by the International Dataspace in the previous step.

Optional (but important): The IDS Connector allows the configuration of ```Proxy```, in case your connector is hosted in a closed network.
You can setup the ```Proxy``` changing the parameter ```ids:connectorProxy``` accordingly. If this is not your case, you should remove the default parameters  ```ids:connectorProxy``` leaving only the parameter ```ids:noProxy``` (see the example below).

Below we side by side an ```example``` configuration in the left hand side and the ```default``` configuration in the right handside.

![Example config.json](https://github.com/eccenca/DataspaceConnector/blob/develop/connector_configuration_example.png)

## Requesting Connection Access

Some of the IDS Brokers requires an <b>IP Unblockage</b> or a <b>formal notification</b> before a connection takes place.
If you are unable to connect even after setting up your trusted key, this might be the reason.
Next section compiles a list of Brokers, their resp. connection addresses and main mantainers.
You can request a <b>IP Unblockage</b> or <b>connection</b> allowance writing to the Broker's respective contact.

# IDS Brokers

## Production Deployment

| Broker | Web Interface | Connection Address | Requires IP Unblockage | Version | Model Compatibility | Mantainer | Contact |
| ------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Mobility Dataspace | https://mobilitydataspace.io/browse | https://ids.mobilitydataspace.io/infrastructure |  YES | ? | ? |Fraunhofer IVI | sebastian.lorenz@ivi.fraunhofer.de |
| IDS Metadata Broker | https://broker.ids.isst.fraunhofer.de/browse | https://broker.ids.isst.fraunhofer.de/infrastructure |  YES | ? | ? | Fraunhofer ISST | info@dataspace-connector.de |

## Test Deployment

Broker | Web Interface | Connection Address | Requires IP Unblockage | Version | Model Compatibility | Mantainer | Contact
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
Test Mobility Dataspace | https://broker.test.mobilitydataspace.io | https://test.ids.mobilitydataspace.io/connector | YES | ? | ? | Fraunhofer IVI | sebastian.lorenz@ivi.fraunhofer.de 

# Infrastructure & Contacts 

## Developers

Name | Contact | Component | Repository
------------ | ------------- | ------------- | -------------
Julia Pampus | julia.pampus@isst.fraunhofer.de | IDS Connector | https://github.com/International-Data-Spaces-Association/DataspaceConnector
Mattias Boeckmann | matthias.boeckmann@iais.fraunhofer.de | IDS Broker | https://github.com/International-Data-Spaces-Association/metadata-broker-open-core
Johannes Lipp | johannes.lipp@fit.fraunhofer.de  | Information Model | ?
