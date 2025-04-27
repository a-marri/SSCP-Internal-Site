# embedded-programmer

## SSCP - Embedded Programmer

## Embedded Programmer

&#x20;

### Setting up a Project to Use Dandelion&#x20;

### Using the Embedded Libraries

If your starter project already included the catalog code, all you have to do is:

* Call catInitializeCatalog, passing it your Catalog variable and the device ID.  Create and register all of your catalog variables (see below for details).Finish initialization by calling catFinishInit and passing the (human-parseable) name of the board.Create both the catalog broadcast task and the catalog receive task.Finally, start your scheduler.  Go!
* Call catInitializeCatalog, passing it your Catalog variable and the device ID. &#x20;
* Create and register all of your catalog variables (see below for details).
* Finish initialization by calling catFinishInit and passing the (human-parseable) name of the board.
* Create both the catalog broadcast task and the catalog receive task.
* Finally, start your scheduler.  Go!
* Call catInitializeCatalog, passing it your Catalog variable and the device ID. &#x20;
* Create and register all of your catalog variables (see below for details).
* Finish initialization by calling catFinishInit and passing the (human-parseable) name of the board.
* Create both the catalog broadcast task and the catalog receive task.
* Finally, start your scheduler.  Go!

Call catInitializeCatalog, passing it your Catalog variable and the device ID. &#x20;

Create and register all of your catalog variables (see below for details).

Finish initialization by calling catFinishInit and passing the (human-parseable) name of the board.

Create both the catalog broadcast task and the catalog receive task.

Finally, start your scheduler.  Go!

If your project didn't already include catalog code you must first have done the following:

* Start with a FreeRTOS project for an STM32F2 or F4.Include lib/drivers/catalog.h and lib/drivers/catalog.c in your project.#include "catalog.h" in global.h.Copy the entire section of global.h labeled "Catalog Variables".Set the device ID to be unique on the bus.Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.Initialize the CAN Tx and Rx queues.Copy the interrupt handler for receiving CAN messages (CAN1\_RX0\_IRQHandler in STM32f2xx\_it.c or STM32f4xx\_it.c)
* Start with a FreeRTOS project for an STM32F2 or F4.
* Include lib/drivers/catalog.h and lib/drivers/catalog.c in your project.
* \#include "catalog.h" in global.h.
* Copy the entire section of global.h labeled "Catalog Variables".Set the device ID to be unique on the bus.Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.
* Set the device ID to be unique on the bus.
* Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.
* Initialize the CAN Tx and Rx queues.
* Copy the interrupt handler for receiving CAN messages (CAN1\_RX0\_IRQHandler in STM32f2xx\_it.c or STM32f4xx\_it.c)
* Start with a FreeRTOS project for an STM32F2 or F4.
* Include lib/drivers/catalog.h and lib/drivers/catalog.c in your project.
* \#include "catalog.h" in global.h.
* Copy the entire section of global.h labeled "Catalog Variables".Set the device ID to be unique on the bus.Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.
* Set the device ID to be unique on the bus.
* Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.
* Initialize the CAN Tx and Rx queues.
* Copy the interrupt handler for receiving CAN messages (CAN1\_RX0\_IRQHandler in STM32f2xx\_it.c or STM32f4xx\_it.c)

Start with a FreeRTOS project for an STM32F2 or F4.

Include lib/drivers/catalog.h and lib/drivers/catalog.c in your project.

\#include "catalog.h" in global.h.

Copy the entire section of global.h labeled "Catalog Variables".

* Set the device ID to be unique on the bus.
* Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.

Set the device ID to be unique on the bus.

Make sure that any variables declared as extern in global.h (such as time) are defined in main.c in the section labeled "Global Variables".  For a good discussion of the meaning of the extern keyword, read the first response to this question.

[this question](http://stackoverflow.com/questions/1433204/what-are-extern-variables-in-c)

Initialize the CAN Tx and Rx queues.

Copy the interrupt handler for receiving CAN messages (CAN1\_RX0\_IRQHandler in STM32f2xx\_it.c or STM32f4xx\_it.c)

#### Creating A New Catalog Entry

* Register each catalog variable by calling catInitEntry.  The variable must be defined as static so that it will persist.  This function needs the following information:The CatalogThe type ID of the variable, as defined in catalog.h and on this websiteThe variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.The name of the variable.  See below for formatting information.The length of the entry (1 unless it is an array; otherwise the length of an array).The address of the variable.
* Register each catalog variable by calling catInitEntry.  The variable must be defined as static so that it will persist.  This function needs the following information:The CatalogThe type ID of the variable, as defined in catalog.h and on this websiteThe variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.The name of the variable.  See below for formatting information.The length of the entry (1 unless it is an array; otherwise the length of an array).The address of the variable.
* The Catalog
* The type ID of the variable, as defined in catalog.h and on this website
* The variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.
* Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.
* The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.
* The name of the variable.  See below for formatting information.
* The length of the entry (1 unless it is an array; otherwise the length of an array).
* The address of the variable.
* Register each catalog variable by calling catInitEntry.  The variable must be defined as static so that it will persist.  This function needs the following information:The CatalogThe type ID of the variable, as defined in catalog.h and on this websiteThe variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.The name of the variable.  See below for formatting information.The length of the entry (1 unless it is an array; otherwise the length of an array).The address of the variable.
* The Catalog
* The type ID of the variable, as defined in catalog.h and on this website
* The variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.
* Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.
* The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.
* The name of the variable.  See below for formatting information.
* The length of the entry (1 unless it is an array; otherwise the length of an array).
* The address of the variable.

Register each catalog variable by calling catInitEntry.  The variable must be defined as static so that it will persist.  This function needs the following information:

[static](http://en.wikipedia.org/wiki/Static_variable)

* The Catalog
* The type ID of the variable, as defined in catalog.h and on this website
* The variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.
* Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.
* The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.
* The name of the variable.  See below for formatting information.
* The length of the entry (1 unless it is an array; otherwise the length of an array).
* The address of the variable.

The Catalog

The type ID of the variable, as defined in catalog.h and on this website

The variable ID, which should be a number between 0x21 and 0xFF.  Lower numbers are reserved for catalog use.

Flags--writable, nonvolatile, or transient, or NO\_FLAGS to explicitly disable all flags.

The announce frequency in milleseconds, or NO\_ANNOUNCE for variables that you want to be able to send without always broadcasting them.  You might use NO\_ANNOUNCE for state variables and only announce them when they change.

The name of the variable.  See below for formatting information.

The length of the entry (1 unless it is an array; otherwise the length of an array).

The address of the variable.

#### Variable Naming Conventions

Names should be in the format name#units.  The name should be human-readable.  Spaces are allowed.  All characters after the last # will be interpreted as units.  Keep in mind that the name will often be displayed in a narrow vertical bar, so make it short and sweet.

Enums:

Names of enums have special properties which are similar to bit fields. Enums support informing the telemetry server of the human readable values that get parsed to strings. Enum names are in the form of name#units@0:State0&1:State1

All information after the question mark is used to parse what each value corresponds to and are of the form number:State corresponding to that number. The numbers do not have to be single digits or in order however the total length of the name string must be shorter than 2048 characters which is the maximum String size supported by the can protocol. For more information see the pages on telemetry architecture.&#x20;

#### Internal Catalog Structure

Two new structs were introduced for interfacing with the catalog.  The first is the Catalog struct, which holds information about the catalog as a whole--the number of variables, the device ID, and the list of entries.  The second is the Entry struct, which encapsulated information about a specific entry in the catalog.  This includes the type of the entry, the name, array length, and a pointer to the variable or array of variables.  The Catalog stores the head of a linked list of Entry structs.  Calls into the catalog library always require a pointer to a Catalog and sometimes require a pointer to an Entry.

#### Force Announce

If you've changed a variable and want to announce that change on the bus immediately, rather than waiting for the regular broadcast interval, you can call catBroadcastValue after your update.  To call this function you need a pointer to the Entry for the relevant variable.  You can get this by capturing the return value of catInitEntry at initialization.  Immediate broadcasts do not change the normal variable broadcast schedule.

### Common Mistakes

Device IDs on the same bus must be unique.  If you have two light boards or two MPPTs, make sure their IDs are different.

Array length should be 1, not zero, if you variable is not actually an array.
