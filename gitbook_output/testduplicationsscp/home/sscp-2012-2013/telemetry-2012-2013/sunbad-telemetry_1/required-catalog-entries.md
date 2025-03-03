# SSCP - Required Catalog Entries

# Required Catalog Entries

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

Entries that are not required (board-specific variables) should start at varID 0x20.

## Catalog protocol version

[](#h.bzlfmubeo849)

Monotonically increasing protocol version number. Starts at 0, currently at 0. If we change the message format or other parameters of the catalog (ie, required parameters), this number will be incremented.

## Catalog hash

[](#h.800yhtlux9b7)

This is a CRC32 (uint32) of the nonvolatile content of the catalog. It serves as a means to detect changes in the catalog, thus triggering the telemetry server or other client to refresh its local cache of catalog entries for a specific board.

## Array of in-use identifiers

[](#h.v66h0gr3a51f)

This allows the telemetry system, or any other client, to quickly determine which variable identifiers are in-use. This makes it possible to query a (possibly small) fraction of the total variable namespace.

## Board name

[](#h.8wzdn4x1lxuu)

Simply the name of the board. Possible examples include "BMS" or "Driver controls".

## Board hardware version

[](#h.1amo7cx8bv42)

Two pins on the processor are dedicated for setting the hardware revision using a weak/strong pull up/down resistor. It allows the telemetry system to make notes of when hardware versions change in the logs, giving us better insight in to how changes to the vehicle platform affect its performance.

## Board serial number

[](#h.r8mi5ed8i4m5)

Unique board serial numbers for a given hardware version allow us to track issues unique to a certain piece of hardware. It also allows us to differentiate between multiple copies of a board on the car. For example, there may be multiple MPPTs or light controllers.

## Software hash

[](#h.mwxz4h3yq309)

This lets us keep track of which versions of software might be causing issues, or see when something may have been flashed with new code. It's also a fast safeguard against program corruption.

## System time

[](#h.n456g5rbnlh3)

Time since board startup, in microseconds.

## Request reboot

[](#h.53lx8xw4mhh8)

Writing a value to this variable will request a reboot and write the requested value to the backup SRAM. This can be used to enter a bootloader.

## Save catalog to flash

[](#h.r81ttrjw8pu8)

Setting this bool will instruct the embedded software that it needs to save nonvolatile entries to flash. Once completed, this variable will reset.

