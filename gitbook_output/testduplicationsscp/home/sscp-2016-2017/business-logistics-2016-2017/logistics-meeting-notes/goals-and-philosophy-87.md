# goals-and-philosophy-87

## SSCP - Goals and Philosophy 8/7

## Goals and Philosophy 8/7

* Aero:29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are betterRachel to do vehicle dynamics simulationsCrosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and ArctanWe need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from MichelinNeed the center of pressure from CFD -- center of gravity can be calculated from math\*\* can likely figure out cross wind force and torque during fine tuningWe know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhereNote: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* 29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are betterRachel to do vehicle dynamics simulationsCrosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and ArctanWe need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from MichelinNeed the center of pressure from CFD -- center of gravity can be calculated from math\*\* can likely figure out cross wind force and torque during fine tuningWe know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhereNote: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* 29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are better
* Calculated by Gawan with the strategy software
* Factors in all of the aero stuff to come up with drag number
* Could be slightly higher for same performance if other factors (crosswinds) are better
* Rachel to do vehicle dynamics simulations
* Crosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* Torque encompasses force, but both should be considered
* Staying in lane vs staying straight (not rotating)
* Maybe we should do something like newtons per kilogram?
* 450 for a lighter car would be bad
* There are things we can do to minimize crosswind affects -- ie crease on the side like Nuon
* Plan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* We need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from Michelin
* Have rolling resistance from Michelin
* Need the center of pressure from CFD -- center of gravity can be calculated from math
* \*\* can likely figure out cross wind force and torque during fine tuning
* We know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhere
* Note: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* Last cycle there was a lot of talk about not making it so easy to be a driver
* Should send our drivers to driving school and teach them about the car's dynamics
* We have about 4 people already who are smallish enough and could get the training necessary
* Array:GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%
* Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)
* Arctan had a loss of 1.8% (absolute)
* Gocharmann claims 0% loss
* Chuzel claims .3% gain (relative)
* If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* Plan = buy one, make a backup
* May go with Trina, depending on testing
* Let's evaluate at the end of the year
* Mechanical:Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the roadWeight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goalGeneral bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the roadWeight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goalGeneral bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?
* Historically 3-wheel cars needed to be front biased
* Luminos things were weird because the spreadsheet was bad
* There's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* Should aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* 50-50 means tail wants to slide out
* \*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballast
* Why did Arctan weigh so much?
* Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the road
* Understeer -- standard cars on the road
* K = Wf/Cf - Wr/ Cr
* Want the car to not oscillate uncontrollably on the road
* Weight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goal
* Biggest problem is yawing during braking
* Make sure the car doesn't yaw a bunchSoft goal
* Soft goal
* General bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?
* Different random springs on different corners
* Making steering column and suspension as light as possible -- titanium? Carbon fiber?
* WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Very hard to control
* Never really had a goal -- just let the components rule
* Aim for Luminos -- hard because their suspension was so light, but also a smaller car
* Composites:Chassis should fit in the aerobodyBeing lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighterGawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structuralBottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSimMinimal Bondo!
* Chassis should fit in the aerobodyBeing lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighterGawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structuralBottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSimMinimal Bondo!
* Chassis should fit in the aerobody
* Being lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighter
* This cycle we have better materials, but won't necessarily be lighter
* More likely for the car to end up stiffer than lighter
* Gawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structural
* It's ok if things can move a little if they aren't structural
* Bottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSim
* Ply cutting to prevent this
* Using ANSYS and FiberSim
* Minimal Bondo!
* Electrical:Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)
* Could include MPPTs, motor controllers
* Could run on the Dyno
* End of winter quarter (with code)
* Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)
* Drop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio
* Most of the drop comes from NRF radio
* 21W calculated (needs Tritium and MPPTs)
* Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* 5.4kWh from 18650G
* Mechanical packaging has not been considered yet -- aiming for weight decrease
* Code:High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* Regen going out
* Throttle going out
* Top of pack behaviorLast time was a safety feature that made the car less safe...
* Last time was a safety feature that made the car less safe...
* Communication going out
* Cruise control needs to work
* BMS should work always
* Strategy/Telemetry:SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will beAbility to detect failuresNumber detected over number of failures
* SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will beAbility to detect failuresNumber detected over number of failures
* SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Should not be like Arctan -- 28% is bad
* Set to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Don't know where end of timing will be
* Ability to detect failuresNumber detected over number of failures
* Number detected over number of failures
* Team goal: Change of race speedGawan: if weather conditions are constant, speed is a good metricAero drag number goal takes into account better array and lighter car to achieve 0% speed
* Gawan: if weather conditions are constant, speed is a good metricAero drag number goal takes into account better array and lighter car to achieve 0% speed
* Gawan: if weather conditions are constant, speed is a good metric
* Aero drag number goal takes into account better array and lighter car to achieve 0% speed

Aero:

* 29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are betterRachel to do vehicle dynamics simulationsCrosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and ArctanWe need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from MichelinNeed the center of pressure from CFD -- center of gravity can be calculated from math\*\* can likely figure out cross wind force and torque during fine tuningWe know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhereNote: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* 29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are better
* Calculated by Gawan with the strategy software
* Factors in all of the aero stuff to come up with drag number
* Could be slightly higher for same performance if other factors (crosswinds) are better
* Rachel to do vehicle dynamics simulations
* Crosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* Torque encompasses force, but both should be considered
* Staying in lane vs staying straight (not rotating)
* Maybe we should do something like newtons per kilogram?
* 450 for a lighter car would be bad
* There are things we can do to minimize crosswind affects -- ie crease on the side like Nuon
* Plan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* We need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from Michelin
* Have rolling resistance from Michelin
* Need the center of pressure from CFD -- center of gravity can be calculated from math
* \*\* can likely figure out cross wind force and torque during fine tuning
* We know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhere
* Note: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* Last cycle there was a lot of talk about not making it so easy to be a driver
* Should send our drivers to driving school and teach them about the car's dynamics
* We have about 4 people already who are smallish enough and could get the training necessary
* 29N would lead to 0% change (with reduction in array size)Calculated by Gawan with the strategy softwareFactors in all of the aero stuff to come up with drag numberCould be slightly higher for same performance if other factors (crosswinds) are better
* Calculated by Gawan with the strategy software
* Factors in all of the aero stuff to come up with drag number
* Could be slightly higher for same performance if other factors (crosswinds) are better
* Rachel to do vehicle dynamics simulations
* Crosswind torque is a better metric than force for analyzing crosswind performanceTorque encompasses force, but both should be consideredStaying in lane vs staying straight (not rotating)Maybe we should do something like newtons per kilogram?450 for a lighter car would be badThere are things we can do to minimize crosswind affects -- ie crease on the side like NuonPlan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* Torque encompasses force, but both should be considered
* Staying in lane vs staying straight (not rotating)
* Maybe we should do something like newtons per kilogram?
* 450 for a lighter car would be bad
* There are things we can do to minimize crosswind affects -- ie crease on the side like Nuon
* Plan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan
* We need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)Have rolling resistance from Michelin
* Have rolling resistance from Michelin
* Need the center of pressure from CFD -- center of gravity can be calculated from math
* \*\* can likely figure out cross wind force and torque during fine tuning
* We know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhere
* Note: we are making driver model smaller and smaller which restricts our driver poolLast cycle there was a lot of talk about not making it so easy to be a driverShould send our drivers to driving school and teach them about the car's dynamicsWe have about 4 people already who are smallish enough and could get the training necessary
* Last cycle there was a lot of talk about not making it so easy to be a driver
* Should send our drivers to driving school and teach them about the car's dynamics
* We have about 4 people already who are smallish enough and could get the training necessary

29N would lead to 0% change (with reduction in array size)

* Calculated by Gawan with the strategy software
* Factors in all of the aero stuff to come up with drag number
* Could be slightly higher for same performance if other factors (crosswinds) are better

Calculated by Gawan with the strategy software

Factors in all of the aero stuff to come up with drag number

Could be slightly higher for same performance if other factors (crosswinds) are better

Rachel to do vehicle dynamics simulations

Crosswind torque is a better metric than force for analyzing crosswind performance

* Torque encompasses force, but both should be considered
* Staying in lane vs staying straight (not rotating)
* Maybe we should do something like newtons per kilogram?
* 450 for a lighter car would be bad
* There are things we can do to minimize crosswind affects -- ie crease on the side like Nuon
* Plan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan

Torque encompasses force, but both should be considered

Staying in lane vs staying straight (not rotating)

Maybe we should do something like newtons per kilogram?

450 for a lighter car would be bad

There are things we can do to minimize crosswind affects -- ie crease on the side like Nuon

Plan of action: weighing Arctan, CFD to get CP, Rachel to calculate torque -- want numbers for Luminos and Arctan

We need to construct a simulation to see how much side force and tire scrub decrease performance (Crow's Landing)

* Have rolling resistance from Michelin

Have rolling resistance from Michelin

Need the center of pressure from CFD -- center of gravity can be calculated from math

\*\* can likely figure out cross wind force and torque during fine tuning

We know that the tires were "true", but we still saw a lot of tire shavings -- had to be coming from somewhere

Note: we are making driver model smaller and smaller which restricts our driver pool

* Last cycle there was a lot of talk about not making it so easy to be a driver
* Should send our drivers to driving school and teach them about the car's dynamics
* We have about 4 people already who are smallish enough and could get the training necessary

Last cycle there was a lot of talk about not making it so easy to be a driver

Should send our drivers to driving school and teach them about the car's dynamics

We have about 4 people already who are smallish enough and could get the training necessary

Array:

* GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%
* Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)
* Arctan had a loss of 1.8% (absolute)
* Gocharmann claims 0% loss
* Chuzel claims .3% gain (relative)
* If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* Plan = buy one, make a backup
* May go with Trina, depending on testing
* Let's evaluate at the end of the year
* GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%
* Goal is to have 24% after encapsulationArctan had a loss of 1.8% (absolute)Gocharmann claims 0% lossChuzel claims .3% gain (relative)
* Arctan had a loss of 1.8% (absolute)
* Gocharmann claims 0% loss
* Chuzel claims .3% gain (relative)
* If we fall short, when do we decide to buy from Gochermann?Plan = buy one, make a backupMay go with Trina, depending on testingLet's evaluate at the end of the year
* Plan = buy one, make a backup
* May go with Trina, depending on testing
* Let's evaluate at the end of the year

GaAs vs Si: going to go with 24.3% SunPower -- final result from Alta was about 23.4%

Goal is to have 24% after encapsulation

* Arctan had a loss of 1.8% (absolute)
* Gocharmann claims 0% loss
* Chuzel claims .3% gain (relative)

Arctan had a loss of 1.8% (absolute)

Gocharmann claims 0% loss

Chuzel claims .3% gain (relative)

If we fall short, when do we decide to buy from Gochermann?

* Plan = buy one, make a backup
* May go with Trina, depending on testing
* Let's evaluate at the end of the year

Plan = buy one, make a backup

May go with Trina, depending on testing

Let's evaluate at the end of the year

Mechanical:

* Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the roadWeight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goalGeneral bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?
* Historically 3-wheel cars needed to be front biased
* Luminos things were weird because the spreadsheet was bad
* There's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* Should aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* 50-50 means tail wants to slide out
* \*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballast
* Why did Arctan weigh so much?
* Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the road
* Understeer -- standard cars on the road
* K = Wf/Cf - Wr/ Cr
* Want the car to not oscillate uncontrollably on the road
* Weight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goal
* Biggest problem is yawing during braking
* Make sure the car doesn't yaw a bunchSoft goal
* Soft goal
* General bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?
* Different random springs on different corners
* Making steering column and suspension as light as possible -- titanium? Carbon fiber?
* WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Very hard to control
* Never really had a goal -- just let the components rule
* Aim for Luminos -- hard because their suspension was so light, but also a smaller car
* Weight distribution, front-rear:Historically 3-wheel cars needed to be front biasedLuminos things were weird because the spreadsheet was badThere's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballastWhy did Arctan weigh so much?
* Historically 3-wheel cars needed to be front biased
* Luminos things were weird because the spreadsheet was bad
* There's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* Should aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* 50-50 means tail wants to slide out
* \*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballast
* Why did Arctan weigh so much?
* Primer:Understeer -- standard cars on the roadK = Wf/Cf - Wr/ CrWant the car to not oscillate uncontrollably on the road
* Understeer -- standard cars on the road
* K = Wf/Cf - Wr/ Cr
* Want the car to not oscillate uncontrollably on the road
* Weight distribution, right-left:Biggest problem is yawing during brakingMake sure the car doesn't yaw a bunchSoft goal
* Biggest problem is yawing during braking
* Make sure the car doesn't yaw a bunchSoft goal
* Soft goal
* General bad practice things with Arctan:Different random springs on different cornersMaking steering column and suspension as light as possible -- titanium? Carbon fiber?
* Different random springs on different corners
* Making steering column and suspension as light as possible -- titanium? Carbon fiber?
* WeightVery hard to controlNever really had a goal -- just let the components ruleAim for Luminos -- hard because their suspension was so light, but also a smaller car
* Very hard to control
* Never really had a goal -- just let the components rule
* Aim for Luminos -- hard because their suspension was so light, but also a smaller car

Weight distribution, front-rear:

* Historically 3-wheel cars needed to be front biased
* Luminos things were weird because the spreadsheet was bad
* There's always errorShould aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* Should aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* 50-50 means tail wants to slide out
* \*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballast
* Why did Arctan weigh so much?

Historically 3-wheel cars needed to be front biased

Luminos things were weird because the spreadsheet was bad

There's always error

* Should aim for between 55-45 and 60-40 (don't want 50-50)50-50 means tail wants to slide out
* 50-50 means tail wants to slide out

Should aim for between 55-45 and 60-40 (don't want 50-50)

* 50-50 means tail wants to slide out

50-50 means tail wants to slide out

\*\* should think about this ahead of time -- can solve with clever mechanical packaging, but if we fail to do that we will need to ballast

Why did Arctan weigh so much?

Primer:

* Understeer -- standard cars on the road
* K = Wf/Cf - Wr/ Cr
* Want the car to not oscillate uncontrollably on the road

Understeer -- standard cars on the road

K = Wf/Cf - Wr/ Cr

Want the car to not oscillate uncontrollably on the road

Weight distribution, right-left:

* Biggest problem is yawing during braking
* Make sure the car doesn't yaw a bunchSoft goal
* Soft goal

Biggest problem is yawing during braking

Make sure the car doesn't yaw a bunch

* Soft goal

Soft goal

General bad practice things with Arctan:

* Different random springs on different corners
* Making steering column and suspension as light as possible -- titanium? Carbon fiber?

Different random springs on different corners

Making steering column and suspension as light as possible -- titanium? Carbon fiber?

Weight

* Very hard to control
* Never really had a goal -- just let the components rule
* Aim for Luminos -- hard because their suspension was so light, but also a smaller car

Very hard to control

Never really had a goal -- just let the components rule

Aim for Luminos -- hard because their suspension was so light, but also a smaller car

Composites:

* Chassis should fit in the aerobodyBeing lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighterGawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structuralBottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSimMinimal Bondo!
* Chassis should fit in the aerobody
* Being lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighter
* This cycle we have better materials, but won't necessarily be lighter
* More likely for the car to end up stiffer than lighter
* Gawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structural
* It's ok if things can move a little if they aren't structural
* Bottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSim
* Ply cutting to prevent this
* Using ANSYS and FiberSim
* Minimal Bondo!
* Chassis should fit in the aerobody
* Being lighter is achievable because smaller car, but otherwise can't be that much lighterThis cycle we have better materials, but won't necessarily be lighterMore likely for the car to end up stiffer than lighter
* This cycle we have better materials, but won't necessarily be lighter
* More likely for the car to end up stiffer than lighter
* Gawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for thatIt's ok if things can move a little if they aren't structural
* It's ok if things can move a little if they aren't structural
* Bottom shell can be done a lot better (haphazard)Ply cutting to prevent thisUsing ANSYS and FiberSim
* Ply cutting to prevent this
* Using ANSYS and FiberSim
* Minimal Bondo!

Chassis should fit in the aerobody

Being lighter is achievable because smaller car, but otherwise can't be that much lighter

* This cycle we have better materials, but won't necessarily be lighter
* More likely for the car to end up stiffer than lighter

This cycle we have better materials, but won't necessarily be lighter

More likely for the car to end up stiffer than lighter

Gawan: a few kg = a few minutes -- don't sacrifice anything for stability/strength for that

* It's ok if things can move a little if they aren't structural

It's ok if things can move a little if they aren't structural

Bottom shell can be done a lot better (haphazard)

* Ply cutting to prevent this
* Using ANSYS and FiberSim

Ply cutting to prevent this

Using ANSYS and FiberSim

Minimal Bondo!

Electrical:

* Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)
* Could include MPPTs, motor controllers
* Could run on the Dyno
* End of winter quarter (with code)
* Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)
* Drop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio
* Most of the drop comes from NRF radio
* 21W calculated (needs Tritium and MPPTs)
* Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* 5.4kWh from 18650G
* Mechanical packaging has not been considered yet -- aiming for weight decrease
* Car on a bench -- more elaborate and earlierCould include MPPTs, motor controllersCould run on the DynoEnd of winter quarter (with code)
* Could include MPPTs, motor controllers
* Could run on the Dyno
* End of winter quarter (with code)
* Quiescent drawDrop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio21W calculated (needs Tritium and MPPTs)
* Drop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio
* Most of the drop comes from NRF radio
* 21W calculated (needs Tritium and MPPTs)
* Battery pack capacity:5.4kWh from 18650GMechanical packaging has not been considered yet -- aiming for weight decrease
* 5.4kWh from 18650G
* Mechanical packaging has not been considered yet -- aiming for weight decrease

Car on a bench -- more elaborate and earlier

* Could include MPPTs, motor controllers
* Could run on the Dyno
* End of winter quarter (with code)

Could include MPPTs, motor controllers

Could run on the Dyno

End of winter quarter (with code)

Quiescent draw

* Drop to 25W (found through calculating draw of everything as of now)Most of the drop comes from NRF radio
* Most of the drop comes from NRF radio
* 21W calculated (needs Tritium and MPPTs)

Drop to 25W (found through calculating draw of everything as of now)

* Most of the drop comes from NRF radio

Most of the drop comes from NRF radio

21W calculated (needs Tritium and MPPTs)

Battery pack capacity:

* 5.4kWh from 18650G
* Mechanical packaging has not been considered yet -- aiming for weight decrease

5.4kWh from 18650G

Mechanical packaging has not been considered yet -- aiming for weight decrease

Code:

* High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* Regen going out
* Throttle going out
* Top of pack behaviorLast time was a safety feature that made the car less safe...
* Last time was a safety feature that made the car less safe...
* Communication going out
* Cruise control needs to work
* BMS should work always
* High priority (as opposed to low priority) bugsRegen going outThrottle going outTop of pack behaviorLast time was a safety feature that made the car less safe...Communication going outCruise control needs to workBMS should work always
* Regen going out
* Throttle going out
* Top of pack behaviorLast time was a safety feature that made the car less safe...
* Last time was a safety feature that made the car less safe...
* Communication going out
* Cruise control needs to work
* BMS should work always

High priority (as opposed to low priority) bugs

* Regen going out
* Throttle going out
* Top of pack behaviorLast time was a safety feature that made the car less safe...
* Last time was a safety feature that made the car less safe...
* Communication going out
* Cruise control needs to work
* BMS should work always

Regen going out

Throttle going out

Top of pack behavior

* Last time was a safety feature that made the car less safe...

Last time was a safety feature that made the car less safe...

Communication going out

Cruise control needs to work

BMS should work always

Strategy/Telemetry:

* SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will beAbility to detect failuresNumber detected over number of failures
* SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Should not be like Arctan -- 28% is bad
* Set to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Don't know where end of timing will be
* Ability to detect failuresNumber detected over number of failures
* Number detected over number of failures
* SOC at end of timingShould not be like Arctan -- 28% is badSet to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Should not be like Arctan -- 28% is bad
* Set to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Don't know where end of timing will be
* Ability to detect failuresNumber detected over number of failures
* Number detected over number of failures

SOC at end of timing

* Should not be like Arctan -- 28% is bad
* Set to 6-8% so that with no array power at all, we could still get from end of timing to finish lineDon't know where end of timing will be
* Don't know where end of timing will be

Should not be like Arctan -- 28% is bad

Set to 6-8% so that with no array power at all, we could still get from end of timing to finish line

* Don't know where end of timing will be

Don't know where end of timing will be

Ability to detect failures

* Number detected over number of failures

Number detected over number of failures

Team goal: Change of race speed

* Gawan: if weather conditions are constant, speed is a good metricAero drag number goal takes into account better array and lighter car to achieve 0% speed
* Gawan: if weather conditions are constant, speed is a good metric
* Aero drag number goal takes into account better array and lighter car to achieve 0% speed
* Gawan: if weather conditions are constant, speed is a good metric
* Aero drag number goal takes into account better array and lighter car to achieve 0% speed

Gawan: if weather conditions are constant, speed is a good metric

Aero drag number goal takes into account better array and lighter car to achieve 0% speed

Philosophy/Goals

* Alex: Having a car that we can get to cross the finish line is super important -- no point of racing if we're just going to crashRachel: new members don't always appreciate this -- they wonder, "why aren't we trying to just go really fast??"Kelsey: remember, our best placing car in recent history was Luminos (not aggressive)Jason: helpful to remind people that it's going to be their friends or themselves in the car -- how do they feel about the risks now?Reed: building up of levels of risk -- is Michigan has historically been ok with sketchy handling, they could get worseKelsey/Steph: remember that if Stanford thinks we're ignoring safety, it'll be much harder for us to work with the universityReed: it would be great to be able to tell Stanford at the end of the cycle "these are the ways our car is safer"Alex: if we need to compromise, should err on the side of reliability/safetyMax: We should always err on the side of safety.  The difficult part is how hard it is to quantify risks and returnsGawan: shouldn't be a comparison of risk vs return but whether we're ok with the risk at allRachel: driver training could be restructured to make it more effective -- not just uninformed hours and hours of driving timeBad that drivers don't know much about how Australia will differ until we get thereAlice Springs testing was too much and didn't get much out of itBrake testing should happen at Crow's Landing, not Thunder HillAlex: Are we going to have a separate topshell?Test array and race arrayWinning vs Learning:Array is a good compromise -- both learning and bestIf it's a personnel issue, it's a little different -- could repurpose people in other areas maybeFast vs good:Max: that's the goal of putting numbers in that spreadsheetStill not 100% decidedEmailed in:Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise
* Alex: Having a car that we can get to cross the finish line is super important -- no point of racing if we're just going to crash
* Rachel: new members don't always appreciate this -- they wonder, "why aren't we trying to just go really fast??"
* Kelsey: remember, our best placing car in recent history was Luminos (not aggressive)
* Jason: helpful to remind people that it's going to be their friends or themselves in the car -- how do they feel about the risks now?
* Reed: building up of levels of risk -- is Michigan has historically been ok with sketchy handling, they could get worse
* Kelsey/Steph: remember that if Stanford thinks we're ignoring safety, it'll be much harder for us to work with the university
* Reed: it would be great to be able to tell Stanford at the end of the cycle "these are the ways our car is safer"
* Alex: if we need to compromise, should err on the side of reliability/safety
* Max: We should always err on the side of safety.  The difficult part is how hard it is to quantify risks and returns
* Gawan: shouldn't be a comparison of risk vs return but whether we're ok with the risk at all
* Rachel: driver training could be restructured to make it more effective -- not just uninformed hours and hours of driving timeBad that drivers don't know much about how Australia will differ until we get thereAlice Springs testing was too much and didn't get much out of itBrake testing should happen at Crow's Landing, not Thunder Hill
* Bad that drivers don't know much about how Australia will differ until we get there
* Alice Springs testing was too much and didn't get much out of it
* Brake testing should happen at Crow's Landing, not Thunder Hill
* Alex: Are we going to have a separate topshell?Test array and race array
* Test array and race array
* Winning vs Learning:Array is a good compromise -- both learning and bestIf it's a personnel issue, it's a little different -- could repurpose people in other areas maybe
* Array is a good compromise -- both learning and best
* If it's a personnel issue, it's a little different -- could repurpose people in other areas maybe
* Fast vs good:Max: that's the goal of putting numbers in that spreadsheetStill not 100% decided
* Max: that's the goal of putting numbers in that spreadsheet
* Still not 100% decided
* Emailed in:Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise
* Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.
* Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise
* Alex: Having a car that we can get to cross the finish line is super important -- no point of racing if we're just going to crash
* Rachel: new members don't always appreciate this -- they wonder, "why aren't we trying to just go really fast??"
* Kelsey: remember, our best placing car in recent history was Luminos (not aggressive)
* Jason: helpful to remind people that it's going to be their friends or themselves in the car -- how do they feel about the risks now?
* Reed: building up of levels of risk -- is Michigan has historically been ok with sketchy handling, they could get worse
* Kelsey/Steph: remember that if Stanford thinks we're ignoring safety, it'll be much harder for us to work with the university
* Reed: it would be great to be able to tell Stanford at the end of the cycle "these are the ways our car is safer"
* Alex: if we need to compromise, should err on the side of reliability/safety
* Max: We should always err on the side of safety.  The difficult part is how hard it is to quantify risks and returns
* Gawan: shouldn't be a comparison of risk vs return but whether we're ok with the risk at all
* Rachel: driver training could be restructured to make it more effective -- not just uninformed hours and hours of driving timeBad that drivers don't know much about how Australia will differ until we get thereAlice Springs testing was too much and didn't get much out of itBrake testing should happen at Crow's Landing, not Thunder Hill
* Bad that drivers don't know much about how Australia will differ until we get there
* Alice Springs testing was too much and didn't get much out of it
* Brake testing should happen at Crow's Landing, not Thunder Hill
* Alex: Are we going to have a separate topshell?Test array and race array
* Test array and race array
* Winning vs Learning:Array is a good compromise -- both learning and bestIf it's a personnel issue, it's a little different -- could repurpose people in other areas maybe
* Array is a good compromise -- both learning and best
* If it's a personnel issue, it's a little different -- could repurpose people in other areas maybe
* Fast vs good:Max: that's the goal of putting numbers in that spreadsheetStill not 100% decided
* Max: that's the goal of putting numbers in that spreadsheet
* Still not 100% decided
* Emailed in:Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise
* Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.
* Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise

Alex: Having a car that we can get to cross the finish line is super important -- no point of racing if we're just going to crash

Rachel: new members don't always appreciate this -- they wonder, "why aren't we trying to just go really fast??"

Kelsey: remember, our best placing car in recent history was Luminos (not aggressive)

Jason: helpful to remind people that it's going to be their friends or themselves in the car -- how do they feel about the risks now?

Reed: building up of levels of risk -- is Michigan has historically been ok with sketchy handling, they could get worse

Kelsey/Steph: remember that if Stanford thinks we're ignoring safety, it'll be much harder for us to work with the university

Reed: it would be great to be able to tell Stanford at the end of the cycle "these are the ways our car is safer"

Alex: if we need to compromise, should err on the side of reliability/safety

Max: We should always err on the side of safety.  The difficult part is how hard it is to quantify risks and returns

Gawan: shouldn't be a comparison of risk vs return but whether we're ok with the risk at all

Rachel: driver training could be restructured to make it more effective -- not just uninformed hours and hours of driving time

* Bad that drivers don't know much about how Australia will differ until we get there
* Alice Springs testing was too much and didn't get much out of it
* Brake testing should happen at Crow's Landing, not Thunder Hill

Bad that drivers don't know much about how Australia will differ until we get there

Alice Springs testing was too much and didn't get much out of it

Brake testing should happen at Crow's Landing, not Thunder Hill

Alex: Are we going to have a separate topshell?

* Test array and race array

Test array and race array

Winning vs Learning:

* Array is a good compromise -- both learning and best
* If it's a personnel issue, it's a little different -- could repurpose people in other areas maybe

Array is a good compromise -- both learning and best

If it's a personnel issue, it's a little different -- could repurpose people in other areas maybe

Fast vs good:

* Max: that's the goal of putting numbers in that spreadsheet
* Still not 100% decided

Max: that's the goal of putting numbers in that spreadsheet

Still not 100% decided

Emailed in:

* Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.
* Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise

Ashe: I want to be a driver, and I wouldn’t call myself risk averse by any means, but I don’t want to design a car that is so hard to drive that finishing safely is based on luck. I think the handling of the car should use Arctan as a baseline and have that be the very worst we can accept. If the car is unstable or very vulnerable to environmental affects, or if it successfully completed the race and then randomly crashed due to wind or something later, that wouldn’t be engineering I’d be proud of. I don’t want to win because we were just incredibly lucky.

Steph: At the end of the day, driver safety should be a priority.  Yes I think we should push the boundaries a bit to improve speed, but I think we should be pushing those boundaries in areas that will decrease safety the least.  Please correct me if I'm wrong, but we really want to do well not only to see our hard work pay off, but also to impress Stanford + sponsors so we can continue to get support in the future.  If anything were to happen to a driver, I think we would all quickly realize it wasn't worth it, as a friend could be seriously injured, and thinking from a colder perspective, we definitely would not be able to continue our project in the future.  I also think it's hard for some of the guys to think like this when there's no chance they'd be in the car.  Anyway: main point is that I think we can be really proud of pushing engineering boundaries in regions that will least affect safety and I am confident we will still do well, but there are some safety things we just can't compromise
