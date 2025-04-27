# telemetry-database

## SSCP - Telemetry Database

## Telemetry Database

The telemetry database has the following tables.

* messages - contains all CAN messages we've received, one per row. values - contains all CAN values. Remember that one message may carry multiple values--for example, battery pack voltage and current. So for every CAN message we receive, multiple rows may be added to this table.measurements - contains the CAN protocol--in other words, the list of measurements that we support. So "battery\_pack.current" corresponds to one row in this table. trips - one row for each "trip", which is just for organization. Eg, "WSC 2011 Day 3" might be a trip.latest\_vals - caches the latest value we've gotten for each measurement.&#x20;
* messages - contains all CAN messages we've received, one per row.&#x20;
* values - contains all CAN values. Remember that one message may carry multiple values--for example, battery pack voltage and current. So for every CAN message we receive, multiple rows may be added to this table.
* measurements - contains the CAN protocol--in other words, the list of measurements that we support. So "battery\_pack.current" corresponds to one row in this table.&#x20;
* trips - one row for each "trip", which is just for organization. Eg, "WSC 2011 Day 3" might be a trip.
* latest\_vals - caches the latest value we've gotten for each measurement.&#x20;
* messages - contains all CAN messages we've received, one per row.&#x20;
* values - contains all CAN values. Remember that one message may carry multiple values--for example, battery pack voltage and current. So for every CAN message we receive, multiple rows may be added to this table.
* measurements - contains the CAN protocol--in other words, the list of measurements that we support. So "battery\_pack.current" corresponds to one row in this table.&#x20;
* trips - one row for each "trip", which is just for organization. Eg, "WSC 2011 Day 3" might be a trip.
* latest\_vals - caches the latest value we've gotten for each measurement.&#x20;

messages - contains all CAN messages we've received, one per row.&#x20;

values - contains all CAN values. Remember that one message may carry multiple values--for example, battery pack voltage and current. So for every CAN message we receive, multiple rows may be added to this table.

measurements - contains the CAN protocol--in other words, the list of measurements that we support. So "battery\_pack.current" corresponds to one row in this table.&#x20;

trips - one row for each "trip", which is just for organization. Eg, "WSC 2011 Day 3" might be a trip.

latest\_vals - caches the latest value we've gotten for each measurement.&#x20;
