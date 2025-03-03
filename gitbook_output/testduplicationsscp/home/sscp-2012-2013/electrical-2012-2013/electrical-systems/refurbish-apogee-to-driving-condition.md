# SSCP - Refurbish Apogee to driving condition

# Refurbish Apogee to driving condition

Purpose

Apogee is a good car that we should use to test against our newer cars as a performance benchmark. If we're not better than our old cars, we shouldn't take our new cars to races. It's a waste of time. Further, getting an old vehicle up and running provides a great test bed for people to play with new electronics or to understand how solar cars work.

Requirements

Apogee is currently lacking an electrical system. The battery pack is toast and needs to be replaced. The battery monitoring system (BMS) has been harvested for other purposes. Driver controls is in unknown state. The motor controller is missing. Greg knows more about Apogee's state. All of these missing systems need to be replaced and the vehicle needs to be tested. The cost to refurbish Apogee should be kept low.

Proposed solutions

Battery pack

Protomold can make more plastic end plates for 18650s for relatively low cost. We should get 72 plus a few spares made and use glue in some low-cost but reasonably high-quality 18650s to assemble a new battery pack. It's probably possible to re-use the fiberglass box from the Xenith practice pack. Finding a contactor could be a problem. Contact TE (formerly Tyco Electronics) to get another set sponsored. Model EV200HAANA is ideal and EV200AAANA is good enough.

[ reasonably high-quality 18650s](http://www.batteryspace.com/Li-ion-18650-Cylindrical-Rechargeable-Cell-3.7V-2600mAh-9.62Wh---LG.aspx)

[ EV200HAANA](http://relays.te.com/datasheets/ev200.pdf)

BMS

We have several spare BMS boards. One of them should go in to the Apogee battery pack. Take care to thoroughly examine all of the connections to the new BMS in the Xenith pack to make sure that nothing is overlooked.

Driver controls

This is trickier. Xenith and Apogee have different driver controls schemes. It may be worthwhile to use the old Apogee driver controls board. Ben Stabler built a version with an STM32 which can successfully drive the vehicle. The Xenith driver controls would present some difficulties as it has encoder inputs, not magnetic angle inputs.

Motor and motor controller

We have the Tritium Wavesculptor20 which was originally designed in to Apogee. It should be dug out and reinstalled with the NGM SCM-150 motor. The motor's datasheet is attached.

[](https://drive.google.com/folderview?id=1LgI21JL7AHZueLrZp66X7URDFwOseKIf)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1LgI21JL7AHZueLrZp66X7URDFwOseKIf#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1LgI21JL7AHZueLrZp66X7URDFwOseKIf#list" frameborder="0"></iframe>

