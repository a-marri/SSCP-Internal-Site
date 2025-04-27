# cad-map

## SSCP - CAD Map

## CAD Map

Everything is stored in the CAD folder on the google drive. YOU MUST USE GOOGLE FILE STREAM TO ACCESS THE CAD FOLDER OR THE REFERENCES WILL NOT WORK PROPERLY -

The CAD got a little messed... Rule of thumb for finding things, you should open the assembly first and then find individual components from that assembly. Several things are defined within the assemblies so that everything updates correctly.&#x20;

The main components of the front suspension have a reference sketch at the begining of the feature tree. This defines the geometry from the original geometry part. For example, the upper control arm (UCA) is gemeotryically just a planar triaingle. Therefore the reference sketch in SR-sus-UCA defines that triangle based off of SR-sus-geo front. This is referenced in the SR-sus-UCA.sldasm assembly. Then the rest of the 3D part is derived off of that original sketch. This makes it easy to change the original gemeotry and have the global assemblies and components update correctly.

Configuarations are used for assemblies to show limits of travel - i.e. the UCA assembly has a bump configuaration that has the UCA in the in full bump. The defualt configurations should have all of the configurations shown at once. NOTE: the configuarations work by suppressing extraneous bodies. This is much easier than trying to define mates that are suspressed in some configurations but not others. &#x20;

Most all the assemblies have the SR-sus-geo front sketch inside them. In the global assemblies, the origins of each individual SR-sus-geo-front is mated together to keep mating consistent and clean. The downsides is you have be good about checking interference.

Main Assemblies - (most all of them define their sub componenets)

SR-sus-full front

* SR-sus-geo front (3D sketches for all of front suspension geometry)
* SR - str- bell crank assem (has entire steering system)

&#x20;   \- SR-str-bell crank hp 3 (has the bell crank hardpoint with the bearing stack)

&#x20;   \- SR-str-drag link ( pushrod between steering bell cranks)

&#x20;   \- SR-str-rack link (push rod from steering rack to bell cranks)

* SR - sus - UCA (Both sides of the UCA in all bump, ride height, and jounce)
* SR - sus - LCA (both sides of the lower control arm in all states)
* SR - sus - Upright wheel (has the upright, steering arm, and hub)

&#x20;   \- SR-sus-Wheel Tire - (has rim, tire, and wheel shrouds, and brake caliper mount)

* SR - sus - tie rod configs (tie rods on all states)
* SR - sus - shock configs (shocks in all states)
* SR - sus - sway bar configs (sway bar in all states)

&#x20;   -SR-sus-sway bar - single sway bar assembly

SR-sus-full rear

&#x20;\- SR-sus-trailing arm v9 (final trailing arm version)?

&#x20;\- SR - sus - rear shock configs

Brake Assembly - Ask drake for more information

SR-brakes-brake pedal fuck my life assembly

Steering Wheel&#x20;
