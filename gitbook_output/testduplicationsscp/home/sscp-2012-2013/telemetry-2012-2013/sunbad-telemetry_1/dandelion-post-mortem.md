# dandelion-post-mortem

## SSCP - Dandelion Post-Mortem

## Dandelion Post-Mortem

(From this Google Doc)

Dandelion Post-Mortem

A retrospective on the SSCP 2013 telemetry system

A note on usage

[A note on usage](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.74kdwqomd2z)

Document rev. 2 (zbrozek)

[Document rev. 2 (zbrozek)](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.faslfuyussz)

Introduction

[Introduction](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.mh9j5sxhv38x)

Purpose of telemetry

[Purpose of telemetry](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.qhzlblfhrgdx)

Prior implementations

[Prior implementations](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.krq9bdc61o48)

Perceived problems to solve with 2013 telemetry

[Perceived problems to solve with 2013 telemetry](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.xcj2k3uaitd5)

Accessibility

[Accessibility](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.rxzr90msur34)

Data loss

[Data loss](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.37jvndgzmkki)

Parsing content in the face of data structure change

[Parsing content in the face of data structure change](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.9b2dmfns0mql)

System components

[System components](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.unghm7cv9e70)

Catalog

[Catalog](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.m9r1pcurpvr)

Server hardware

[Server hardware](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.pd31pvmz9oil)

Backend

[Backend](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.9wazwt72ju8z)

Display

[Display](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.dgj7vl3ybnu)

Insights from the elders

[Insights from the elders](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.i6z2zzs6yzcq)

Hindsight 20/20

[Hindsight 20/20](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.snjf2ahynmhu)

Future paths

[Future paths](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.f0i549ue1l9n)

Document rev. 1 (fenichel)

[Document rev. 1 (fenichel)](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.1gen8xyxucqz)

Questions (all)

[Questions (all)](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.tzxp83faevq2)

## A note on usage

The purpose of this document is to help new team members understand the Luminos telemetry system as it was intended to be; as it was during the race; and as we think it should be modified going forward.  Facts about the system should be in the main document.  Opinions on the system should be clearly marked as such, by being placed either in the section Insights from the elders or in comments.  Questions about statements made in the document should be comments so we can have threaded conversations; more general questions can be asked in the section at the end of the doc.

[Insights from the elders](https://docs.google.com/document/d/17YiJ7zBBpbE2IhBhWvZEYqFE6yAwcSP8CxqRNpYFzNs/edit#heading=h.i6z2zzs6yzcq)

## Document rev. 2 (zbrozek)

### Introduction

#### Purpose of telemetry

At first, the telemetry system exists to allow for debugging of a vehicle. It provides real-time visibility into the state (and thus behavior) of a vehicle which aids in development. As the vehicle becomes a stable platform, the accumulation of performance data informs predictive models and permits the formation of race strategy.

#### Prior implementations

Stanford’s previous cars used various approaches to provide telemetry. Equinox (2005), Solstice (2007), and Apogee (2009) used RF-to-UART modems on both the car and chase to provide a data bridge. Solstice had a central computer with an RS232 port to an off-the shelf RF modem. All subsequent cars had in-vehicle packet networks (CAN) and transparent bridges to a chase vehicle. Equinox and Apogee used Zigbee modules. Xenith (2011) used a SPI-connected WiFi module. In all cases, compiled software ran on a client computer to receive data via UART and display it. No data was stored on-car.

[UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter)

[off-the shelf RF modem](http://ftp1.digi.com/support/documentation/productmanual_xtend_pkgr_rs232rs485rfmodem.pdf)

[Zigbee modules](http://www.digi.com/products/wireless-wired-embedded-solutions/zigbee-rf-modules/zigbee-mesh-module/xbee-zb-module)

[WiFi module](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en558369)

### Perceived problems to solve with 2013 telemetry

#### Accessibility

All old cars had a point-to-point bridge that allowed only one connection between a user and the car. Typically there was a single receiver, a single computer configured to use it, and a single human capable of using the setup. Frequently the hardware or the human were misplaced or out of commission, leading to a loss of visibility into the vehicle and a lot of angry engineers.

Dandelion solution: Choosing WiFi allowed connectivity between the vehicle and almost every mobile device in existence. Making the data accessible via a web interface means that no specialized software is required to use the system.

#### Data loss

Solstice through Xenith had no on-car data logging. As a result, whenever the car was on but no receiver setup was available, data was lost. It turned out that this was most of the time, especially during early vehicle debugging and forever after the end of a race.

Dandelion solution: On-car data logging. By making data source and sink inseparable, less data is lost.

#### Parsing content in the face of data structure change

Software developers add, remove, and change content and its format all the time. Historically, data structure change would (in the best case) simply not show up in the frontend, or (in the worst case) break the frontend completely.

Dandelion solution: Reflection mechanisms that would allow for in-situ reconstruction of available data and its formats. Superficially similar to protocol buffers.

[protocol buffers](http://en.wikipedia.org/wiki/Protocol_Buffers)

### System components

#### Catalog

In order to facilitate available data reflection and in-flight message decoding, we created the CAN Catalog. It provides a CAN message format that allows for in-flight decoding, and mandates a set of predefined messages that allow for full reflection of the remaining messages. On the embedded side, there are a set of libraries that handle the low-level interface between CAN peripherals as well as the generation of Catalog-compatible messages.

[CAN message format](../../../../../../stanford.edu/testduplicationsscp/home/sscp-2012-2013/telemetry-2012-2013/sunbad-telemetry_1/can-catalog-message-format/)

[predefined messages](../../../../../../stanford.edu/testduplicationsscp/home/sscp-2012-2013/telemetry-2012-2013/sunbad-telemetry_1/required-catalog-entries/)

#### Server hardware

Initially we started with a Gumstix-based computer on a custom carrier circuit board which provided an interface to CAN via an MCP2515. Due to severely bad WiFi performance, we switched to an i.MX6-based computer on a more nicely-designed board and with a nicer box. Both solutions had onboard WiFi, but the i.MX6 had onboard CAN and better performance on all axes. It lived on-car and would boot up automatically with the vehicle.

[Gumstix-based](https://store.gumstix.com/index.php/products/621/)

[MCP2515](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010406)

[i.MX6-based](http://boundarydevices.com/products/nitrogen6x-som/)

#### Backend

Catalog messages are received and logged to a SQL database by a Java EE backend. At boot-up, the server would query the vehicle and rebuild the catalog (by exercising the reflection mechanisms) if catalog checksums had changed.

#### Display

A Javascript-heavy frontend would query the SQL database and show available catalog entries (variables) on all boards present on the CAN bus. It provided means to drag-and-drop display types (live text, color-coded box, line graph, etc) around on to a virtual dashboard. The user could save and recall a dashboard layout.

### Insights from the elders

#### Hindsight 20/20

Fundamentally Dandelion and all of the infrastructure behind it is a technological solution to a discipline problem. Being sure to have a spare receiver, spare computer, and spare trained human is straightforward and technically simple.

Catalog is a reasonably well-designed system that has a mostly-debugged implementation with nice libraries and a good interface. Unfortunately, the further up the stack you go, the less well-behaved the system becomes. There are undiagnosed bugs in the reflection interaction between the embedded systems and the backend server. The frontend is extremely slow and buggy, was never used ‘in production’, and was not seriously developed after the end of an independent study course.

Server hardware was a challenge and a source of trouble. The Gumstix implementation was overwhelmingly too slow to communicate with a saturated CAN bus (\~50% CPU) and bridge  to WiFi (another \~50% CPU), leaving no CPU time for running the backend software (which itself was quite greedy). Switching to the i.MX6 module bought WiFi and CAN solutions that were much more efficient, as well as a much faster processor. Unfortunately it took a lot of development time to get to that point and was still not problem-free.

One major problem was the boot-time. It took 10-15 seconds for the computer to boot, missing the most critical CAN bus traffic. There was no workaround for this, and a lot of kernel, bootloader, and init script hacking was required to get it to be even this fast. Power consumption was also high, and the computer crashed when the weather was hot--in particular, when the CPU was maxed and the temperature was high.

In the end a much simpler system actually ended up being used for real-time telemetry and strategy. It used an embedded CAN-to-Ethernet bridge with a WiFi access point on the car to stream packets to a receiving access point in chase. Multiple clients could connect and packet decoding was done via Python script and UDP socket. Reflection and the solution to dynamic content went by the wayside, though the Catalog message format and the low-level libraries remained in use.

#### Future paths

Authoring a simple-to-use CAN configuration, message queuing, and interrupt-handling library was a win. It eradicated entire classes of problems (gross CAN misconfiguration and timing errors) and made it much easier for new members to get productive within an embedded networking context. That library should see continued development and use.

On-car storage with a computer that boots nearly instantly is attractive. The existing CAN-to-Ethernet bridge device (which also includes UART and SD card interfaces) is almost fast enough for this. Further effort to refine the SD card driver and include additional buffer RAM would make this feasible. A chase-side computer could provide frontend services

Switching away from WiFi would save a lot of power. Digi’s 900 MHz 9Xtend modules provide a lot of flexibility on the tradeoff between range and power, but have somewhat limited bandwidth and would require a proprietary receiver. Bluetooth LE would allow anybody to walk up and connect, offer extremely power, but could have inadequate range.

[9Xtend](http://www.digi.com/products/model?mid=2662)

[Bluetooth](http://www.st.com/web/catalog/sense_power/FM1968/CL1976/SC1898/PF258646)

Putting the bulk of the computing power in chase, possibly as a permanent (and duplicable!) installation would save weight and power in the solar car. A simple mechanism to query prior log data from onboard storage on the car would allow gap filling while caching on the chase computer would reduce bandwidth needs and latency.

.

## Document rev. 1 (fenichel)

Dandelion had a lot of moving parts.  At a high level it was intended to be an all-in-one telemetry system that both recorded data on the car and sent it back to the chase vehicle.

It might be best to look at it in terms of the problems we were trying to solve.

* Losing data due to network inconsistencies between chase and solar car.Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.Point people: Greg, Sasha, Sam D’Amico.Inconsistencies between the actual messages coming off the car (and formats) and the IDs and formats recorded in our decoding spec.Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.Point people: Rachel, Sasha.Having to build a custom interface to do any analysis of data.The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.Point people: Nathan Hall-Snyder, Paul Chen.
* Losing data due to network inconsistencies between chase and solar car.Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.Point people: Greg, Sasha, Sam D’Amico.
* Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.
* The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Point people: Greg, Sasha, Sam D’Amico.
* Inconsistencies between the actual messages coming off the car (and formats) and the IDs and formats recorded in our decoding spec.Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.Point people: Rachel, Sasha.
* Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* This was done every time the car booted.
* Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.
* All messages were timestamped upon receipt.
* There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.
* The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.
* Data type (bool, enum, long, etc)
* Variable name, as a string, transmitted in 8-byte chunks if necessary.
* Possible values for an enum, transmitted in the variable name.
* Frequency at which the variable would be sent.
* Other values visible and commented in code.
* Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.
* The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.
* Catalog entries included a pointer to data and an enum saying how to read that data.
* This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.
* It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).
* It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.
* There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* Point people: Rachel, Sasha.
* Having to build a custom interface to do any analysis of data.The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.Point people: Nathan Hall-Snyder, Paul Chen.
* The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* See each variable on the car and which board it came from.
* Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).
* Build groups of variables that should be viewed together.
* Save these groupings as named “dashboards” and reload them later.
* Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.
* It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.
* Point people: Nathan Hall-Snyder, Paul Chen.
* Losing data due to network inconsistencies between chase and solar car.Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.Point people: Greg, Sasha, Sam D’Amico.
* Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.
* The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Point people: Greg, Sasha, Sam D’Amico.
* Inconsistencies between the actual messages coming off the car (and formats) and the IDs and formats recorded in our decoding spec.Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.Point people: Rachel, Sasha.
* Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* This was done every time the car booted.
* Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.
* All messages were timestamped upon receipt.
* There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.
* The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.
* Data type (bool, enum, long, etc)
* Variable name, as a string, transmitted in 8-byte chunks if necessary.
* Possible values for an enum, transmitted in the variable name.
* Frequency at which the variable would be sent.
* Other values visible and commented in code.
* Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.
* The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.
* Catalog entries included a pointer to data and an enum saying how to read that data.
* This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.
* It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).
* It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.
* There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* Point people: Rachel, Sasha.
* Having to build a custom interface to do any analysis of data.The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.Point people: Nathan Hall-Snyder, Paul Chen.
* The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* See each variable on the car and which board it came from.
* Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).
* Build groups of variables that should be viewed together.
* Save these groupings as named “dashboards” and reload them later.
* Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.
* It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.
* Point people: Nathan Hall-Snyder, Paul Chen.

Losing data due to network inconsistencies between chase and solar car.

* Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.
* The startup time of the system meant that we lost important information in the first minute(s) of the car running.
* Point people: Greg, Sasha, Sam D’Amico.

Solution: Build telemetry around a full linux system on a single board.  Buy that board off the shelf, and add on a simple CAN-USB to communicate with the rest of the car.  Run a database on the car and write all messages to the database as they come in.

* Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.
* The startup time of the system meant that we lost important information in the first minute(s) of the car running.

Ended up building our own stripped-down version of the linux kernel.  This involved a lot of debugging.

The startup time of the system meant that we lost important information in the first minute(s) of the car running.

Point people: Greg, Sasha, Sam D’Amico.

Inconsistencies between the actual messages coming off the car (and formats) and the IDs and formats recorded in our decoding spec.

* Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.This was done every time the car booted.Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.All messages were timestamped upon receipt.There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* This was done every time the car booted.
* Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.
* All messages were timestamped upon receipt.
* There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.
* The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.
* Data type (bool, enum, long, etc)
* Variable name, as a string, transmitted in 8-byte chunks if necessary.
* Possible values for an enum, transmitted in the variable name.
* Frequency at which the variable would be sent.
* Other values visible and commented in code.
* Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.
* The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.
* Catalog entries included a pointer to data and an enum saying how to read that data.
* This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.
* It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).
* It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.
* There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.
* Point people: Rachel, Sasha.

Solution: create an algorithm by which the server discovers all other boards on the network, asks for all relevant variables on that board, and learns how to interpret each message from each board.

* This was done every time the car booted.
* Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.
* All messages were timestamped upon receipt.
* There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.
* The metadata about a message included:Data type (bool, enum, long, etc)Variable name, as a string, transmitted in 8-byte chunks if necessary.Possible values for an enum, transmitted in the variable name.Frequency at which the variable would be sent.Other values visible and commented in code.
* Data type (bool, enum, long, etc)
* Variable name, as a string, transmitted in 8-byte chunks if necessary.
* Possible values for an enum, transmitted in the variable name.
* Frequency at which the variable would be sent.
* Other values visible and commented in code.
* Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.
* The library of code that defined the catalog also defined ways to set and read values that were in the catalog.Catalog entries included a pointer to data and an enum saying how to read that data.
* Catalog entries included a pointer to data and an enum saying how to read that data.
* This was designed with data-creating boards (BMS, Xenith driver controls) in mind.It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.
* It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).
* It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.
* There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.

This was done every time the car booted.

Message values were parsed from 8 bytes to their correct data types as they were received, then put into the database in their final forms.

All messages were timestamped upon receipt.

There were thorny questions here about how to deal with changes in the protocol.  We settled with allow boards to stop sending messages but not allowing them to reuse IDs.  I believe this was informal; a similar problem and solution can also be seen in the definition of protobufs.

The metadata about a message included:

* Data type (bool, enum, long, etc)
* Variable name, as a string, transmitted in 8-byte chunks if necessary.
* Possible values for an enum, transmitted in the variable name.
* Frequency at which the variable would be sent.
* Other values visible and commented in code.

Data type (bool, enum, long, etc)

Variable name, as a string, transmitted in 8-byte chunks if necessary.

Possible values for an enum, transmitted in the variable name.

Frequency at which the variable would be sent.

Other values visible and commented in code.

Each board on the car had its own set of variables, defined and added to a “catalog” that was sent to the server when requested.

The library of code that defined the catalog also defined ways to set and read values that were in the catalog.

* Catalog entries included a pointer to data and an enum saying how to read that data.

Catalog entries included a pointer to data and an enum saying how to read that data.

This was designed with data-creating boards (BMS, Xenith driver controls) in mind.

* It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.
* It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).
* It also ignored boards that wanted to send messages on edges rather than at regular intervals.Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.This was a significant oversight.
* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.

It formalized sending messages, reducing hard coding of message IDs and manual bit/byte-bashing to add data to message bodies.

It ignored boards that might want to receive data (on Luminos, the button board was essentially a slave to driver controls RE: display).

It also ignored boards that wanted to send messages on edges rather than at regular intervals.

* Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.
* This was a significant oversight.

Luminos button board did not need to send the state of the buttons every 10 ms, but it did need to send a message as soon as the state of a button changed.

This was a significant oversight.

There were undiagnosed heisenbugs in the catalog/server communication code throughout the progress.  Finding those problems required us to debug the entire stack; we never had enough tools to make that easy, so bugs persisted to the race.  The primary manifestation was the catalog not rebuilding on a reboot.

Point people: Rachel, Sasha.

Having to build a custom interface to do any analysis of data.

* The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:See each variable on the car and which board it came from.Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).Build groups of variables that should be viewed together.Save these groupings as named “dashboards” and reload them later.Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* See each variable on the car and which board it came from.
* Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).
* Build groups of variables that should be viewed together.
* Save these groupings as named “dashboards” and reload them later.
* Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.
* It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.
* Point people: Nathan Hall-Snyder, Paul Chen.

The Dandelion frontend was designed to allow drag-and-drop data visualization.  You could:

* See each variable on the car and which board it came from.
* Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).
* Build groups of variables that should be viewed together.
* Save these groupings as named “dashboards” and reload them later.
* Graph variables next to each other (through drag-and-drop configuration).The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.
* The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.

See each variable on the car and which board it came from.

Display variables as enums, raw values, flags (square running from green to red; useful to quickly check if the car was behaving nominally).

Build groups of variables that should be viewed together.

Save these groupings as named “dashboards” and reload them later.

Graph variables next to each other (through drag-and-drop configuration).

* The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.

The on-car board sent a set of data points to the client; all of the work involved in graphing was done on the client side.

This was intended to make the team spend less engineering time on interfaces and allow people to build new views into the data when they wanted to see something new.

It decreased our dependency on a single engineer for building interfaces, at the cost of the new system being fragile->only a few engineers were able to fix it.

Point people: Nathan Hall-Snyder, Paul Chen.

.

## Questions (all)

Why did implementing a mini Linux kernel solve the network inconsistency issues? Why was it necessary to design a new one on a single board rather than use some existing infrastructure? Would this have to be done again, or could this kernel be reused so we could devote time to other parts of the system? Really trying to avoid debugging during the race here this time around.

The document has been updated to contain more information about this.  Sasha can answer further questions.

Is there a way I could look at your code from the last cycle (or part of it)  to get a better idea of setup and design?

Yes.  Look in the libraries section of the sunbad SVN repo for the embedded libraries; look at BMS code for canonical use of the CAN libraries.  Search for “dandelion” in the sunbad SVN to find the Eclipse project for the server code. (fenichel)
