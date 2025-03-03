# SSCP - Lessons Learned From Topshell 1

# Lessons Learned From Topshell 1

We began our manufacturing process with a setback: we could not get our encapsulation recipe to work successfully in SunPower's laminator. This set us behind in terms of time and experience; we needed to create entirely new processes to encapsulate our largest modules internally.  That refinement process itself then took time to reach a level at which we could be confident that we could make an array that would go on Sundae.  With an accelerated timeline, we had to rush some things and work long nights to complete the array. Special thanks to Sir Eddy for his hard work, and rest in piece tempered glass, we hardly knew you.

This page serves as a starting point to our mental reset for topshell 2. We made all the mistakes we needed to make with topshell 1, and probably a few more, to make the manufacturing of topshell 2 a smooth process. As long as we keep in mind everything we have learned so far, we will have a beautiful race topshell. If we don't, our burns will be for nought. 

Note: this is not intended to provide a thorough SOP for any of our processes, but rather to remind us of the most common errors we have come across/could come across while manufacturing our next topshell.

Potting

issue: hand-mixing materials will not provide proper cure for epoxy.

solution: use air gun and dp 420

issue: tape covering underside of topshell not leaving a smooth finish on the epoxy. 

solution: place flat masking tape over hole, then several layers of duct tape behind that (preferably single) piece to provide support

issue: some holes not being filled entirely by the epoxy

solution: wait several minutes after laying first application of epoxy, then manually spread the epoxy to all the areas in which it failed to settle. add more as needed.

issue: even with dp-420, uneven curing of the epoxy sometimes occurs within the holes.

solution: if epoxy is sticky and the issue is noticed before routing has begun, note that hole, then let it sit for several more hours before trying to drill into it. if router is drilled into uncured epoxy, re-route the hole again, then refill with epoxy.

Drilling

issue: router scratching paint/carbon

solution: cover painted areas on topshell with masking then flash breaker tape. fold over edges so dust does not accumulate. also cover underside of router with flash breaker tape. 

issue: channel epoxy layer not being drilled deeply enough

solution: quantify necessary router depth required for channel re-drill after the epoxy has cured

issue: holes/channels needing to be drilled very close to the paint

solution: mark absolute boundaries with sharpie; go slowly and be careful.

issue: poor measurements of tab placement on topshell

solution: do not begin to mark placement of cutouts for tabs until all modules have been trimmed 

VHB taping

issue: uneven level of paint along edges of topshell 

solution: measure and mark variations in height, noting which thickness of VHB works best in each location

issue: some VHB not sticking as well as others to carbon fiber and/or back sheet

solution: test each type before use in module placement; change types if bond strength is unsatisfactory

issue: module unwieldiness and dexterity limitations: the larger the module, the more likely it is to bend downward and scrape the topshell with its VHB.

solution: for small- to mid-sized modules, establish an SOP between two people as to how they will lead the tabs into the holes, while a third person receives them from beneath the topshell. preferably, the same three people will perform this process for the entirety of the array to minimize miscommunications in the SOP

issue: tab tape scraping epoxy wall

solution: cut off excess tape beforehand

issue: large modules needing tabs honed in

solution: attach to end of tab some string/tape to feed through hole early in the process of laying down the module

issue: front module

solution: an SOP involving at least six people, and a lot of patience. 

Large glass

issue: vacuum bag ripping/melting against oven for full front glass encaps

solution: lay vacuum tape along top and bottom edge of glass and put vacuum bag over the tape, as a cushion. on the back of the glass, lay a 6 inch strip of vacuum tape at 14 in, 18 in, and 22 in from the edge near the top of the glass, then lay a piece of vacuum bag on top of those strips. this provides a cushion from the middle structure in the back of the oven.

issue: poor bond strength

solution: use both vacuums and do not start the timer until oven has equilibrated and is above 175C. 

issue: vacuum hoses pulling and losing seal

solution: when placing them on the tape, orient them diagonally to better facilitate their being pulled through the holes in the oven door. use excess vacuum tape around hose area; fold over excess vacuum bag to seal tape from outside in case leaks appear. post someone at oven door at all times to ensure rapid response to a vacuum leak.

Encapsulation issues

        issue: forgetting to cut out openings for the tabs in the back layer of encapsulant and in the back sheet, then threading the tabs through those openings

        solution: have the group double check that we have performed all major tasks at regular intervals

issue: double sided tape imprinting upon module

solution: precisely lay modules in central area of glass; i.e. not over the double sided tape.

issue: trimmed modules leaking encapsulant and sticking to release film

solution: spray mold release in area with good air circulation onto a paper towel. wipe this towel onto the glass, the blue release film, and the green perforated release film in areas that may come into contact with the encapsulant.

issue: poor bond strength + bubbling

solution: ensure vacuum is pulled well (clamp hoses to check for changes in pitch and inspect exhaust from the red oil vacuum for visible smoke—both are indications of poor vacuum). if bond strength is an issue, vacuum was likely not providing necessary pressure.  pull vacuum on the module again, heat in oven again—preferably before trimming to limit encapsulant spillover. this will pull bubbles closer to the edges and should help with bond strength issues. could use dp-105 method if still necessary (see Manufacturing Logistics 2017 page)

issue: adhesive from double sided tape sticking to glass post-encapsulation

solution: bathe in goo gone for ~20 minutes before using new razor blades to scrape glass

        issue: back sheet sticks to release film.

        solution: make sure top sheet covers everywhere there is encapsulant and back sheet, and then some.

Vacuum issues

issue: red vacuum leaking oil onto glass when blue vacuum is on and red is off.

solution: do not leave one vacuum on while other is off for more than a few minutes—just enough to check your vacuum seal. 

issue: blue vacuum not turning on

solution: this occurs when vacuum has already been pulled and the vacuum hose is connected to pump. pull off hose, allow air to enter the vacuum, then place the hose on the nozzle.

Oven issues

issue: error message on screen

solution: replace temperature sensor (someone enter in name of sensor)

issue: touchy controls—setting temperature to anything lower than current temp usually results in a 10-15C drop below target temp before rising again back to oven temp

solution: we want our modules to feel the burn. nothing lower than 175C should appear on the temp readout while timer is going. modules will go into oven when the screen reads 210 (for large glass) or 190 (for small glass) and then the temp will drop; once temp has bottomed out and started rising again, set temp to 185 and start timer. raise or lower temp setting as needed.

        issue: large glass, small oven

        solution: wear PPE and get extra help holding doors!

Outdoor tester

issue: inconsistent test variables

solution(s): normalize pyronometer to sun. shade cells until immediately before test is run and then immediately after to keep temperature-related efficiency loss to a minimum. perform I_sc test simultaneously on modules in question. perform all tests on cloudless days. standardize distance from vail at which the tests will occur to provide similar levels of ambient irradiance. always note the test environment.

issue: wires coming loose

solution: to be determined. talk to john

Trimming

issue: cracking cells 

solution: do not place clamps near cells; lean on straight edge not cells

issue: edge not straight

solution: use multiple clamps on straight edge, be diligent. 

issue: blank encapsulations needing trimmed 

solution: talk to danielle!

        issue: not enough extra blank area for trimming

        solution: have aero sign off on our dimensions before encapsulating. 

Soldering

deferring to Eric and Abby for this!

EL testing

issue: reaching power supply wire clamps beneath cells

solution: tape interconnect tabs to edge of corner tabs while cells are still face down so they stick out from beneath the cells and allow for easy access

Silicone seams 

issue: cracking

solution: more testing to determine specific silicone type and time relative to its curing process at which masking tape surrounding silicone should be removed

        issue: seams not covering the top of the modules 

        solution: place tape a little bit back from the edge of the module. Won't lose any aero, and it'll seal in the module better and will make masking easier. 

Module handling

issue: silicone and primer staining top sheet

solution: clean (deferring to others on methodology here)

issue: module surface scratches

solution: unless currently needed for testing, always tape tabs! and dog-ear one of the ends to ensure easy tape removal. Also, give each module its own poster board covered in clean room paper.  tape it down. minimize sliding of modules while face-down. if something (module or otherwise) is placed on top of a module, lift the thing off rather than sliding it off. preferred tape to use on modules are masking and scotch (and Kapton in specific areas)

issue: cracking

solution: only carry trimmed modules by pinching areas between cells. modules CAN bend—but only along one (standard) axis! if needed, enlist extra hands to push evenly along surface area to change orientation of the bend.

Top shell handling

        Issue: array dust cover blows off in wind; tape does not stick to carbon but does stick to paint/top sheet and will leave residue.

        solution: don't tape to the top shell itself; anchor sheet to ground/objects around top shell in strategic locations. if residue is on paint, use ONR (Optimum No Rinse) and a microfiber cloth to wipe off. Do NOT use ONR on top sheet: ONR is designed to fill in small bumps in a surface, which is great for paint, but not so much for a texturized top sheet. Use IPA instead. 

Logistics

issue: suppliers suck!

solution: finalize required inventory early on, and have all supplies for the final stretch ordered before the final stretch :)

issue: scissors

solution: we can always use more scissors

issue: organization

solution: if a subset of people clean the array area, debrief with anyone not present where the items of import (scissors, modules, tape) were placed. array shelving should be reorganized before manufacturing of second top shell.

In closing, I would like to emphasize the issue of the human factor, which does not exactly fit in any of the above categories. We needed to put in many late nights to get this array completed. Fatigue and miscommunication among the array team led to greater inefficiencies, more late nights, and thus more fatigue and miscommunication.  Here are some lessons I have learned myself about working optimally under high stress and limited time: 

* Listen to others' suggestions, even if you think you are well-versed in the area in contention. The likely cause of miscommunication is they already made the mistake you are about to, and a page like this didn't exist for you to gain the experience from. 
* Triple check on the details of your project and on the intuition behind why you're doing it at all. For example, knowing fewer seams on the car leads to better aero performance will likely help you remember to cut out an extra large top sheet, encapsulant, and back sheet during your module encapsulation.
* Speed does not directly translate to improved efficiency. Take your time, do it well the first time, and we won't have to worry about it again. 
* In major multi-person projects, like encapsulations, drilling and potting, and laying down modules, review the SOP of what you are about to do, and have quality checks of the process before every point of "no turning back." For example, before putting a module in the oven, or drilling holes in the topshell. Few mistakes we can make are irrevocable, but many can set us back days, especially when we are low on materials.
* If you are tired and noticing a degradation of work quality, switch out with someone else and take a break/nap/go home as necessary. There is a time (June 30th) for all nighters, but we also need to be healthy!

Listen to others' suggestions, even if you think you are well-versed in the area in contention. The likely cause of miscommunication is they already made the mistake you are about to, and a page like this didn't exist for you to gain the experience from. 

Triple check on the details of your project and on the intuition behind why you're doing it at all. For example, knowing fewer seams on the car leads to better aero performance will likely help you remember to cut out an extra large top sheet, encapsulant, and back sheet during your module encapsulation.

Speed does not directly translate to improved efficiency. Take your time, do it well the first time, and we won't have to worry about it again. 

In major multi-person projects, like encapsulations, drilling and potting, and laying down modules, review the SOP of what you are about to do, and have quality checks of the process before every point of "no turning back." For example, before putting a module in the oven, or drilling holes in the topshell. Few mistakes we can make are irrevocable, but many can set us back days, especially when we are low on materials.

If you are tired and noticing a degradation of work quality, switch out with someone else and take a break/nap/go home as necessary. There is a time (June 30th) for all nighters, but we also need to be healthy!

