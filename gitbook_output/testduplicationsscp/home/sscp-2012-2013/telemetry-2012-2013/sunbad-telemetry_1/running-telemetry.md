# running-telemetry

## SSCP - Running Telemetry

## Running Telemetry

### Dependencies

* Java v7 or greaterCan USB or dedicated telemetry hardwareMaven (not required for logger or can client/server)
* Java v7 or greater
* Can USB or dedicated telemetry hardware
* Maven (not required for logger or can client/server)
* Java v7 or greater
* Can USB or dedicated telemetry hardware
* Maven (not required for logger or can client/server)

Java v7 or greater

Can USB or dedicated telemetry hardware

Maven (not required for logger or can client/server)

### Running the Can Server and Can Client

### Running Logger

* Navigate to sunbad->software-telemetry->release->logger-(highest number of release)Open the config.properties fileUpdate the fields necessary to connect to a sql serverUpdate the can\_server field to the ip address of the device running the can serverTo run the packaged jar in the terminal type java -jar logger-(number of highest release).jar config.propertiesThe logger will spit out information about the can messages it receives during building the catalog. If the catalog is successfully built the logger will print out the names of the messages that it inserts into the database.&#x20;
* Navigate to sunbad->software-telemetry->release->logger-(highest number of release)
* Open the config.properties fileUpdate the fields necessary to connect to a sql serverUpdate the can\_server field to the ip address of the device running the can server
* Update the fields necessary to connect to a sql server
* Update the can\_server field to the ip address of the device running the can server
* To run the packaged jar in the terminal type java -jar logger-(number of highest release).jar config.properties
* The logger will spit out information about the can messages it receives during building the catalog. If the catalog is successfully built the logger will print out the names of the messages that it inserts into the database.&#x20;

1. Navigate to sunbad->software-telemetry->release->logger-(highest number of release)
2. Open the config.properties fileUpdate the fields necessary to connect to a sql serverUpdate the can\_server field to the ip address of the device running the can server
3. Update the fields necessary to connect to a sql server
4. Update the can\_server field to the ip address of the device running the can server
5. To run the packaged jar in the terminal type java -jar logger-(number of highest release).jar config.properties
6. The logger will spit out information about the can messages it receives during building the catalog. If the catalog is successfully built the logger will print out the names of the messages that it inserts into the database.&#x20;

Navigate to sunbad->software-telemetry->release->logger-(highest number of release)

Open the config.properties file

1. Update the fields necessary to connect to a sql server
2. Update the can\_server field to the ip address of the device running the can server

Update the fields necessary to connect to a sql server

Update the can\_server field to the ip address of the device running the can server

To run the packaged jar in the terminal type java -jar logger-(number of highest release).jar config.properties

The logger will spit out information about the can messages it receives during building the catalog. If the catalog is successfully built the logger will print out the names of the messages that it inserts into the database.&#x20;

### Running the Backend Server

* Navigate to sunbad->software-telemetry->releases->dandelion-(highest number of release)In the terminal type mvn jetty:run
* Navigate to sunbad->software-telemetry->releases->dandelion-(highest number of release)
* In the terminal type mvn jetty:run

1. Navigate to sunbad->software-telemetry->releases->dandelion-(highest number of release)
2. In the terminal type mvn jetty:run

Navigate to sunbad->software-telemetry->releases->dandelion-(highest number of release)

In the terminal type mvn jetty:run
