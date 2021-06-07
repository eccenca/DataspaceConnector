<h1 align="center">
  <br>
  <a href="https://dataspace-connector.de/dsc_logo.svg"><img src="https://dataspace-connector.de/dsc_logo.svg" alt="Dataspace Connector Logo" width="200"></a>
  <br>
      Dataspace Connector
  <br>
</h1>


<p align="center">
  <a href="mailto:info@dataspace-connector.de">Contact</a> •
  <a href="#contributing">Contribute</a> •
  <a href="https://international-data-spaces-association.github.io/DataspaceConnector/">Docs</a> •
  <a href="https://github.com/FraunhoferISST/DataspaceConnector/issues">Issues</a> •
  <a href="#license">License</a>
</p>


The Dataspace Connector is an implementation of an IDS connector component following the
[IDS Reference Architecture Model](https://www.internationaldataspaces.org/wp-content/uploads/2019/03/IDS-Reference-Architecture-Model-3.0.pdf).
It integrates the [IDS Information Model](https://github.com/International-Data-Spaces-Association/InformationModel)
and uses the [IDS Connector Framework](https://github.com/FraunhoferISST/IDS-Connector-Framework)
for IDS functionalities and message handling.
The core component in this repository provides a REST API for loading, updating, and deleting
resources with local or remote data enriched by its metadata. It supports IDS conform message
handling with other IDS connectors and components and implements usage control for selected IDS
usage policy patterns.

***

<h3 align="center" >
  <a href="https://international-data-spaces-association.github.io/DataspaceConnector/">
    Manual & Documentation
  </a>
</h3>

***
## Quick Start

### Initializing

If you want to build and run locally, ensure that at least Java 11 is installed. Then, follow these steps:

1.  Clone this repository.
2.  Execute `cd DataspaceConnector` and `./mvnw clean package`.
3.  Navigate to `/target` and run `java -jar dataspaceconnector-{VERSION}.jar`.
4.  If everything worked fine, the connector is available at https://localhost:8080/. The API can
    be accessed at https://localhost:8080/api. The Swagger UI can be found at https://localhost:8080/api/docs.

For more details, see [here](https://international-data-spaces-association.github.io/DataspaceConnector/).

### Connecting to an IDS Broker

To connect to an IDS Broker consult the [Broker Connection Quick Guide](./QUIDE_GUIDE_BROKER_CONNECTION.md). 

## Contributing

You are very welcome to contribute to this project when you find a bug, want to suggest an
improvement, or have an idea for a useful feature. Please find a set of guidelines at the
[CONTRIBUTING.md](CONTRIBUTING.md) and the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Developers

This is an ongoing project of the [Data Economy](https://www.isst.fraunhofer.de/en/business-units/data-economy.html)
business unit of the [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html).

The core development is driven by
* [Heinrich Pettenpohl](https://github.com/HeinrichPet), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html), Project Manager
* [Julia Pampus](https://github.com/juliapampus), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html), Lead Developer
* [Brian-Frederik Jahnke](https://github.com/brianjahnke), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)
* [Ronja Quensel](https://github.com/ronjaquensel), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)

with significant contributions, comments, and support by (in alphabetical order):
* [Haydar Qarawlus](https://github.com/hqarawlus), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)
* [Johannes Pieperbeck](https://github.com/jpieperbeck), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)
* [René Brinkhege](https://github.com/renebrinkhege), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)
* [Steffen Biehs](https://github.com/steffen-biehs), [Fraunhofer ISST](https://www.isst.fraunhofer.de/en.html)

## License
Copyright © 2020 Fraunhofer ISST. This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) for details.
