# sunwhale-alumni-design-review-10414

## SSCP - Sunwhale Alumni Design Review 10/4/14

## Sunwhale Alumni Design Review 10/4/14

Presentation here.

[here](https://docs.google.com/presentation/d/1L63XqnINg4eHKKn82E4TCfEVgrG8vFgCSK5-IKXJejs/edit?usp=sharing)

Topics: Aero, suspension, chassis, procurement timelines, regulation compliance, array, concentrators, topshell alignment & latching, car body seam placement, canopy construction, BMS hardware & code, battery pack testing, composites testing, budget.

Alumni: Wesley, Forest, Rachel Fenichel, DC, Paul Karplus, Sam Lenius, Ian Girard, DC, Danny, NHS

* Aero is in the 33-40N range as is. Settled on general car shape, mainfoil, etc. Tweaking for better drag <=30N. Have crosswind simulations, can make additional adjustments to better optimize.Aero + suspension interplay: Fitting suspension hardpointsincreasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?) bringing the mounting points towards outside of car (shorter arms)different arm geometryDanny: Increasing fillet radius should not induce a drag penalty if we do it right. If we balance everything, should be able to mitigate Venturi effect.Forest: have we considered meta-fairings / sealing the wheel wells? This is also space to take into consideration, in terms of wheel volumes.ChassisProbably have to buy panels Wesley: Shock adjustability? For Xenith had to change the pressure in the shocks, which also changed other shock dynamicsWesley: Order shocks early once we have them picked. High in demand from American FSAE teams. (Tried to buy more right before race for Luminos, KAZ was sold out.)Chassis panels to aerobody: Wesley: Construction process? Xenith style, laying up panels into bottom shell and carbon over it Luminos style, construct shells, construct chassis, glue togetherLayup plan all over spring break (! woooo !! ) Give people a heads up / put on SSCP Google CalendarSuspension (Aravind)Multilink double wishbone geometry, similar to LuminosShock mounted on lower control arm to simplify upright designCurrently validating Matlab script for calculating loadsGuillermo on procurement / timelines for a few things:Solar cellsBuying 600 Bin K (need ~~400 for car)Leftover Bin J for testingWesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.Michelin tiresAwaiting a French shipmentWesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.Order qty: 20?Molds & ChristensenThings are good with them, built/ding good relationshipPotential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"InsertsClickbond - Order now? BatteriesCan't get sponsored from Panasonic from the same source as earlier. In contact with Paul Denning, Panasonic, looking around for other sourcesAlso talking with Tesla, but up in the airFor test pack, probably enough left from Luminos (3.4s)New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?ShocksTalk to KAZ, put down dp on shocksWaiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)Material stockCarbon, core - shittonGo through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)Metals - Sponsorship & procurement, good underclassmen project?\* VW has an implicit exclusivity agreement with our team \* (Be sensitive with mention of Tesla, etc.Array3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!Currently have Luminos EVA, have another Bridgestone one to test nextAccess to lamination machines at SunPowerSunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (~~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapesIn conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stopsAlternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulezMatt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia\* Could get Catia via Boeing if we wanted \*Vinyl / Paint3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on itLower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paintConcentratorsSemprius - Did Nuna concentrators, "working with another team"Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairingWesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimateHave we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phaseTopshell alignment, latching, charging strategyConcentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurationsSam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hitGoing to use a topshell design (vs. monocoque)Seam PlacementCut out along array (topshell = array inset)Split down middle of carSusan/Charlie looking into alignment and latchingWesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.Driver canopy construction (Lisa)Carbon mold negative for inset where windscreen is spacedTherformed polycarb segments of window (rather than whole bubble)Could be thinner than in Luminos, because won't be constrained by thickness of trailing edgeGlue in w/ VHB or epoxy + glass beadsFor seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive toolingIan: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?Battery pack layout (Emily)15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)Pack layouts, 15x32" \~ish.Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)Composites (Jamie)Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEAInsert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used whereTextreme (wet layups for spread-toe) requires more skill / less variable team sizeWesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.Forest: Bigger coupons are better, for testing.
* Aero is in the 33-40N range as is. Settled on general car shape, mainfoil, etc. Tweaking for better drag <=30N. Have crosswind simulations, can make additional adjustments to better optimize.
* Aero + suspension interplay: Fitting suspension hardpointsincreasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?) bringing the mounting points towards outside of car (shorter arms)different arm geometry
* increasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?)&#x20;
* bringing the mounting points towards outside of car (shorter arms)
* different arm geometry
* Danny: Increasing fillet radius should not induce a drag penalty if we do it right. If we balance everything, should be able to mitigate Venturi effect.
* Forest: have we considered meta-fairings / sealing the wheel wells? This is also space to take into consideration, in terms of wheel volumes.
* ChassisProbably have to buy panels&#x20;
* Probably have to buy panels&#x20;
* Wesley: Shock adjustability? For Xenith had to change the pressure in the shocks, which also changed other shock dynamics
* Wesley: Order shocks early once we have them picked. High in demand from American FSAE teams. (Tried to buy more right before race for Luminos, KAZ was sold out.)
* Chassis panels to aerobody:&#x20;
* Wesley: Construction process? Xenith style, laying up panels into bottom shell and carbon over it Luminos style, construct shells, construct chassis, glue together
* Xenith style, laying up panels into bottom shell and carbon over it&#x20;
* Luminos style, construct shells, construct chassis, glue together
* Layup plan all over spring break (! woooo !! ) Give people a heads up / put on SSCP Google Calendar
* Give people a heads up / put on SSCP Google Calendar
* Suspension (Aravind)Multilink double wishbone geometry, similar to LuminosShock mounted on lower control arm to simplify upright designCurrently validating Matlab script for calculating loads
* Multilink double wishbone geometry, similar to Luminos
* Shock mounted on lower control arm to simplify upright design
* Currently validating Matlab script for calculating loads
* Guillermo on procurement / timelines for a few things:
* Solar cellsBuying 600 Bin K (need \~400 for car)Leftover Bin J for testingWesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.
* Buying 600 Bin K (need \~400 for car)
* Leftover Bin J for testing
* Wesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.
* Michelin tiresAwaiting a French shipmentWesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.Order qty: 20?
* Awaiting a French shipment
* Wesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.
* Order qty: 20?
* Molds & ChristensenThings are good with them, built/ding good relationshipPotential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"
* Things are good with them, built/ding good relationship
* Potential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but&#x20;
* Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"
* Ian: "If it ain't broke don't fix it"
* InsertsClickbond - Order now?&#x20;
* Clickbond - Order now?&#x20;
* BatteriesCan't get sponsored from Panasonic from the same source as earlier. In contact with Paul Denning, Panasonic, looking around for other sourcesAlso talking with Tesla, but up in the airFor test pack, probably enough left from Luminos (3.4s)New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?
* Can't get sponsored from Panasonic from the same source as earlier.&#x20;
* In contact with Paul Denning, Panasonic, looking around for other sources
* Also talking with Tesla, but up in the air
* For test pack, probably enough left from Luminos (3.4s)
* New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?
* ShocksTalk to KAZ, put down dp on shocksWaiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)
* Talk to KAZ, put down dp on shocks
* Waiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)
* Material stockCarbon, core - shittonGo through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)Metals - Sponsorship & procurement, good underclassmen project?
* Carbon, core - shitton
* Go through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)
* Metals - Sponsorship & procurement, good underclassmen project?
*
  * VW has an implicit exclusivity agreement with our team \* (Be sensitive with mention of Tesla, etc.
* Array3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!Currently have Luminos EVA, have another Bridgestone one to test nextAccess to lamination machines at SunPowerSunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapesIn conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stopsAlternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulezMatt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia
* 3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* 3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* Currently have Luminos EVA, have another Bridgestone one to test next
* Access to lamination machines at SunPower
* SunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Would look into if it is the same topsheet?
* Booked for the new style
* \--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Wesley: Probably not worth if we have SunPower lab access
* Would lose out on team knowledge / experience? Could still make backup modules?
* To improve efficiency of our own layup process, make more standardized array module shapes
* In conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stops
* Cooling for array, esp. during control stops
* Alternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Matt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia
* Can't do it properly in SolidWorks, could in Catia
*
  * Could get Catia via Boeing if we wanted \*
* Vinyl / Paint3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on itLower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint
* 3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on it
* Lower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint
* ConcentratorsSemprius - Did Nuna concentrators, "working with another team"Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairingWesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimateHave we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phase
* Semprius - Did Nuna concentrators, "working with another team"
* Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Made for larger scale commercial layouts, but we could modify / collapse them for fit and use in car
* Need to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Make module static or collapsible
* How to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* ElectricalsDo-able.
* Do-able.
* Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Wesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimate
* Sam Lenius: "You can learn a lot of things just by holding things."
* Use a toy model to refine our performance estimate
* Have we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phase
* Tradeoff is <1 SunPower cell, in terms of cell area
* Could just ditch out of car day before race
* Big risk is in the time/resources/manpower during design phase
* Topshell alignment, latching, charging strategyConcentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurationsSam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hitGoing to use a topshell design (vs. monocoque)Seam PlacementCut out along array (topshell = array inset)Split down middle of carSusan/Charlie looking into alignment and latchingWesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.
* Concentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurations
* 34 concentrators \~ +500 additional Watts
* Sam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.
* Diagrams of charging / angle / concentrator # configurations
* Sam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hit
* Going to use a topshell design (vs. monocoque)
* Seam PlacementCut out along array (topshell = array inset)Split down middle of car
* Cut out along array (topshell = array inset)
* Split down middle of car
* Susan/Charlie looking into alignment and latching
* Wesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.
* Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.
* Structure/support for car while standing is a big concern -- high winds.
* Driver canopy construction (Lisa)Carbon mold negative for inset where windscreen is spacedTherformed polycarb segments of window (rather than whole bubble)Could be thinner than in Luminos, because won't be constrained by thickness of trailing edgeGlue in w/ VHB or epoxy + glass beadsFor seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive toolingIan: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?
* Carbon mold negative for inset where windscreen is spaced
* Therformed polycarb segments of window (rather than whole bubble)
* Could be thinner than in Luminos, because won't be constrained by thickness of trailing edge
* Glue in w/ VHB or epoxy + glass beads
* For seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Wesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in molds
* Ian: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Polycarb is more industry standard than what was used on Luminos (PETG)
* Hard clear coat / other coatings?
* Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Ian: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.
* Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?
* Battery pack layout (Emily)15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)Pack layouts, 15x32" \~ish.Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)
* 15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)
* Pack layouts, 15x32" \~ish.
* Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* \--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)
* Composites (Jamie)Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEAInsert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used whereTextreme (wet layups for spread-toe) requires more skill / less variable team sizeWesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.Forest: Bigger coupons are better, for testing.
* Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.
* Testing sample sections car: weave/core/uni/core/etc.
* Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.
* End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Insert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used where
* Sam: Find out failure modes & can optimize what sizes are used where
* Textreme (wet layups for spread-toe) requires more skill / less variable team size
* Wesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.
* Forest: Bigger coupons are better, for testing.
* Aero is in the 33-40N range as is. Settled on general car shape, mainfoil, etc. Tweaking for better drag <=30N. Have crosswind simulations, can make additional adjustments to better optimize.
* Aero + suspension interplay: Fitting suspension hardpointsincreasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?) bringing the mounting points towards outside of car (shorter arms)different arm geometry
* increasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?)&#x20;
* bringing the mounting points towards outside of car (shorter arms)
* different arm geometry
* Danny: Increasing fillet radius should not induce a drag penalty if we do it right. If we balance everything, should be able to mitigate Venturi effect.
* Forest: have we considered meta-fairings / sealing the wheel wells? This is also space to take into consideration, in terms of wheel volumes.
* ChassisProbably have to buy panels&#x20;
* Probably have to buy panels&#x20;
* Wesley: Shock adjustability? For Xenith had to change the pressure in the shocks, which also changed other shock dynamics
* Wesley: Order shocks early once we have them picked. High in demand from American FSAE teams. (Tried to buy more right before race for Luminos, KAZ was sold out.)
* Chassis panels to aerobody:&#x20;
* Wesley: Construction process? Xenith style, laying up panels into bottom shell and carbon over it Luminos style, construct shells, construct chassis, glue together
* Xenith style, laying up panels into bottom shell and carbon over it&#x20;
* Luminos style, construct shells, construct chassis, glue together
* Layup plan all over spring break (! woooo !! ) Give people a heads up / put on SSCP Google Calendar
* Give people a heads up / put on SSCP Google Calendar
* Suspension (Aravind)Multilink double wishbone geometry, similar to LuminosShock mounted on lower control arm to simplify upright designCurrently validating Matlab script for calculating loads
* Multilink double wishbone geometry, similar to Luminos
* Shock mounted on lower control arm to simplify upright design
* Currently validating Matlab script for calculating loads
* Guillermo on procurement / timelines for a few things:
* Solar cellsBuying 600 Bin K (need \~400 for car)Leftover Bin J for testingWesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.
* Buying 600 Bin K (need \~400 for car)
* Leftover Bin J for testing
* Wesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.
* Michelin tiresAwaiting a French shipmentWesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.Order qty: 20?
* Awaiting a French shipment
* Wesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.
* Order qty: 20?
* Molds & ChristensenThings are good with them, built/ding good relationshipPotential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"
* Things are good with them, built/ding good relationship
* Potential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but&#x20;
* Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"
* Ian: "If it ain't broke don't fix it"
* InsertsClickbond - Order now?&#x20;
* Clickbond - Order now?&#x20;
* BatteriesCan't get sponsored from Panasonic from the same source as earlier. In contact with Paul Denning, Panasonic, looking around for other sourcesAlso talking with Tesla, but up in the airFor test pack, probably enough left from Luminos (3.4s)New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?
* Can't get sponsored from Panasonic from the same source as earlier.&#x20;
* In contact with Paul Denning, Panasonic, looking around for other sources
* Also talking with Tesla, but up in the air
* For test pack, probably enough left from Luminos (3.4s)
* New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?
* ShocksTalk to KAZ, put down dp on shocksWaiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)
* Talk to KAZ, put down dp on shocks
* Waiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)
* Material stockCarbon, core - shittonGo through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)Metals - Sponsorship & procurement, good underclassmen project?
* Carbon, core - shitton
* Go through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)
* Metals - Sponsorship & procurement, good underclassmen project?
*
  * VW has an implicit exclusivity agreement with our team \* (Be sensitive with mention of Tesla, etc.
* Array3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!Currently have Luminos EVA, have another Bridgestone one to test nextAccess to lamination machines at SunPowerSunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapesIn conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stopsAlternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulezMatt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia
* 3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* 3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* Currently have Luminos EVA, have another Bridgestone one to test next
* Access to lamination machines at SunPower
* SunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Would look into if it is the same topsheet?
* Booked for the new style
* \--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Wesley: Probably not worth if we have SunPower lab access
* Would lose out on team knowledge / experience? Could still make backup modules?
* To improve efficiency of our own layup process, make more standardized array module shapes
* In conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stops
* Cooling for array, esp. during control stops
* Alternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Matt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia
* Can't do it properly in SolidWorks, could in Catia
*
  * Could get Catia via Boeing if we wanted \*
* Vinyl / Paint3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on itLower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint
* 3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on it
* Lower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint
* ConcentratorsSemprius - Did Nuna concentrators, "working with another team"Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairingWesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimateHave we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phase
* Semprius - Did Nuna concentrators, "working with another team"
* Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Made for larger scale commercial layouts, but we could modify / collapse them for fit and use in car
* Need to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Make module static or collapsible
* How to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* ElectricalsDo-able.
* Do-able.
* Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Wesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimate
* Sam Lenius: "You can learn a lot of things just by holding things."
* Use a toy model to refine our performance estimate
* Have we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phase
* Tradeoff is <1 SunPower cell, in terms of cell area
* Could just ditch out of car day before race
* Big risk is in the time/resources/manpower during design phase
* Topshell alignment, latching, charging strategyConcentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurationsSam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hitGoing to use a topshell design (vs. monocoque)Seam PlacementCut out along array (topshell = array inset)Split down middle of carSusan/Charlie looking into alignment and latchingWesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.
* Concentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurations
* 34 concentrators \~ +500 additional Watts
* Sam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.
* Diagrams of charging / angle / concentrator # configurations
* Sam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hit
* Going to use a topshell design (vs. monocoque)
* Seam PlacementCut out along array (topshell = array inset)Split down middle of car
* Cut out along array (topshell = array inset)
* Split down middle of car
* Susan/Charlie looking into alignment and latching
* Wesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.
* Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.
* Structure/support for car while standing is a big concern -- high winds.
* Driver canopy construction (Lisa)Carbon mold negative for inset where windscreen is spacedTherformed polycarb segments of window (rather than whole bubble)Could be thinner than in Luminos, because won't be constrained by thickness of trailing edgeGlue in w/ VHB or epoxy + glass beadsFor seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive toolingIan: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?
* Carbon mold negative for inset where windscreen is spaced
* Therformed polycarb segments of window (rather than whole bubble)
* Could be thinner than in Luminos, because won't be constrained by thickness of trailing edge
* Glue in w/ VHB or epoxy + glass beads
* For seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Wesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in molds
* Ian: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Polycarb is more industry standard than what was used on Luminos (PETG)
* Hard clear coat / other coatings?
* Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Ian: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.
* Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?
* Battery pack layout (Emily)15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)Pack layouts, 15x32" \~ish.Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)
* 15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)
* Pack layouts, 15x32" \~ish.
* Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* \--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)
* Composites (Jamie)Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEAInsert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used whereTextreme (wet layups for spread-toe) requires more skill / less variable team sizeWesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.Forest: Bigger coupons are better, for testing.
* Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.
* Testing sample sections car: weave/core/uni/core/etc.
* Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.
* End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Insert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used where
* Sam: Find out failure modes & can optimize what sizes are used where
* Textreme (wet layups for spread-toe) requires more skill / less variable team size
* Wesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.
* Forest: Bigger coupons are better, for testing.

Aero is in the 33-40N range as is. Settled on general car shape, mainfoil, etc. Tweaking for better drag <=30N. Have crosswind simulations, can make additional adjustments to better optimize.

Aero + suspension interplay: Fitting suspension hardpoints

* increasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?)&#x20;
* bringing the mounting points towards outside of car (shorter arms)
* different arm geometry

increasing fairing/body fillet radius on underside, to make room for suspension travel in jounce (?)&#x20;

bringing the mounting points towards outside of car (shorter arms)

different arm geometry

Danny: Increasing fillet radius should not induce a drag penalty if we do it right. If we balance everything, should be able to mitigate Venturi effect.

Forest: have we considered meta-fairings / sealing the wheel wells? This is also space to take into consideration, in terms of wheel volumes.

Chassis

* Probably have to buy panels&#x20;

Probably have to buy panels&#x20;

Wesley: Shock adjustability? For Xenith had to change the pressure in the shocks, which also changed other shock dynamics

Wesley: Order shocks early once we have them picked. High in demand from American FSAE teams. (Tried to buy more right before race for Luminos, KAZ was sold out.)

Chassis panels to aerobody:&#x20;

Wesley: Construction process?&#x20;

* Xenith style, laying up panels into bottom shell and carbon over it&#x20;
* Luminos style, construct shells, construct chassis, glue together

Xenith style, laying up panels into bottom shell and carbon over it&#x20;

Luminos style, construct shells, construct chassis, glue together

Layup plan all over spring break (! woooo !! )&#x20;

* Give people a heads up / put on SSCP Google Calendar

Give people a heads up / put on SSCP Google Calendar

Suspension (Aravind)

* Multilink double wishbone geometry, similar to Luminos
* Shock mounted on lower control arm to simplify upright design
* Currently validating Matlab script for calculating loads

Multilink double wishbone geometry, similar to Luminos

Shock mounted on lower control arm to simplify upright design

Currently validating Matlab script for calculating loads

Guillermo on procurement / timelines for a few things:

Solar cells

* Buying 600 Bin K (need \~400 for car)
* Leftover Bin J for testing
* Wesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.

Buying 600 Bin K (need \~400 for car)

Leftover Bin J for testing

Wesley: Would we be able to buy another 200 cells if we realized over the summer that we needed to make another array? Look into being able to acquire another car's worth, presenting that case of a last minute need.

Michelin tires

* Awaiting a French shipment
* Wesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.
* Order qty: 20?

Awaiting a French shipment

Wesley: Put in a PO or whatever to firmly initialize. Be aggressive, it's a competitive market.

Order qty: 20?

Molds & Christensen

* Things are good with them, built/ding good relationship
* Potential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but&#x20;
* Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.Ian: "If it ain't broke don't fix it"
* Ian: "If it ain't broke don't fix it"

Things are good with them, built/ding good relationship

Potential visit to maintain our good relationship - en route to Aerodyn would be good. Molds are long done, but&#x20;

Haven't looked into any other mold manufacturers (Wesley's previous suggestion?) hard to do without being rude / endangering a relationship; things with Christensen are solid.

* Ian: "If it ain't broke don't fix it"

Ian: "If it ain't broke don't fix it"

Inserts

* Clickbond - Order now?&#x20;

Clickbond - Order now?&#x20;

Batteries

* Can't get sponsored from Panasonic from the same source as earlier.&#x20;
* In contact with Paul Denning, Panasonic, looking around for other sources
* Also talking with Tesla, but up in the air
* For test pack, probably enough left from Luminos (3.4s)
* New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?

Can't get sponsored from Panasonic from the same source as earlier.&#x20;

In contact with Paul Denning, Panasonic, looking around for other sources

Also talking with Tesla, but up in the air

For test pack, probably enough left from Luminos (3.4s)

New cell capacity (3.6) is out, but we probably won't be able to get our hands on them?

Shocks

* Talk to KAZ, put down dp on shocks
* Waiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)

Talk to KAZ, put down dp on shocks

Waiting on weight distribution for shock specifications (need to know within 5 lbs for shocks)

Material stock

* Carbon, core - shitton
* Go through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)
* Metals - Sponsorship & procurement, good underclassmen project?

Carbon, core - shitton

Go through Luminos order list and make sure misc. items are all accounted for (e.g. foaming adhesive, etc.)

Metals - Sponsorship & procurement, good underclassmen project?

* VW has an implicit exclusivity agreement with our team \* (Be sensitive with mention of Tesla, etc.

Array

* 3M topsheet from Luminos is the best that we've tested yet3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* 3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!
* Currently have Luminos EVA, have another Bridgestone one to test next
* Access to lamination machines at SunPower
* SunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cellWould look into if it is the same topsheet?Booked for the new style--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Would look into if it is the same topsheet?
* Booked for the new style
* \--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Wesley: Probably not worth if we have SunPower lab access
* Would lose out on team knowledge / experience? Could still make backup modules?
* To improve efficiency of our own layup process, make more standardized array module shapes
* In conversation with company ThermaCore, with product K-Core for thermal conductivityCooling for array, esp. during control stops
* Cooling for array, esp. during control stops
* Alternatively, focus efforts on cooling during control stops Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez
* Matt's diagram of modules / layout on carCan't do it properly in SolidWorks, could in Catia
* Can't do it properly in SolidWorks, could in Catia

3M topsheet from Luminos is the best that we've tested yet

* 3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!

3M contact visit was successful -- gave him some sample, found potentially more efficient version, might go through?!

Currently have Luminos EVA, have another Bridgestone one to test next

Access to lamination machines at SunPower

SunCat encapsulation - Has room for "legacy encapsulation" (same as Luminos), for $32 / cell

* Would look into if it is the same topsheet?
* Booked for the new style
* \--> Is this worthwhile? (\~$20k array) MONEY VS TIMEWesley: Probably not worth if we have SunPower lab accessWould lose out on team knowledge / experience? Could still make backup modules?To improve efficiency of our own layup process, make more standardized array module shapes
* Wesley: Probably not worth if we have SunPower lab access
* Would lose out on team knowledge / experience? Could still make backup modules?
* To improve efficiency of our own layup process, make more standardized array module shapes

Would look into if it is the same topsheet?

Booked for the new style

\--> Is this worthwhile? (\~$20k array) MONEY VS TIME

* Wesley: Probably not worth if we have SunPower lab access
* Would lose out on team knowledge / experience? Could still make backup modules?
* To improve efficiency of our own layup process, make more standardized array module shapes

Wesley: Probably not worth if we have SunPower lab access

Would lose out on team knowledge / experience? Could still make backup modules?

To improve efficiency of our own layup process, make more standardized array module shapes

In conversation with company ThermaCore, with product K-Core for thermal conductivity

* Cooling for array, esp. during control stops

Cooling for array, esp. during control stops

Alternatively, focus efforts on cooling during control stops&#x20;

* Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez

Conveniently, a large fan for "cooling the people holding the array up"? <-- Look into rulez

Matt's diagram of modules / layout on car

* Can't do it properly in SolidWorks, could in Catia

Can't do it properly in SolidWorks, could in Catia

* Could get Catia via Boeing if we wanted \*

Vinyl / Paint

* 3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on it
* Lower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint

3M could pre-print our vinyl, given car shape, with logos/etc. pre-printed on it

Lower priority. Time crunch = 2 color solid vinyl, more time = printed vinyl / get a sponsor involved, more more time = paint

Concentrators

* Semprius - Did Nuna concentrators, "working with another team"
* Arzon Solar - New partnership, makes concentrator unitsMade for larger scale commercial layouts, but we could modify / collapse them for fit and use in carNeed to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracyElectricalsDo-able.Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Made for larger scale commercial layouts, but we could modify / collapse them for fit and use in car
* Need to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Make module static or collapsible
* How to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* ElectricalsDo-able.
* Do-able.
* Do a model fit with wheel, concentrators, batteries, + other elements in fairing
* Wesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?Sam Lenius: "You can learn a lot of things just by holding things."Use a toy model to refine our performance estimate
* Sam Lenius: "You can learn a lot of things just by holding things."
* Use a toy model to refine our performance estimate
* Have we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.Tradeoff is <1 SunPower cell, in terms of cell areaCould just ditch out of car day before raceBig risk is in the time/resources/manpower during design phase
* Tradeoff is <1 SunPower cell, in terms of cell area
* Could just ditch out of car day before race
* Big risk is in the time/resources/manpower during design phase

Semprius - Did Nuna concentrators, "working with another team"

Arzon Solar - New partnership, makes concentrator units

* Made for larger scale commercial layouts, but we could modify / collapse them for fit and use in car
* Need to decide:Make module static or collapsibleHow to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Make module static or collapsible
* How to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* ElectricalsDo-able.
* Do-able.
* Do a model fit with wheel, concentrators, batteries, + other elements in fairing

Made for larger scale commercial layouts, but we could modify / collapse them for fit and use in car

Need to decide:

* Make module static or collapsible
* How to trackingNeed +/- 1 degree accuracyBuild a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy
* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy

Make module static or collapsible

How to tracking

* Need +/- 1 degree accuracy
* Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy

Need +/- 1 degree accuracy

Build a prototype to see what kind of mechanism (+ collapsibility?) needed for that accuracy

Electricals

* Do-able.

Do-able.

Do a model fit with wheel, concentrators, batteries, + other elements in fairing

Wesley: Can we get our hands on any concentrator, even another company, to play around with in the shop?

* Sam Lenius: "You can learn a lot of things just by holding things."
* Use a toy model to refine our performance estimate

Sam Lenius: "You can learn a lot of things just by holding things."

Use a toy model to refine our performance estimate

Have we considered the trade-offs / risks? Only 1 team has ever pulled it off successfully.

* Tradeoff is <1 SunPower cell, in terms of cell area
* Could just ditch out of car day before race
* Big risk is in the time/resources/manpower during design phase

Tradeoff is <1 SunPower cell, in terms of cell area

Could just ditch out of car day before race

Big risk is in the time/resources/manpower during design phase

Topshell alignment, latching, charging strategy

* Concentrator charging at beginning / end of day (would not use during control stops)34 concentrators \~ +500 additional WattsSam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.Diagrams of charging / angle / concentrator # configurations
* 34 concentrators \~ +500 additional Watts
* Sam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.
* Diagrams of charging / angle / concentrator # configurations
* Sam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hit
* Going to use a topshell design (vs. monocoque)
* Seam PlacementCut out along array (topshell = array inset)Split down middle of car
* Cut out along array (topshell = array inset)
* Split down middle of car
* Susan/Charlie looking into alignment and latching
* Wesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.
* Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array). Structure/support for car while standing is a big concern -- high winds.
* Structure/support for car while standing is a big concern -- high winds.

Concentrator charging at beginning / end of day (would not use during control stops)

* 34 concentrators \~ +500 additional Watts
* Sam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.
* Diagrams of charging / angle / concentrator # configurations

34 concentrators \~ +500 additional Watts

Sam Lenius: Did we take into consideration the atmospheric effects? Evening different from solar noon.

Diagrams of charging / angle / concentrator # configurations

Sam Lenius: Could pop off bubble during charging and replace with concentrators. Tracker design is critical if we're blocking any cells, because all the cells on that module will take a hit

Going to use a topshell design (vs. monocoque)

Seam Placement

* Cut out along array (topshell = array inset)
* Split down middle of car

Cut out along array (topshell = array inset)

Split down middle of car

Susan/Charlie looking into alignment and latching

Wesley: Luminos focused much more on hinging & latching, than seam construction. Worked out well. Door was stiff enough on its own. Make sure latching system works very well.

Sam/Wesley: Hinged array to car, like whole 4-bar linkage. (Could prop up car on its own hinged array).&#x20;

* Structure/support for car while standing is a big concern -- high winds.

Structure/support for car while standing is a big concern -- high winds.

Driver canopy construction (Lisa)

* Carbon mold negative for inset where windscreen is spaced
* Therformed polycarb segments of window (rather than whole bubble)
* Could be thinner than in Luminos, because won't be constrained by thickness of trailing edge
* Glue in w/ VHB or epoxy + glass beads
* For seamWesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in moldsIan: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Wesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in molds
* Ian: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.
* Sam: How can we improve the optical clarity? Luminos was not up to snuffPolycarb is more industry standard than what was used on Luminos (PETG)Hard clear coat / other coatings?Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Polycarb is more industry standard than what was used on Luminos (PETG)
* Hard clear coat / other coatings?
* Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling
* Ian: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.
* Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?

Carbon mold negative for inset where windscreen is spaced

Therformed polycarb segments of window (rather than whole bubble)

Could be thinner than in Luminos, because won't be constrained by thickness of trailing edge

Glue in w/ VHB or epoxy + glass beads

For seam

* Wesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in molds
* Ian: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.

Wesley: If we got plastic early enough, could do layup (@ lower temp or higher temp plastic) w/ bubble in molds

Ian: Thermoforming is inherently 'unstable' as you stretch/deform a material, so there's going to need to be a lost of post-work anyhow to get the seam nice. Only so much you can do in CAD.

Sam: How can we improve the optical clarity? Luminos was not up to snuff

* Polycarb is more industry standard than what was used on Luminos (PETG)
* Hard clear coat / other coatings?
* Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling

Polycarb is more industry standard than what was used on Luminos (PETG)

Hard clear coat / other coatings?

Polycarb needs an aluminum plug (Tokai) = suuper expensive tooling

Ian: Doesn't make the car go faster at the end of the day. You can see well enough. Race car for one race.

Wesley: Look into other industries? Other things that care about optical clarity / thermoforming. Helicopter windscreens? Radar things?

Battery pack layout (Emily)

* 15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)
* Pack layouts, 15x32" \~ish.
* Fitting electronics needs to be considered. Number of boards are increasing.--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* \--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?
* Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)

15 parallel, 27 series --> same voltage as Luminos, allows using the same motors (for a negligible continuous power loss over the more favorable configuration; not worth changing motors for)

Pack layouts, 15x32" \~ish.

Fitting electronics needs to be considered. Number of boards are increasing.

* \--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?

\--> Need to think about / someone responsible for pack as a whole. (Mech + EE integration) Emily?

Talking with a 3D printing company for the clamshells. Faster & cheaper & more modifiable than injection molding. (Guillermo)

Composites (Jamie)

* Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipmentTesting sample sections car: weave/core/uni/core/etc.
* Testing sample sections car: weave/core/uni/core/etc.
* Ian: What numbers are we seeking that will make the car faster?Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Knowledge / better intuition / data about what strengths & what thicknesses are required where.
* Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.
* End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Much more useful data. Something we can derive aktual knowledge from / can't FEA
* Insert testing is even more usefulSam: Find out failure modes & can optimize what sizes are used where
* Sam: Find out failure modes & can optimize what sizes are used where
* Textreme (wet layups for spread-toe) requires more skill / less variable team size
* Wesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.
* Forest: Bigger coupons are better, for testing.

Contact at SACL (Structures & Composites Lab), toured & presenting with them to use their equipment

* Testing sample sections car: weave/core/uni/core/etc.

Testing sample sections car: weave/core/uni/core/etc.

Ian: What numbers are we seeking that will make the car faster?

* Knowledge / better intuition / data about what strengths & what thicknesses are required where.

Knowledge / better intuition / data about what strengths & what thicknesses are required where.

Forest: Failure modes are super complicated. To test core, sit on it? Nothing useful we can do with impact testing.

End bond testing (Carbon vs. epoxy fillets): Ian/Forest +++

* Much more useful data. Something we can derive aktual knowledge from / can't FEA

Much more useful data. Something we can derive aktual knowledge from / can't FEA

Insert testing is even more useful

* Sam: Find out failure modes & can optimize what sizes are used where

Sam: Find out failure modes & can optimize what sizes are used where

Textreme (wet layups for spread-toe) requires more skill / less variable team size

Wesley: Do really good documentation, to make it useful for you in 2 months and for the next team. Photos, upload on site, etc.

Forest: Bigger coupons are better, for testing.

Don't be afraid to throw stuff out on solarcore more often. Sunwhale has been quieter than previous cars, alumni will always be happy to chime in on there. - Wesley

Alumni Email Feedback

* ArrayCan you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.Chassis, suspension, and aeroHas the whole automatic deformation thing started working?Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.Canopy, windscreen, moving body parts in generalThe easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.BatteryI didn't parse what 'affirmative' and 'negative' mean.Why is BMS volume increasing?DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.
* ArrayCan you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.
* Can you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.
* ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* You have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.
* In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.
* If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.
* Chassis, suspension, and aeroHas the whole automatic deformation thing started working?Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.
* Has the whole automatic deformation thing started working?
* Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.
* Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.
* Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.
* The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.
* SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.
* Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.
* Canopy, windscreen, moving body parts in generalThe easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.
* The easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.
* There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.
* Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.
* BatteryI didn't parse what 'affirmative' and 'negative' mean.Why is BMS volume increasing?DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.
* I didn't parse what 'affirmative' and 'negative' mean.
* Why is BMS volume increasing?
* DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.
* ArrayCan you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.
* Can you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.
* ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* You have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.
* In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.
* If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.
* Chassis, suspension, and aeroHas the whole automatic deformation thing started working?Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.
* Has the whole automatic deformation thing started working?
* Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.
* Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.
* Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.
* The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.
* SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.
* Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.
* Canopy, windscreen, moving body parts in generalThe easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.
* The easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.
* There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.
* Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.
* BatteryI didn't parse what 'affirmative' and 'negative' mean.Why is BMS volume increasing?DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.
* I didn't parse what 'affirmative' and 'negative' mean.
* Why is BMS volume increasing?
* DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.

Array

* Can you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.
* ThermalsYou have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* You have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.
* In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.
* Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.
* If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.

Can you get 1000 cells? Having enough for two arrays is comforting, especially if you plan on encapsulating yourself. They're cheap enough that there's little reason not to if you can.

Thermals

* You have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.
* In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.

You have a low-wattage, high-area, high-uniformity heat dissipation problem. It's hard to imagine how a spreading material (like k-core) would help in this context. If you had highly localized sources of heat (like transistors), that would be a different story. But you don't.

In your case you have only a few ways to try to improve. Best performance per effort is perforating the carbon behind the cells to get heat out from both sides. Next best is to reduce lamination stack thickness and maximize thermal conductivity. Encapsulating with silicone (or silicone gel) would probably be a big improvement, but would be nontrivial R\&D. Figuring out how to implement an infrared mirror could be a massive improvement, even if it costs some transmission, but would probably be difficult to do. Luckily you're not cost constrained.

Has anybody done research on figuring out what Chuzel's new hotness is? You can probably get some broken or reject panel for analysis from another team unless there are contractual obligations between them and Suncat.

If you do make your own array, budget time and money to build some jigs and automation to make your life easier. Really, really, try to have as few types of panels as possible. One is ideal. Two is livable. Three or more is awful. Stick to rectangles.

Chassis, suspension, and aero

* Has the whole automatic deformation thing started working?
* Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.
* Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.
* Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.
* The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.
* SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.
* Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.

Has the whole automatic deformation thing started working?

Consider staying with a monocoque. If anybody wants a reminder of how crappy dealing with two shells is, let me know and we can look at Apogee together. Making this decision based on a speculative inclusion (concentrators) seems unwarranted.

Having sharp corners at the bottoms of fairings seems like a mistake. Everywhere else in aero you want smooth fillets. What about the fairings makes it desirable to sharp fillets near the ground? Further, those will get hung up on small bumps and generally get destroyed. Putting a bit of a taper on those in the long direction makes them much easier to live with after a car is made.

Catamaran car, sure, but consider sucking in the region between the two wheel boxes a little bit. Right now you have about zero ground clearance, so a speed bump will result in a beached sunwhale.

The superposition of wheel locations in the suspension model doesn't include bumps at either end of steering lock. You should do a motion study and come up with the complete volume swept over the full range of motion. Then figure out how much you think the suspension and wheel will flex (it bends more than you think!) and inflate your volume by that amount.

SSCP should suck it up and do a proper meta fairing around the wheel. By all accounts this is a significant aero improvement, but even without that it's a win for cleanliness and safety inside the car. It ensures that road debris is not kicked up into the driver cavity.

Get more shocks than you think you need. Try to stick to coil-over designs. Decoupling damping from spring rate helps you dial in performance. Integrated designs can work fine, but be sure to build in lead time to get more than one set in order to buy an iteration or two.

Canopy, windscreen, moving body parts in general

* The easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.
* There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.
* Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.

The easiest way to get a clear windscreen is to design it to be a simple curve and just bending a laser-cut flat piece of plastic into an inset. This worked pretty well on Apogee, and we weren't even all that competent.

There are windscreen bonding agents that have a little bit of give to them. They're highly tolerant of heat, UV, and water while also soaking up some vibration. They're designed not to be too strong, so you can peel out windshields when the need arises. Used on real cars, usually black or white.

Making good seams on things that move frequently and which you are not allowed to tape is miserable. Try to minimize that. Non-hinged, tape-able seams are marginally annoying, but not so bad.

Battery

* I didn't parse what 'affirmative' and 'negative' mean.
* Why is BMS volume increasing?
* DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.

I didn't parse what 'affirmative' and 'negative' mean.

Why is BMS volume increasing?

DC/DC redundancy seems unnecessary. There has been no DC/DC failure in a Stanford car in any of the last six races, nor in any test drives. So why pay the complexity penalty? I firmly believe that more-complicated designs fail more often than simple ones. Delete as many parts as possible and make sure that what remains is well-designed and robust.

-Sasha

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1ediaamE5WSTwBmogfHXyhPdRYqryjlj7#list)
