# wiring

## SSCP - Wiring

## Wiring

Rough sketch of wiring in Sundae:

(old diagram)

[old diagram](https://docs.google.com/drawings/d/198CTBvlpVDiW_9TMsFFJhCCNxLxcaQPUJWUnu60GV3o/edit?usp=sharing)

#### Embedded Content

Embedded content: [Embedded Content](https://docs.google.com/drawings/d/1RlxQpM3Mshu7fn7yJw62MvfnwgAq6WG7331qhdKhhN8/preview?ac=true)

#### Embedded Content

Embedded content: [Embedded Content](wiring.md)

![](../../../../assets/sheets_32dp.png)

Below is a list of wiring and connectors for each point-to-point connection in the car:

Bottomshell

From Vehicle Computer

Each of these connections ends on the Vehicle Computer side in a Deutsch DT12 connector.  Required parts to build the DT connectors mating with the VC Deutsch Box are as follows:

#### Embedded Content

Embedded content: [Custom embed](wiring.md)

See the instructional video here on how to assemble the connector: https://www.youtube.com/watch?v=jE712DGw8CY

[https://www.youtube.com/watch?v=jE712DGw8CY](https://www.youtube.com/watch?v=jE712DGw8CY)

Additionally, the crimper box contains a sheet with information on how wires should be stripped prior to crimping.  Only use the Deutsch crimper to make these crimps.

Below is an image of the VC pinout.

![](../../../../assets/image_0af3ea667f.png)

Note these are not arranged in the same order as they will be arranged in the header of the box.  The below image shows the order of the connectors when VC is viewed from above:

![](../../../../assets/image_a7dd003005.png)

Array Wiring

Strings:

A0- > 1 > 2 > 3 > 4 > A0+

A1- > 6 > 5 > A1+

B0- > 8 > 7 > B0+

B1- > 15 > 16 > B1+

C0- > 10 > 9 > C0+

C1- > 17 > 18 > C1+

D0- > 11 > 19 > D0+

D1- > 14 > 13 > 12 > D1+

![](../../../../assets/image_a8c9e56cc1.jpg)

![](../../../../assets/image_5a35d87d63.jpg)

from Sam Lenius (also see attached document)

AMPSEAL PINOUT (CABLE SIDE, TOP LEFT IS PIN 1, BOTTOM RIGHT IS PIN 14)&#x20;

TOP ROW&#x20;

1. ARRAY CHANNEL 0 POSITIVE (6-120V, 0-6.5A)&#x20;
2. ARRAY CHANNEL 0 RETURN&#x20;
3. CAN HI&#x20;
4. CAN LO&#x20;
5. CAN VCC (9-36V)&#x20;

MIDDLE ROW&#x20;

6. ARRAY CHANNEL 1 POSITIVE (6-120V, 0-6.5A)&#x20;
7. ARRAY CHANNEL 1 RETURN&#x20;
8. CAN GND&#x20;
9. CAN GND&#x20;

BOTTOM ROW&#x20;

10. BATTERY POSITIVE (MAX ARRAY VOLTAGE - 160V)&#x20;
11. BATTERY NEGATIVE&#x20;
12. CAN VCC (9-36V)&#x20;
13. CAN HI&#x20;
14. CAN LO

The below photos show the \[MPPT]\[Channel] each string is connected to

![](../../../../assets/image_57d8aeefff.png)

![](../../../../assets/image_f37ddeb471.png)

Practice topshell 8/5 map from mppt channel to address (assumes lower address is channel 0):

A0 -- 0x602

A1 -- 0x603

B0 -- 0x60A

B1 -- 0x60B

C0 -- 0x604

C1 -- 0x605

D0 -- 0x606

D1 -- 0x607

Umbilical Cord Connector (571-HDP24-24-23PE / 571-HDP26-24-23SE)

![](../../../../assets/image_a2414f6711.jpg)

Center

A

Inner circle (MPPT outputs)

B: MPPT A +

C: MPPT B +&#x20;

D: MPPT C +&#x20;

E   MPPT D +&#x20;

F:  MPPT A -&#x20;

G: MPPT B -&#x20;

H   MPPT C -&#x20;

J:  MPPT D -&#x20;

Outer circle

K:  Blink Left +

L:  Blink Left -

M:  Blink Right +

N:  Blink Right -

O:  Brake +

P:  Brake -

Q:  LV+       (Phoenix cable RED)

R:  LV-        (Phoenix cable BLACK)

S:  CAN H    (Phoenix cable WHITE)

T:  CAN L     (Phoneix cable BLUE)

U:  EDisc in

V:  EDisc out

W: &#x20;

X: &#x20;

BMS Ethernet:

Pack-side Connector:

![](../../../../assets/image_285cd76765.jpg)

![](../../../../assets/image_0f4004ac0a.png)

TX+ Red

TX- Black

RX+ White

RX- Green

Car-side Connector:

![](../../../../assets/image_00a6f774c1.jpg)

Steering Wheel Connector

![](../../../../assets/image_0109defae0.jpg)

![](../../../../assets/image_d284b3974b.jpg)

Ethernet wire to RJ45 wire

Red - Striped Orange

White - Striped Green

Black - Solid Orange

Green - Solid Green

The wiring and connectors needed for each connection from VC are listed below, organized by their other endpoint:

1. VC-> BMS

&#x20;   a. Power

&#x20;       \- cable: 2-conductor Alphawire&#x20;

&#x20;       \- connector (BMS side): 3-position Deutsch HD10 (do not plug leftover pin, it's for Edisc)

&#x20;   b. Ethernet

&#x20;       \- cable: 2-pair/4-conductor Belden

&#x20;       \- connector (BMS side): Deutsch DT4

2. VC-> Steering Wheel

&#x20;   a. Ethernet + Edisc

&#x20;       \- cable: 2-pair/4-conductor Belden

&#x20;       \- connector (SW side): Lifeline p/n 410-200-019

3. VC-> Umbilical

&#x20;   a. MPPT CAN

&#x20;       \- cable: Phoenix 5-conductor

&#x20;       \- connector: Phoenix A-code 5-pin (built in to cable); ends at Umbilical connector

&#x20;   b. Edisc

&#x20;       \- cable: a single conductor, can be red array wiring

&#x20;       \- connector: Umbilical

&#x20;   c. Power for Taillights, Rear Turn Signals&#x20;

&#x20;       \- cable: 2-conductor Alphawire x 3 (Taillights, L turn, R turn)

&#x20;       \- connector: Umbilical

4. VC-> Pedals

&#x20;   a. Power + Signal

&#x20;       \- cable: 3-conductor Alphawire x 2 (Throttle, Brake)

&#x20;       \- connector: Ampseal connector

5. VC-> Headlights, Front Turn Signals, and Side Lights

&#x20;   a. Power

6. VC-> Rear View System

&#x20;   a. Power

7. VC-> Handheld Radio Microphone

&#x20;   a. Switch

8. VC-> GPS Antenna

&#x20;   a. Feed

9. VC-> Wifi Antenna

&#x20;   a. Ethernet

10. VC-> Tritiums

&#x20;   a. Tritium CAN

From BMS

Harnesses that include BMS as one endpoint but do not go to VC are the wiring to power the motors (other endpoint is the Tritiums), wiring to the MPPTs (other endpoint is the Umbilical), and wiring to the&#x20;

1. BMS-> Tritiums

&#x20;   a. HV Power (L+R)

2. BMS->HV Splitter Box

&#x20;   a. HV Power

HVA-280 Assembly manual

[HVA-280 Assembly manual](http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc\&DocId=Specification+Or+Standard%7F408-10299%7FB%7Fpdf%7FEnglish%7FENG_SS_408-10299_B.pdf%7F1587826-2)

From HV Splitter Box

1. HV Splitter Box-> Umbilical

&#x20;   a. HV Power (for MPPTs)

Tritiums->Motors

1. Motor Resolver Cable

&#x20;   a. Signal

2. 3-Phase Power

&#x20;   a. HV Power

Topshell

From Umbilical

1. Umbilical-> MPPTs

&#x20;   a. MPPT CAN

&#x20;   b. HV Power

&#x20;  &#x20;

2. Umbilical-> Edisc button

&#x20;   a. Edisc (x2)

3. Umbilical-> Taillights, Rear Turn Signals

From Array

1. Array-> MPPTs

&#x20;   cable: Alphawire red/black hook-up wire&#x20;

&#x20;   connector: TE ELCON mini

&#x20;   Assembly instructions: see "ENG\_SS\_114-19110\_C.pdf" attached at the bottom of the page.

&#x20;

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=150gbJjDgxJ22sl1ATQiqVnxpJUGqPm1X#list)
