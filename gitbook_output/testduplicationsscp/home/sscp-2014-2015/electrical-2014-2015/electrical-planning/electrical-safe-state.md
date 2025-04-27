# SSCP - Electrical Safe State

# Electrical Safe State

### The driving regulatory force behind our architectural decisions is the concept of the electrical safe state introduced in the WSC2015 regulations. While it is always a good idea to fully read and understand the rules, the relevant sections to this state (excerpted from the rules on 9/24/14) are:

[](#h.x7m8yeoefeui)

        1.     All conductors emerging from the energy storage packs packs must be galvanically isolated from the energy storage devices inside those packs.

        2.     No conductors emerging from the energy storage packs or solar collector may carry high voltage, even though galvanically isolated.

        3.     All conductors emerging from the solar array must be isolated from all circuitry in the rest of the car by one or more mechanical switches or contactors.

        4.     If the solar control electronics (such as MPPTs) are physically close to the solar cells, teams may request permission. . . to deem these components part of the solar collector.

        5.     All wires, connectors, and electronics modules (such as MPPTs) which remain at high voltage when in safe state must be double insulated.

        6.     All mechanisms for placing the solar EV into safe state and maintaining safe state must employ mechanical switches or ‘normally open’ contactors designed to be fail-safe, if an electrical activation mechanism fails, the solar EV must automatically place itself into safe state immediately, and must remain in safe state indefinitely.

        7.     Contactors and switches must be rated to break DC fault currents.

        8.     Capacitors are not considered to be part of the energy storage system if their total energy storage capacity is less than 10.0Wh. Such capacitors must automatically discharge to less than 60V within 5 seconds of the solar EV being placed in safe state.

## Battery Pack Compliance: 

[](#h.hdu64klb4o3w)

    Assumptions: This explanation will be framed in terms of modifications that would have to be made to the Luminos battery pack and BMS 7.  

    To comply with these regulations, we will need to install two EV200 Contactors (see here for reasons the EV200s were selected), one on each end of the energy storage pack (bottom of bottom-most cell and top of top-most cell). 

[ here](/home/sscp-2014-2015/electrical-2014-2015/electrical-planning/contactor-selection)

    The existing battery back already has one of these contactors, on the high-side. The battery pack voltage sits on one side, and the positive leads of the three exterior power connectors are bussed together on the other side. This contactor is still compliant. 

    The second contactor could be inserted between the terminal on the bottom of the battery pack and the "PACK -" terminal on the BMS. It cannot be located between the BMS and the connectors because the BMS uses low-side current measurement on the negative terminals of those connectors, so they cannot be bussed together. 

BMS 7 only controls a single contactor (on the high-side) so a second drive circuit will need to be added. Since this contactor is only used on the ground side, it can be activated immediately upon initial boot (when the 24V bus comes up). I have yet to do detailed analysis of what happens to the existing precharge complete sensing circuitry, but I suspect that not having a ground reference for it could result in a false positive in the tens of milliseconds before the low-side contactor is turned on. To avoid this, I would advise integrating a power sequencing IC into the existing "precharge complete" detection circuitry. This IC would turn on the low-side contactor, then a fixed amount of time later (longer than the longest possible contactor turn-on time) would signal the existing circuitry that the ground path is established. This signal would then get AND-ed in with the other tests (voltage measurement, CPU input, etc). 

## Solar Colector Compliance:

[](#h.gsts93hcapoi)

    Assumptions: Framed in terms of modifications to the MPPT box as used on Luminos.

    To comply with these regulations, 2 EV200 contactors are to be used to disconnect both the positive and negative HV terminals on the output of the "MPPT Box." Inside of this box are all of the MPPTs whose negative HV terminals are all ganged together on one side of the low-side contactor, and positive HV terminals are ganged together on one side of the high-side contactor. 

    The MPPT box on Luminos is only capable of controlling a single contactor, and also has some extremely fail precharge sensing. An upgraded controller should be designed that upon being powered immediately powers the low-side contactor and then proceeds with precharge. An isolated 24V-5V converter and digital isolator can be used to enable HV- referenced, comparator-based sensing of absolute battery pack voltage voltage (to check for applied voltage) and (MPPT Cap Voltage / Battery Pack Voltage) ratio sensing to ensure proper precharge completion, similar to what was done for the main precharge on BMS 7.

    Using only 2 contactors on the HV side (instead of many contactors on the solar panel input side) requires we comply with rule number 4 as shown above. See this page for our current documentation of communication with the WSC officials regarding this point. 

[ this page](/home/sscp-2014-2015/electrical-2014-2015/electrical-planning/array-definition)

