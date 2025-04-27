# loading-conditions

## SSCP - Loading Conditions

## Loading Conditions

### Introduction

Loading conditions are a set of parameters that our team uses to simulate the loads on the car during a race. Driving loads are broken into three categories:

* Bump, a force that causes the wheel to move upwards, usually due to a bump on the road
* Brake - a force created by the vehicle braking
* Corner, a force created by the wheel cornering

Bump, a force that causes the wheel to move upwards, usually due to a bump on the road

Brake - a force created by the vehicle braking

Corner, a force created by the wheel cornering

Fatigue loads are broken into two categories. The number of cycles for these two events are orders of magnitude greater than all other cyclic loads:

* Rotating cycles - loads which occur on each rotation of a wheel
* Bump cycles - loads which occur on each bump event. Bump events are assumed to happen no more often than the resonant frequency of the suspension.

Rotating cycles - loads which occur on each rotation of a wheel

Bump cycles - loads which occur on each bump event. Bump events are assumed to happen no more often than the resonant frequency of the suspension.

Loading conditions must be correctly applied to all system-critical mechanical components in order to ensure that no one component will fail unexpectedly.&#x20;

### Historical Loading Conditions

#### Luminos

Luminos Suspension Loading Conditions

#### Embedded Content

Embedded content: [Custom embed](loading-conditions.md)

g = vehicle mass \* gravity \* .7

Source:&#x20;

The 4G bump comes from a paper written by Rabih Al Zaher about the CSIRO motor.&#x20;

2g and 1g requirements come from ASC regulations.&#x20;

The .7 derating comes from best practices of the Minnesota Solar Vehicle Project and has its roots in a dynamics model of the car during a single wheel bump event.

Luminos Shock Loading Conditions

Unsprung Mass

&#x20;100g shock in Bump Direction

&#x20; Sprung Mass   &#x20;

&#x20;25g shock in Bump Direction

g = 9.81m/s^2

Source: GMW3172 Specification

Luminos Cyclic Loading Conditions

Rotating Cycles

All unsprung mass, including bearings, shall be subject to and rated for at least 1.4x10^7 cycles, \~15000 miles, 1G

&#x20;Bump Cycles

&#x20;Not used on Luminos

Source: 1 cycle per wheel rotation, 15000 miles

Luminos Random Vibration Loading

While not tested, this specification was used for order of magnitude calculations for various components.

Vibration Spec, Components < 12kg

8G frequency sweep, XYZ, all components < 12 kg on car, 3 hrs/direction

&#x20;Vibration Spec, Components > 12 kg

&#x20;2G frequency sweep, XYZ, all components > 12 kg, 3 hrs/direction

Source: UN Battery Module Vibration resistance spec: http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN\_Test\_Manual\_Lithium\_Battery\_Requirements.pdf&#x20;

[http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN\_Test\_Manual\_Lithium\_Battery\_Requirements.pdf](http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN_Test_Manual_Lithium_Battery_Requirements.pdf)

Luminos Brake Pedal Loading Conditions

Force Applied to Pedal

500 lbf, applied normal to pedal.

Source: Historical Data

#### Xenith

Static Loading Conditions

&#x20;Bump   &#x20;

&#x20;3g

&#x20; Brake   &#x20;

&#x20;2g

&#x20;Corner

&#x20;1g

Fatigue Loading Conditions

Rotating Cycles, unsprung mass

4.8 x 10^6 cycles, 5000 miles, 1G

&#x20;Bump Cycles

&#x20;Not used on Xenith

Where g = total weight of car

#### Apogee

&#x20;Bump   &#x20;

&#x20;3g

&#x20; Brake   &#x20;

&#x20;2g

&#x20;Corner

&#x20;1g

Where g = vehicle weight / 3

#### Solstice

&#x20;Bump   &#x20;

2g

&#x20; Brake   &#x20;

&#x20;1g

&#x20;Corner

&#x20;1g

&#x20;

Where g = vehicle weight / 2

#### Luminos Tire Patch Quick Reference

#### Maximum Loading On Suspension Loading Quick Reference

Force Calculated From Loads Text File From  Shark

&#x20;6800N along suspension linkage

&#x20;Bump  &#x20;

&#x20;7141N

&#x20; Brake  &#x20;

&#x20;3570N

&#x20;Corner

&#x20;1785N

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1jZGPkOlD-rATjadnDGN7BAwhSnH0-T-8#list)
