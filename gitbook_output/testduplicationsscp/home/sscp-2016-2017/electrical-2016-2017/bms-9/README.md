# SSCP - BMS 9

# BMS 9

Introduction

If we were to liken the current electrical system to the human body, the Vehicle Computer would be the brain and the BMS, or Battery Management System, would be the heart. The main responsibility of the BMS is to monitor and control the energy flowing from the battery cells out to the rest of the car and vice versa. This is to ensure that the battery cells stay within acceptable current and voltage limits. If we were using alkaline AAA batteries or lead acid car batteries, we wouldn't have to worry about this. However, we are using lithium ion batteries (the best option under WSC rules) that require monitoring and protection in order to keep them from permanently damaging themselves, or at the very worst, catching fire. The data gathered from monitoring (voltage, current, and temperature) is also used to calculate the battery's current state of charge to help inform race strategy.

Design Philosophy

The following is a snippet written by BMS 7 designer Max Praglin which summarizes my design approach more effectively than I could have ever done:

Each designer has different reasons for putting endless hours into SSCP. My reasons are: learning, and being involved in a cool project. Past generations of designers have re-invented the wheel for the sake of "innovation," or because "it is the only way to learn." I don't think it's necessary to start from scratch to learn something.

Thus, the BMS I set out to design is not intended to be novel, but reliable and maintainable. Designing a circuit from scratch may mean more experience in selecting parts and feel like more understanding is gained; however, this does not mean that less is learned through iterating on a design. Iteration forces consideration of prior design decisions and requires a more in-depth understanding of each circuit block, if improvement is to be made. I could have thrown out all work done on Solar Car BMS's before, but I chose to rethink Greg's BMS 6, with a focus on modernizing parts selections, eliminating unnecessary components (especially those that are failure-prone, like connectors, power supplies, or capacitors), and characterizing / testing the final product.

The bottom line: if you're the person tasked with "building" a BMS for the next car, and you're starting from scratch without a clear reason for changing the architecture of the BMS, then I haven't met my design goals. In the interest of progressing forward with a reliable and functional design (and giving more time for other projects on the car), this BMS is intended to only require changes that will help adapt to the architecture of the next car. I've made every attempt to keep parts modern and simplify the design. Consider this before throwing out the countless hours I've put into a BMS - your time is finite. Each hour you spend reinventing what I've done here (that does not clearly improve over the current design) is an hour that won't go to another section of the car.

Happy Solar Car Racing!

--Max Praglin, Class of 2014-ish

Design Requirements

The following are all the rules from the WSC 2017 regulations that pertain to BMS 9:

2.5.12 Capacitors are not considered to be part of the energy storage system if their total energy storage capacity is less than 10.0 Wh. Such capacitors must be automatically discharged to less than 60 V within five seconds of the solar car being placed in safe state (see Regulation 2.29).

2.28.7 The resistance between any exposed conductive part and each terminal of the energy storage system must exceed 100 V ohms, where V is the nominal voltage of the energy storage system.

2.28.10 Each energy storage pack must be protected by a fuse or circuit-breaker rated to interrupt the short-circuit fault current of the pack. This fuse or circuit-breaker must be mounted in or on the energy storage pack.

2.29.1 The solar car must have a ‘safe state’ which minimizes the risk of electrical fire and electric shock to occupants, team members, emergency response personnel, and

bystanders. When in the safe state:

* there must not be a high voltage (> 60V DC or 30Vrms AC) across any pair of conductors emerging from energy storage packs or from the solar collector
* every conductor emerging from each energy storage pack must be galvanically isolated from every energy storage cell
* low voltage must not be present across any pair of conductors emerging from energy storage packs or the solar collector unless the pair of conductors is incapable of delivering more than 50 mA of current.

there must not be a high voltage (> 60V DC or 30Vrms AC) across any pair of conductors emerging from energy storage packs or from the solar collector

every conductor emerging from each energy storage pack must be galvanically isolated from every energy storage cell

low voltage must not be present across any pair of conductors emerging from energy storage packs or the solar collector unless the pair of conductors is incapable of delivering more than 50 mA of current.

2.29.2 Any conductor that is more than 200 mm from the nearest PV cell or from an associated electronics module such as a maximum power point tracker is considered to be outside of the solar collector.

2.29.3 All mechanisms for placing the solar car into safe state and maintaining safe state must employ mechanical switches or ‘normally open’ contactors designed to be fail-safe; if an electrical activation mechanism fails, the solar car must automatically and immediately place itself into safe state, and must remain in safe state indefinitely.

2.29.4 The driver must be able to place the solar car into safe state while seated in the normal driving position and without releasing the safety-belt.

2.29.5 For emergency use, an activation device that immediately places the solar car into safe state must be provided on the exterior of the car. The activation device must be placed within a yellow disc with a minimum diameter of 180 mm. Also in the yellow disk must be a blue equilateral triangle (minimum side length 150 mm) that contains a red flash, with the legend Emergency Electrical Isolation. In addition, there must be a clear instruction on how to operate the device (e.g., PULL or PRESS). The yellow isolation disc containing the activation mechanism must be clearly visible to an emergency services first responder approaching the driver, and must be within 100 mm of the base of that part of the windscreen used to meet the forward vision requirement, and adjacent to the driver egress opening.

The only significant change from the WSC 2015 regulations is the third bullet point of rule 2.29.1, which requires the addition of a 50mA fuse to the EDISC line that emerges from the battery pack.

BMS 8 Post-Analysis

BMS 8.2.2 Post-Analysis

[BMS 8.2.2 Post-Analysis](https://docs.google.com/a/stanford.edu/document/d/1DXTfR67JL6nFit6exlADnqQYrLJ4T5gCZlVjvvhkOCQ/edit?usp=sharing)

Changelog

BMS 9.0.0 Changelog

[BMS 9.0.0 Changelog](https://docs.google.com/a/stanford.edu/document/d/1IPmUXOrr5pJl52jpCSYGDnbbPKpCnWRdim4mYnZ0mMM/edit?usp=sharing)

Design Reviews

Empty

Final Architectural Decisions

Empty

Bring Up & Testing

Empty

Additional Materials

Electrical System Constraints

[Electrical System Constraints](https://docs.google.com/a/stanford.edu/document/d/1C5cRYkEMdZvqIsB5LGSC9nN3_aMiR6sSnc9K6V9FECw/edit?usp=sharing)

