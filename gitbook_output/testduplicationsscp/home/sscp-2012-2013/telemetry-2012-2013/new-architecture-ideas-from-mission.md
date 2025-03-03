# SSCP - New Architecture Ideas (from Mission)

# New Architecture Ideas (from Mission)

We're planning to let each board manage its own catalog of measurements.

The telemetry clients (TelemLight and TelemLogger) will query the car not only for specific measurements, but also for metadata. This eliminates the problem of keeping the code on the various boards and the telem clients in sync. 

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

typedef struct catalog_entry {

    ...

} catentry_t;

bms_catalog.h

double bat_voltages[35];

static catentry_t cat_bat_voltages = {

    TRANSIENT,

    READONLY,

    14,

    FLOAT,

    35,

    &bat_voltages

};

...

static catentry_t catalog[] = {

    cat_board_version, //defined in catalog.h or something

    ...

    cat_array_current,

    cat_motor_current,

    cat_bat_voltages,

    ...

};

bms.c

...initialization code

announcer_send(&cat_array_current, 100); //send this every 100 ms

announcer_send(&cat_motor_current, 100);

announcer_ignore(&cat_lols); //don't auto send, don't monitor

announcer_verify(&cat_bat_voltages, 1000); //don't auto-send, but do verify that it's sent at least once a second

announcer_start(); //ALL ENTRIES IN CATALOG must be spec'd here, or it complains (any ignores should be explicit)

... query each module for voltages, wait for all of them to respond

cat_send(&cat_bat_voltages);

