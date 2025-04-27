# new-telemetry-architecture

## SSCP - New Telemetry Architecture

## New Telemetry Architecture

Greg and I talked about the architecture of the new telemetry system

### Fundamental Features

* Be able to make changes to embedded code without making changes on the telemetry serverSignificantly reduce the tool-chain necessary to collect dataProvide useful  and incisive visualizations of the dataAllow for incorporation of external data into the server
* Be able to make changes to embedded code without making changes on the telemetry server
* Significantly reduce the tool-chain necessary to collect data
* Provide useful  and incisive visualizations of the data
* Allow for incorporation of external data into the server
* Be able to make changes to embedded code without making changes on the telemetry server
* Significantly reduce the tool-chain necessary to collect data
* Provide useful  and incisive visualizations of the data
* Allow for incorporation of external data into the server

Be able to make changes to embedded code without making changes on the telemetry server

Significantly reduce the tool-chain necessary to collect data

Provide useful  and incisive visualizations of the data

Allow for incorporation of external data into the server

### Sub-Projects

#### CAN Architecture

* High Level Features:Modify the existing CAN architecture to support type information and multi-packet messagesCreate a standardized protocol for querying parameters from connected devicesCreate an standardized embedded API for communications over the CAN busLow Level GoalsImplement extended identifiersImplement multi-packet messagesImplement a parameter catalog
* High Level Features:Modify the existing CAN architecture to support type information and multi-packet messagesCreate a standardized protocol for querying parameters from connected devicesCreate an standardized embedded API for communications over the CAN bus
* Modify the existing CAN architecture to support type information and multi-packet messages
* Create a standardized protocol for querying parameters from connected devices
* Create an standardized embedded API for communications over the CAN bus
* Low Level GoalsImplement extended identifiersImplement multi-packet messagesImplement a parameter catalog
* Implement extended identifiers
* Implement multi-packet messages
* Implement a parameter catalog
* High Level Features:Modify the existing CAN architecture to support type information and multi-packet messagesCreate a standardized protocol for querying parameters from connected devicesCreate an standardized embedded API for communications over the CAN bus
* Modify the existing CAN architecture to support type information and multi-packet messages
* Create a standardized protocol for querying parameters from connected devices
* Create an standardized embedded API for communications over the CAN bus
* Low Level GoalsImplement extended identifiersImplement multi-packet messagesImplement a parameter catalog
* Implement extended identifiers
* Implement multi-packet messages
* Implement a parameter catalog

High Level Features:

* Modify the existing CAN architecture to support type information and multi-packet messages
* Create a standardized protocol for querying parameters from connected devices
* Create an standardized embedded API for communications over the CAN bus

Modify the existing CAN architecture to support type information and multi-packet messages

Create a standardized protocol for querying parameters from connected devices

Create an standardized embedded API for communications over the CAN bus

Low Level Goals

* Implement extended identifiers
* Implement multi-packet messages
* Implement a parameter catalog

Implement extended identifiers

Implement multi-packet messages

Implement a parameter catalog

#### CAN Logger

* High Level Features:Send and receive CAN messagesDatabaseInterface with CAN hardwareParses messages and inserts them into the databaseLow level:Assemble stringsTimestampOn startup, constructs a table of devices that are currently connected to the CAN busOrganizes packets based on sender
* High Level Features:Send and receive CAN messagesDatabaseInterface with CAN hardwareParses messages and inserts them into the database
* Send and receive CAN messages
* Database
* Interface with CAN hardware
* Parses messages and inserts them into the database
* Low level:Assemble stringsTimestampOn startup, constructs a table of devices that are currently connected to the CAN busOrganizes packets based on sender
* Assemble strings
* Timestamp
* On startup, constructs a table of devices that are currently connected to the CAN bus
* Organizes packets based on sender
* High Level Features:Send and receive CAN messagesDatabaseInterface with CAN hardwareParses messages and inserts them into the database
* Send and receive CAN messages
* Database
* Interface with CAN hardware
* Parses messages and inserts them into the database
* Low level:Assemble stringsTimestampOn startup, constructs a table of devices that are currently connected to the CAN busOrganizes packets based on sender
* Assemble strings
* Timestamp
* On startup, constructs a table of devices that are currently connected to the CAN bus
* Organizes packets based on sender

High Level Features:

* Send and receive CAN messages
* Database
* Interface with CAN hardware
* Parses messages and inserts them into the database

Send and receive CAN messages

Database

Interface with CAN hardware

Parses messages and inserts them into the database

Low level:

* Assemble strings
* Timestamp
* On startup, constructs a table of devices that are currently connected to the CAN bus
* Organizes packets based on sender

Assemble strings

Timestamp

On startup, constructs a table of devices that are currently connected to the CAN bus

Organizes packets based on sender

#### Web Backend

* High Level Features:A web server for clients to connect to and be able to view information about the car.
* High Level Features:A web server for clients to connect to and be able to view information about the car.
* A web server for clients to connect to and be able to view information about the car.
* High Level Features:A web server for clients to connect to and be able to view information about the car.
* A web server for clients to connect to and be able to view information about the car.

High Level Features:

* A web server for clients to connect to and be able to view information about the car.

A web server for clients to connect to and be able to view information about the car.

* Low Level:DHCPRetrieves and sends requested data to and from the databaseSupports virtual Devices (Anemometer, Pyranometer)Sends CAN packets back to the car&#x20;
* DHCPRetrieves and sends requested data to and from the databaseSupports virtual Devices (Anemometer, Pyranometer)Sends CAN packets back to the car&#x20;
* DHCP
* Retrieves and sends requested data to and from the database
* Supports virtual Devices (Anemometer, Pyranometer)
* Sends CAN packets back to the car&#x20;

Low Level:

* DHCPRetrieves and sends requested data to and from the databaseSupports virtual Devices (Anemometer, Pyranometer)Sends CAN packets back to the car&#x20;
* DHCP
* Retrieves and sends requested data to and from the database
* Supports virtual Devices (Anemometer, Pyranometer)
* Sends CAN packets back to the car&#x20;
* DHCP
* Retrieves and sends requested data to and from the database
* Supports virtual Devices (Anemometer, Pyranometer)
* Sends CAN packets back to the car&#x20;

DHCP

Retrieves and sends requested data to and from the database

Supports virtual Devices (Anemometer, Pyranometer)

Sends CAN packets back to the car&#x20;

#### Web Frontend

* High Level Features:Manages the user interface and graphing utilitiesGet direct or averaged readings from any subsystem on the carGenerate visualizations of data with selectable independent and dependent variablesLow Level:Widgets AJAX?
* High Level Features:Manages the user interface and graphing utilitiesGet direct or averaged readings from any subsystem on the carGenerate visualizations of data with selectable independent and dependent variables
* Manages the user interface and graphing utilities
* Get direct or averaged readings from any subsystem on the car
* Generate visualizations of data with selectable independent and dependent variables
* Low Level:Widgets AJAX?
* Widgets&#x20;
* AJAX?
* High Level Features:Manages the user interface and graphing utilitiesGet direct or averaged readings from any subsystem on the carGenerate visualizations of data with selectable independent and dependent variables
* Manages the user interface and graphing utilities
* Get direct or averaged readings from any subsystem on the car
* Generate visualizations of data with selectable independent and dependent variables
* Low Level:Widgets AJAX?
* Widgets&#x20;
* AJAX?

High Level Features:

* Manages the user interface and graphing utilities
* Get direct or averaged readings from any subsystem on the car
* Generate visualizations of data with selectable independent and dependent variables

Manages the user interface and graphing utilities

Get direct or averaged readings from any subsystem on the car

Generate visualizations of data with selectable independent and dependent variables

Low Level:

* Widgets&#x20;
* AJAX?

Widgets&#x20;

AJAX?
