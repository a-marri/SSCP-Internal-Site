# SSCP - Loading Conditions

# Loading Conditions

## Introduction

[](#h.1getn550rckr)

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

Loading conditions must be correctly applied to all system-critical mechanical components in order to ensure that no one component will fail unexpectedly. 

## Historical Loading Conditions

[](#h.9vyuuqr16a8i)

### Luminos

[](#h.t9ehoasbiy92)

Luminos Suspension Loading Conditions

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

g = vehicle mass * gravity * .7

Source: 

The 4G bump comes from a paper written by Rabih Al Zaher about the CSIRO motor. 

2g and 1g requirements come from ASC regulations. 

The .7 derating comes from best practices of the Minnesota Solar Vehicle Project and has its roots in a dynamics model of the car during a single wheel bump event.

Luminos Shock Loading Conditions

Unsprung Mass

 100g shock in Bump Direction

  Sprung Mass    

 25g shock in Bump Direction

g = 9.81m/s^2

Source: GMW3172 Specification

Luminos Cyclic Loading Conditions

Rotating Cycles

All unsprung mass, including bearings, shall be subject to and rated for at least 1.4x10^7 cycles, ~15000 miles, 1G

 Bump Cycles

 Not used on Luminos

Source: 1 cycle per wheel rotation, 15000 miles

Luminos Random Vibration Loading

While not tested, this specification was used for order of magnitude calculations for various components.

Vibration Spec, Components < 12kg

8G frequency sweep, XYZ, all components < 12 kg on car, 3 hrs/direction

 Vibration Spec, Components > 12 kg

 2G frequency sweep, XYZ, all components > 12 kg, 3 hrs/direction

Source: UN Battery Module Vibration resistance spec: http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN_Test_Manual_Lithium_Battery_Requirements.pdf 

[http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN_Test_Manual_Lithium_Battery_Requirements.pdf](http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/UN_Test_Manual_Lithium_Battery_Requirements.pdf)

Luminos Brake Pedal Loading Conditions

Force Applied to Pedal

500 lbf, applied normal to pedal.

Source: Historical Data

### Xenith

[](#h.1y7swumai7td)

Static Loading Conditions

 Bump    

 3g

  Brake    

 2g

 Corner

 1g

Fatigue Loading Conditions

Rotating Cycles, unsprung mass

4.8 x 10^6 cycles, 5000 miles, 1G

 Bump Cycles

 Not used on Xenith

Where g = total weight of car

### Apogee

[](#h.z70f5b66awix)

 Bump    

 3g

  Brake    

 2g

 Corner

 1g

Where g = vehicle weight / 3

### Solstice

[](#h.gvkzl744ndp1)

 Bump    

2g

  Brake    

 1g

 Corner

 1g

 

Where g = vehicle weight / 2

### Luminos Tire Patch Quick Reference

[](#h.bln9rbljaxzp)

### Maximum Loading On Suspension Loading Quick Reference

[](#h.mlrurq2565n0)

Force Calculated From Loads Text File From  Shark

 6800N along suspension linkage

 Bump   

 7141N

  Brake   

 3570N

 Corner

 1785N

[](https://drive.google.com/folderview?id=1jZGPkOlD-rATjadnDGN7BAwhSnH0-T-8)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1jZGPkOlD-rATjadnDGN7BAwhSnH0-T-8#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1jZGPkOlD-rATjadnDGN7BAwhSnH0-T-8#list" frameborder="0"></iframe>

