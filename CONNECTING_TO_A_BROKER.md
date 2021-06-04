# How to connect to a broker

In this page we breake down the International Data Space (IDS) infrastructure and modus operandi.
This document is structured as follows.
Next section details all necessary steps to initiate a connection to an IDS Broker.
Following there is a list of common IDS Broker Connection Addresses as well as Web Interfaces.
Lastly, there are a list of useful contacts for requesting access or reporting problems on different IDS Brokers.

# Connecting to a broker

  There are three steps for connecting to an IDS Broker: (1) request and register your trusted key, (2) Setting up a trusted key in an IDS Connector, and (3)         Requesting connection access to an IDS Broker. In the following we elucidade each one of those steps.

## Requesting a trusted key

   The communication between the different IDS components is performed using a secure communication channel. 
   To be able to either connect or trasfer data between an IDS component one may request a trusted key to the IDS Consortium.
   To do so, you may contact 

## Configuring a the IDS Connector with a trusted key

With the trusted key in your hands, its time to set it up into your IDS Connector.
The IDS Connector comes with a default setup for connecting to the test

## Requesting Connection Access

Some of the IDS Brokers requires an IP unblockage or to be formaly notified before connections take place.
If you are unable to connect even after setting up your trusted key, this might be the reason.
Next section compiles a list of brokers their resp. connection addresses and main mantainers.
You can request a IP Unblockage writing to the broker's respective contact.

# IDS Brokers

## Production Deployment

Broker | Web Interface | Connection Address | Requires IP unblockage | Mantainer | Contact
------------ | ------------- | ------------- | ------------- | ------------- | -------------
Mobility Dataspace | https://mobilitydataspace.io/browse | https://ids.mobilitydataspace.io/infrastructure | NO | Fraunhofer IVI | sebastian.lorenz@ivi.fraunhofer.de 
IDS Metadata Broker | https://broker.ids.isst.fraunhofer.de/browse | https://broker.ids.isst.fraunhofer.de/infrastructure | YES | Fraunhofer ISST | info@dataspace-connector.de

## Test Deployment

Broker | Web Interface | Connection Address | Version 
------------ | ------------- | ------------- | -------------
Test Mobility Dataspace | https://broker.test.mobilitydataspace.io | https://test.ids.mobilitydataspace.io/connector | ?

# Infrastructure & Contacts 

## Developers

Name | Contact | Component | Repository
------------ | ------------- | ------------- | -------------
Julia Pampus | julia.pampus@isst.fraunhofer.de | IDS Connector | https://github.com/International-Data-Spaces-Association/DataspaceConnector
Mattias Boeckmann | matthias.boeckmann@iais.fraunhofer.de | IDS Broker | https://github.com/International-Data-Spaces-Association/metadata-broker-open-core
Johannes Lipp | johannes.lipp@fit.fraunhofer.de  | Information Model | ?
