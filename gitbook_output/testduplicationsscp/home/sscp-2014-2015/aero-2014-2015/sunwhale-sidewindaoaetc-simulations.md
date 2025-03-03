# SSCP - Sunwhale Sidewind/AoA/etc Simulations

# Sunwhale Sidewind/AoA/etc Simulations

These are cars referred to on the Sunwhale Iterations page that have also been run with additional simulations (sidewind, AoA, etc.)

[ Sunwhale Iterations](/stanford.edu/testduplicationsscp/home/sscp-2014-2015/aero-2014-2015/sunwhale-iterations)

Sunwhale-014

Location: sftp://cars/sunwhale/aero/sunwhale-014

Results

Fluent

Drag: 33.594041 

Sideforce: 3.6714592 

Lift: -41.858841

SU2

Drag: 34.483 N

Lift: -38.2765 N 

Sidewind Runs

This model was run in SU2 as an external flow-style problem (changing the walls and outlet to type MARKER_FAR, and adding a y velocity to the inlet boundary condition.

"sunwhale-014-wind0"

vy = 0 m/s (control)

Drag: 34.469 N

Sideforce: 4.119 N

Lift: -38.53 N

"sunwhale-014-wind1"

vy = -10 m/s (starboard to port)

Drag: 171 N

Sideforce: -443.66 N

Lift: -11.25 N

"sunwhale-014-wind2"

vy = +10 m/s (port to starboard)

Drag: 179.497 N

Sideforce: 453.9657 N

Lift: 161.827 N

"sunwhale-014-wind3"

vy = +5 m/s (port to starboard)

Drag: 63.85 N

Sideforce: 171 N

Lift:  14.78 N

"sunwhale-014-wind4"

vy = +3 m/s (port to starboard)

Drag: 44.28 N

Sideforce: 91.87 N

Lift:  -11.813 N

"sunwhale-014-wind5"

vy = -3 m/s (port to starboard)

Drag: 42.72 N

Sideforce: -83.38

Lift:  -49.65

"sunwhale-014-wind6"

vy = -5 m/s (port to starboard)

Drag: 60.88 N

Sideforce: -161.6 N

Lift:  -50.41

Sunwhale-016

Location: sftp://cars/sunwhale/aero/Sunwhale-016

Using Sunwhale-015 CAD, but adding a dimple under the car. The CAD is robust enough to allow some change in dimple shape without needing to fix up the entire model. I also chose fully symmetric airfoils for the fairings to hopefully improve our performance in crosswinds. I blended the fairing into the main body on the sides of the car by using the "side of car" curve as part of the fairing cutout trimming tool. The "side of car" curve is used in defining the main body surface and is created by projecting the 3/4 main foil onto the planform view of the car.

Drag: 41.1 N

Lift: -104.6 N

Sideforce: -5.8 N

"sunwhale-016-wind1"

vy = +3 m/s

Drag: 38.71 N

Sideforce: 103.78 N

Lift: -109.76 N

"sunwhale-016-wind2"

vy = -3 m/s

Drag: 40.03 N

Sideforce: -102.2 N

Lift: -83.41 N

"sunwhale-016-wind3"

vy = +5 m/s

Drag: 35.25 N

Sideforce: 177.41 N

Lift: -111.85 N

"sunwhale-016-wind4"

vy = -5 m/s

Drag: 37.024 N

Sideforce: -186.125 N

Lift: -57.85 N

Sunwhale-019

Location: sftp://cars/sunwhale/aero/Sunwhale-019

Using Sunwhale-014 CAD, with improved bubble

Drag: 33.183 N

Sideforce: 3.05 N

Lift: -42.02 N

SideWinds

Sunwhale-019-wind1

vy = 5 m/s

Force in the X direction (Drag) 35.0319 N

Force in the Y direction (SideForce) 8.6515 N

Force in the Z direction (Lift) -40.1904 N

Sunwhale-019-wind2

vy = -5 m/s

Force in the X direction (Drag) 35.1109 N

Force in the Y direction (SideForce) -2.0038 N

Force in the Z direction (Lift) -41.7918 N

Sunwhale-019-wind3

vy = 10 m/s

Force in the X direction (Drag) 39.4669 N

Force in the Y direction (SideForce) 9.7833 N

Force in the Z direction (Lift) -45.6641 N

Sunwhale-019-wind4

vy = -10 m/s

Force in the X direction (Drag) 39.7213 N

Force in the Y direction (SideForce) -2.4203 N

Force in the Z direction (Lift) -48.0504 N

Angle of Attack

Sunwhale-019-aoa1

vz = 1 m/s

angle = 2.33 deg

Force in the X direction (Drag) 30.0014 N

Force in the Y direction (SideForce) 2.9320 N

Force in the Z direction (Lift) -30.5182 N

Sunwhale-019-aoa2

angle = 4.65 deg

vz = 2 m/s

Force in the X direction (Drag) 26.4614 N

Force in the Y direction (SideForce) 2.6544 N

Force in the Z direction (Lift) -22.1681 N

Sunwhale-019-aoa3

vz = 3 m/s

angle = 6.96 deg

[](https://drive.google.com/folderview?id=1Wj4uUpHs_brNkKciz1KjP1RGoSuWARTM)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1Wj4uUpHs_brNkKciz1KjP1RGoSuWARTM#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1Wj4uUpHs_brNkKciz1KjP1RGoSuWARTM#list" frameborder="0"></iframe>

