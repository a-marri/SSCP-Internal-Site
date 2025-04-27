# new-architecture-ideas-from-mission

## SSCP - New Architecture Ideas (from Mission)

## New Architecture Ideas (from Mission)

We're planning to let each board manage its own catalog of measurements.

The telemetry clients (TelemLight and TelemLogger) will query the car not only for specific measurements, but also for metadata. This eliminates the problem of keeping the code on the various boards and the telem clients in sync.&#x20;

We'll try to structure the code on the embedded side to minimize opportunities for fail (such as forgetting to send out a measurement) while making it as easy as possible to add measurements. Embedded software components

* Every device specifies a set of catalog entries (for example, the battery pack has one for module voltages)Each catalog entry represents a measurement or measurement arrayEach device also uses a set of generic catalog entries for things like board versionEach device has a catalog: a statically defined list of all supported entriesEach catalog entry has a lifetime: transient (RAM-only) or persistent (Flash or battery-backed SRAM)Each catalog entry is either readonly or writeable via the CAN bus.The embedded lib takes care of CAN message queueing, interfacing with the CAN chip, etcThe embedded lib includes an announcer, a FreeRTOS thread which can auto-publish each measurement every X millisecs
* Every device specifies a set of catalog entries (for example, the battery pack has one for module voltages)
* Each catalog entry represents a measurement or measurement array
* Each device also uses a set of generic catalog entries for things like board version
* Each device has a catalog: a statically defined list of all supported entries
* Each catalog entry has a lifetime: transient (RAM-only) or persistent (Flash or battery-backed SRAM)
* Each catalog entry is either readonly or writeable via the CAN bus.
* The embedded lib takes care of CAN message queueing, interfacing with the CAN chip, etc
* The embedded lib includes an announcer, a FreeRTOS thread which can auto-publish each measurement every X millisecs
* Every device specifies a set of catalog entries (for example, the battery pack has one for module voltages)
* Each catalog entry represents a measurement or measurement array
* Each device also uses a set of generic catalog entries for things like board version
* Each device has a catalog: a statically defined list of all supported entries
* Each catalog entry has a lifetime: transient (RAM-only) or persistent (Flash or battery-backed SRAM)
* Each catalog entry is either readonly or writeable via the CAN bus.
* The embedded lib takes care of CAN message queueing, interfacing with the CAN chip, etc
* The embedded lib includes an announcer, a FreeRTOS thread which can auto-publish each measurement every X millisecs

Every device specifies a set of catalog entries (for example, the battery pack has one for module voltages)

Each catalog entry represents a measurement or measurement array

Each device also uses a set of generic catalog entries for things like board version

Each device has a catalog: a statically defined list of all supported entries

Each catalog entry has a lifetime: transient (RAM-only) or persistent (Flash or battery-backed SRAM)

Each catalog entry is either readonly or writeable via the CAN bus.

The embedded lib takes care of CAN message queueing, interfacing with the CAN chip, etc

The embedded lib includes an announcer, a FreeRTOS thread which can auto-publish each measurement every X millisecs

* The embedded lib is shared across all devices on the car

The embedded lib is shared across all devices on the car

catalog.h

...

typedef struct catalog\_entry {

&#x20;   ...

} catentry\_t;

bms\_catalog.h

double bat\_voltages\[35];

static catentry\_t cat\_bat\_voltages = {

&#x20;   TRANSIENT,

&#x20;   READONLY,

&#x20;   14,

&#x20;   FLOAT,

&#x20;   35,

&#x20;   \&bat\_voltages

};

...

static catentry\_t catalog\[] = {

&#x20;   cat\_board\_version, //defined in catalog.h or something

&#x20;   ...

&#x20;   cat\_array\_current,

&#x20;   cat\_motor\_current,

&#x20;   cat\_bat\_voltages,

&#x20;   ...

};

bms.c

...initialization code

announcer\_send(\&cat\_array\_current, 100); //send this every 100 ms

announcer\_send(\&cat\_motor\_current, 100);

announcer\_ignore(\&cat\_lols); //don't auto send, don't monitor

announcer\_verify(\&cat\_bat\_voltages, 1000); //don't auto-send, but do verify that it's sent at least once a second

announcer\_start(); //ALL ENTRIES IN CATALOG must be spec'd here, or it complains (any ignores should be explicit)

... query each module for voltages, wait for all of them to respond

cat\_send(\&cat\_bat\_voltages);
