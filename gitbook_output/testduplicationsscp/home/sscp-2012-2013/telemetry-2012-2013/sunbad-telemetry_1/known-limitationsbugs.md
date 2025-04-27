# known-limitationsbugs

## SSCP - Known Limitations/Bugs

## Known Limitations/Bugs

### Graphing

### Front End

### Catalog Assembler

#### Can Bus overflow

Currently the code tries to get devices and parameters concurrently, this could overwhelm the can bus wiht too many requests on startup. Better flow control should be implimented in the catalog building code

### Embedded Code

Locking isn't set up properly.  Mostly we're doing operations on words, so it's fine--a get request will just work.  I need to make set a critical segment, but I also need to make sure that users know to lock their reads and writes from variables in their own critical segments.  What we have right now is no worse than the previous system with interrupts, but it's not going to do any better yet.

The user is still responsible for more things than I like:

* Initializing the CanTxQueue and the CanRxQueue.Setting up the interrupt handlerCreating the broadcast and receive tasks
* Initializing the CanTxQueue and the CanRxQueue.
* Setting up the interrupt handler
* Creating the broadcast and receive tasks
* Initializing the CanTxQueue and the CanRxQueue.
* Setting up the interrupt handler
* Creating the broadcast and receive tasks

Initializing the CanTxQueue and the CanRxQueue.

Setting up the interrupt handler

Creating the broadcast and receive tasks

Automatic CAN initialization still fails for an F4

Things to change as a result of review:

* Architecture: Pull announcer out of catalog, make it its own list.Include isAnnounced flagMake CRC32 less fragile: do not rely on magic '5'. Possibly use an overprovisioned array to hold struct elements (assigned by name!).Use a wrapper function to handle resetting the CRC32 peripheral (avoid using bool reset)Rename short #define constants to include CAT\_ RR 9/1/12Get rid of strlen in write\_string(): this leads to possibility of infinitely shortening the string upon multiple remote write. Prefer preallocating, consider using realloc.Shorten most data types in the entry struct to be uint8 (as appropriate) except length, which should be at least uint16Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwiseArbitrary use of \_T and not \_T on typeID is weird. Sasha recommends ditching the \_T everywhere. RR 9/1/12Add function to find entry\* based on variable pointerWrite a CAN driver, use it. Later.No need to allow assembleID to make non-catalog IDsReconsider where to place for-loop for sending array entries (currently in announcer) to simplify code through greater reuseRewrite catUpdate to take a void\*
* Architecture: Pull announcer out of catalog, make it its own list.Include isAnnounced flag
* Include isAnnounced flag
* Make CRC32 less fragile: do not rely on magic '5'. Possibly use an overprovisioned array to hold struct elements (assigned by name!).
* Use a wrapper function to handle resetting the CRC32 peripheral (avoid using bool reset)
* Rename short #define constants to include CAT\_ RR 9/1/12
* Get rid of strlen in write\_string(): this leads to possibility of infinitely shortening the string upon multiple remote write. Prefer preallocating, consider using realloc.
* Shorten most data types in the entry struct to be uint8 (as appropriate) except length, which should be at least uint16Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise
* Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise
* Arbitrary use of \_T and not \_T on typeID is weird. Sasha recommends ditching the \_T everywhere. RR 9/1/12
* Add function to find entry\* based on variable pointer
* Write a CAN driver, use it. Later.
* No need to allow assembleID to make non-catalog IDs
* Reconsider where to place for-loop for sending array entries (currently in announcer) to simplify code through greater reuse
* Rewrite catUpdate to take a void\*
* Architecture: Pull announcer out of catalog, make it its own list.Include isAnnounced flag
* Include isAnnounced flag
* Make CRC32 less fragile: do not rely on magic '5'. Possibly use an overprovisioned array to hold struct elements (assigned by name!).
* Use a wrapper function to handle resetting the CRC32 peripheral (avoid using bool reset)
* Rename short #define constants to include CAT\_ RR 9/1/12
* Get rid of strlen in write\_string(): this leads to possibility of infinitely shortening the string upon multiple remote write. Prefer preallocating, consider using realloc.
* Shorten most data types in the entry struct to be uint8 (as appropriate) except length, which should be at least uint16Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise
* Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise
* Arbitrary use of \_T and not \_T on typeID is weird. Sasha recommends ditching the \_T everywhere. RR 9/1/12
* Add function to find entry\* based on variable pointer
* Write a CAN driver, use it. Later.
* No need to allow assembleID to make non-catalog IDs
* Reconsider where to place for-loop for sending array entries (currently in announcer) to simplify code through greater reuse
* Rewrite catUpdate to take a void\*

Architecture: Pull announcer out of catalog, make it its own list.

* Include isAnnounced flag

Include isAnnounced flag

Make CRC32 less fragile: do not rely on magic '5'. Possibly use an overprovisioned array to hold struct elements (assigned by name!).

Use a wrapper function to handle resetting the CRC32 peripheral (avoid using bool reset)

Rename short #define constants to include CAT\_ RR 9/1/12

Get rid of strlen in write\_string(): this leads to possibility of infinitely shortening the string upon multiple remote write. Prefer preallocating, consider using realloc.

Shorten most data types in the entry struct to be uint8 (as appropriate) except length, which should be at least uint16

* Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise

Variable length will always be the real, fully hydrated length. Index will refer to chunks for strings and will 1:1 map otherwise

Arbitrary use of \_T and not \_T on typeID is weird. Sasha recommends ditching the \_T everywhere. RR 9/1/12

Add function to find entry\* based on variable pointer

Write a CAN driver, use it. Later.

No need to allow assembleID to make non-catalog IDs

Reconsider where to place for-loop for sending array entries (currently in announcer) to simplify code through greater reuse

Rewrite catUpdate to take a void\*

### Logger

Embedded side fails silently when an entry ID is used twice.  It uses the info from the first one created because of the linked list implementation, but this is a side effect and should not be relied upon.

Float->double conversion will have some loss of accuracy.  We'll have to do math to know where this will cause problems.

Timestamps are inaccurate--java/c problem?

Aggregator is written in C.

### Server/Backend

### Database

#### Consistency

Devices Consistency

Right now when a device is removed from the car it is not removed form the catalog. Eventually the databse should check all the id's that the car gets to make sure only the devices that are current are shown in the catalog.&#x20;
