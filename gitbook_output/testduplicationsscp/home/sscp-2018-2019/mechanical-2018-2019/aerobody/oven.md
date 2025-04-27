# oven

## SSCP - Oven

## Oven

#### Embedded Content

Embedded content: [Embedded Content](oven.md)

![](../../../../../assets/docs_32dp.png)

\[COPY]

How to Build a Composites Oven

Experimental Findings of the 2019 SSCP Mechanical Team

Overview:

This document serves as a guide to oven-building for future membership of the Stanford Solar Car Project. It is based on the long process of trial and error undertaken by the 2019 mechanical team, which itself referenced the precedents of previous cycles, and thus it presents at least some semblance of optimization. It should therefore be perfectly appropriate to replicate the following procedure exactly. However, there are several improvements which were realized in the building process but never fully applied. These will be included as interjections and suggestions for further optimization but hold no guarantee of working correctly.

Warnings:

Do not…

* recycle hot air into the intakes of the heaters (only pull in outside air)\*attempt to modify the heaters’ built-in thermostats in order to control oven temperature (disabling them is ok)
* recycle hot air into the intakes of the heaters (only pull in outside air)\*
* attempt to modify the heaters’ built-in thermostats in order to control oven temperature (disabling them is ok)

1. recycle hot air into the intakes of the heaters (only pull in outside air)\*
2. attempt to modify the heaters’ built-in thermostats in order to control oven temperature (disabling them is ok)

recycle hot air into the intakes of the heaters (only pull in outside air)\*

attempt to modify the heaters’ built-in thermostats in order to control oven temperature (disabling them is ok)

\*If you do this, the plastic compression chamber will melt and lose air pressure. This will prevent the fuel from atomizing and it will instead drip down and collect in the fan housing. In our case, this led to a small fire precariously close to the fuel tank.

Timeline:

Preparation should begin at least three weeks in advance.

(approximate/divided by individual sessions/not including experimentation time)

#### Embedded Content

Embedded content: [Custom embed](oven.md)

Materials Used:

(not an exhaustive list)

#### Embedded Content

Embedded content: [Custom embed](oven.md)

Structure:

A basic SketchUp model of the oven’s structure can be found in the file ‘sscp\_oven.skp’. Dimensions may vary based on mold size, but ours was approximately 5.5 x 5.5 x 17.5ft. All following analysis will be based on those measurements.      &#x20;

The 2x4-ribbed plywood design was structurally sufficient and efficient to build. Each of the four long faces should be assembled flat on the ground with the 2x4s centered under the vertical seams in the plywood. It is extremely important, however, that their spacing is kept consistent in order to match the joints between panels. 1.5” screws placed every \~14in along both sides of the seams will secure the segments together. Disassembly will be easier if no screws are within 2in of the outer edge (so they don’t interfere with the walls). The 2x4s on the walls must then be trimmed to interface with the roof and floor.

The walls can each be raised into place and secured with corner brackets on both sides of each 2x4 joint. The plywood for the doors can be clamped in place temporarily to provide extra support. The roof should then be lifted into place and secured in the same manner.

The plywood for the doors can be fastened together using short segments of 2x4. More of these segments should be added around the rim at the locations of the latches.

Insulation:

We used 1in thick high-temperature mineral wool insulation on all the inside surfaces of the box as well as around the holes for the air intakes (to protect the wood from the metal). This material can easily be cut with scissors, razor blades, or box knives. On the walls, ceiling, and doors, this was secured using screws and fender washers. A sheet of insulation was also temporarily laid over the caster tracks near the air inlet in order to prevent the angle iron from overheating and charring the wood.

Together, the insulation and plywood should provide a thermal resistance of about R = 5 ft&#x32;_&#x68;&#x72;_&#xBA;FBtu. This means that maintaining a temperature of 275ºF should require a power input of approximately 20,000 Btuhr. After considering the effects of heat leaks, this is pretty consistent with our findings, as temperature can be maintained relatively easily using one 80,000 Btuhrheater intermittently. However, this should be avoided as it may overheat the vents or create hotspots on the mold.

Tracks:

Steel angle irons laid angle-up serve as tracks that interface with the grooved casters. They can be secured to the floor using standard wood screws driven directly on either side but should be placed on top of a \~4in wide secondary layer of plywood in order to clear the insulation and better support the weight of the mold. Consistent spacing can be achieved by cutting scraps of plywood to the length of the desired track width and using them as templates.

Two extra track segments should be kept available in order to facilitate the loading of the molds. These will slide on top of the secured track and protrude from the door of the box, each resting on a block with a height equal to the level of the track bed (one 2x4 and two plywood layers in our case).

Heaters:

Though only one heater is required to maintain temperature (275ºF or 135ºC) at any given time, it is important to incorporate at least three in order to achieve an even temperature gradient and avoid overheating any of the inlet vents or creating hotspots on the molds.

Before using the heaters, their thermocouples should be removed, thus disabling the emergency high temperature cutoff. This can be achieved by unplugging both wires connected to the thermocouple and reattaching one directly to the switch (need more info)

The heaters can be integrated into the ductwork using the reducers. To do this, remove the top shell of the heater and slide the combustion chamber out of its housing. Place the large end of the reducer over this chamber and return it to its mounted position. Replacing and tightening the top of the heater will now secure the reducer in place. Using this setup has the added benefit of creating a nozzle at the outlet of the heater and thus increasing the exit velocity of the hot air.

Ducting:

We used 6in aluminum ducting for all of our connections. These ran from each heater nozzle to their respective vent locations on the walls of the oven and were secured using hose clamps at each end. We found it was necessary to ensure that these pipes were never shorter than \~4ft, even for those that connected near the base of the oven. This is to allow the air to cool slightly before entering the chamber and to further prevent hotspots or vent overheating.

The vents were placed on a secondary layer of insulation and secured to the walls using wood screws. This better separated them from the wood to prevent charring. We pointed these vents \~30º downwards in order to both encourage circulation and fight the natural tendency for the heat gradient to bias towards the top.

&#x20;

Over the course of our experimentation, we tried several vent orientations and locations before arriving at this solution:

Because the airflow rate is high and thus the drop between inlet and outlet temperature is relatively low, the exhaust hole can be considered with some (reverse) equivalency to a fourth vent. This allowed for symmetry and a relatively even gradient (though the temperature was often a couple degrees higher on the side of the wall with two vents). However, we found that maintaining this uniformity for extended periods of time required running “-ing” by itself, only pulsing the other two heaters intermittently. So, it is quite possible that one of the following formats would prove more efficient:

Charring:

Though, for the most part, the oven was well-insulated, there were several locations where charring occurred. To prevent this, it is important to minimize gaps in the insulation (especially on the ceiling) and to avoid direct contact between metal and wood.&#x20;

&#x20; &#x20;

Loading/Unloading:

A pallet jack is extremely important to the loading operation. Our method is laid out in the following procedure:

* Open both doors.Roll the mold until its front wheels are butted up against the door sill and approximately aligned with the tracks (if any of the casters are fixed direction, they should be in front).Use the pallet jack (from the side) to lift the front wheels off the ground. The mold should be resting only on the rear wheels and pallet jack and the front wheels should be slightly above the height of the tracks.Lay the extra angle irons on top of the secured ones and let them protrude from the oven until they are comfortably under the front wheels. Use the extra blocks to support them.Slowly lower the front wheels onto the the extended tracks. The jack can roll side to side to allow for perfect alignment.The mold can now be rolled forward until it is off the track extensions, and these extra angle irons can be removed. Throughout the process of rolling the mold, the vacuum tubes should be pushed through their respective holes in the oven wall. It can be rolled until the back casters hit the sill, striving for perfect alignment with the tracks.The jack can now be used (from the rear) to lift the rear casters above the height of the rails and roll the mold the rest of the way inside. It is extra important that the wheels are pre-aligned as the jack can no longer provide side to side movement.Once the mold is in its desired position, the wheels should be locked.
* Open both doors.
* Roll the mold until its front wheels are butted up against the door sill and approximately aligned with the tracks (if any of the casters are fixed direction, they should be in front).
* Use the pallet jack (from the side) to lift the front wheels off the ground. The mold should be resting only on the rear wheels and pallet jack and the front wheels should be slightly above the height of the tracks.
* Lay the extra angle irons on top of the secured ones and let them protrude from the oven until they are comfortably under the front wheels. Use the extra blocks to support them.
* Slowly lower the front wheels onto the the extended tracks. The jack can roll side to side to allow for perfect alignment.
* The mold can now be rolled forward until it is off the track extensions, and these extra angle irons can be removed. Throughout the process of rolling the mold, the vacuum tubes should be pushed through their respective holes in the oven wall. It can be rolled until the back casters hit the sill, striving for perfect alignment with the tracks.
* The jack can now be used (from the rear) to lift the rear casters above the height of the rails and roll the mold the rest of the way inside. It is extra important that the wheels are pre-aligned as the jack can no longer provide side to side movement.
* Once the mold is in its desired position, the wheels should be locked.

1. Open both doors.
2. Roll the mold until its front wheels are butted up against the door sill and approximately aligned with the tracks (if any of the casters are fixed direction, they should be in front).
3. Use the pallet jack (from the side) to lift the front wheels off the ground. The mold should be resting only on the rear wheels and pallet jack and the front wheels should be slightly above the height of the tracks.
4. Lay the extra angle irons on top of the secured ones and let them protrude from the oven until they are comfortably under the front wheels. Use the extra blocks to support them.
5. Slowly lower the front wheels onto the the extended tracks. The jack can roll side to side to allow for perfect alignment.
6. The mold can now be rolled forward until it is off the track extensions, and these extra angle irons can be removed. Throughout the process of rolling the mold, the vacuum tubes should be pushed through their respective holes in the oven wall. It can be rolled until the back casters hit the sill, striving for perfect alignment with the tracks.
7. The jack can now be used (from the rear) to lift the rear casters above the height of the rails and roll the mold the rest of the way inside. It is extra important that the wheels are pre-aligned as the jack can no longer provide side to side movement.
8. Once the mold is in its desired position, the wheels should be locked.

Open both doors.

Roll the mold until its front wheels are butted up against the door sill and approximately aligned with the tracks (if any of the casters are fixed direction, they should be in front).

Use the pallet jack (from the side) to lift the front wheels off the ground. The mold should be resting only on the rear wheels and pallet jack and the front wheels should be slightly above the height of the tracks.

Lay the extra angle irons on top of the secured ones and let them protrude from the oven until they are comfortably under the front wheels. Use the extra blocks to support them.

Slowly lower the front wheels onto the the extended tracks. The jack can roll side to side to allow for perfect alignment.

The mold can now be rolled forward until it is off the track extensions, and these extra angle irons can be removed. Throughout the process of rolling the mold, the vacuum tubes should be pushed through their respective holes in the oven wall. It can be rolled until the back casters hit the sill, striving for perfect alignment with the tracks.

The jack can now be used (from the rear) to lift the rear casters above the height of the rails and roll the mold the rest of the way inside. It is extra important that the wheels are pre-aligned as the jack can no longer provide side to side movement.

Once the mold is in its desired position, the wheels should be locked.

The unloading process closely resembles the loading process but in reverse. Note that since the mold must now roll up onto the track extensions, some extra force will be required. We also found it necessary to brace the extensions with our feet as this was applied. It is likely possible to devise a system in which the extension segments are shorter and align vertically with the tracks (butt up against them instead of laying over them), allowing the molds to roll out more easily. However, this would require some sort of alignment ridge beneath them and would likely be unnecessarily complicated.

Operation:

To control the temperature, we used four thermistor locations, displayed on a digital readout and manually monitored by a rotating shift of 1-2 team members. A power strip, connecting to each heater, acted as a centralized control panel. It is important that this strip has individual cutoff switches for each heater, as this allows for both minute control of the temperature distribution and the accessibility of an emergency kill switch. The vent should be held or propped open slightly any time a heater is on.

With some observation (ideally during the gradual ramp-up period), an approximate correlation between heater pulses and thermistor readings can be realized. Though this is highly dependent on the shape of the mold being baked/the outside temperature/etc., some initial trial and error should discover a sustainable heating routine, useable for the majority of the bake and only needing occasional minor adjustments. This does not necessarily mean that the heaters will always be on in parallel or for the same lengths of time. In our case, for example, “-ing” was on a much greater proportion of the time than the other two.

Using these methods, we found that we could keep all four thermistor readings within a margin of 5-10ºC of our target temperature. For added reassurance, we took frequent visual temperature readings by aiming the flir through removable portholes on the doors.

For the cooldown period, we found that little-to-no input was needed from the heaters. For the most part, the desired rate could be maintained by gradually opening the vents and portholes, using a fan to speed up the process as the temperature equalized.

Disassembly:

The insulation should be removed first, followed by the vents and rails. The plywood panels can be removed individually, leaving the 2x4 frame mostly in place. This should happen in segments, moving from one end to the other and working from top to bottom for each section.
