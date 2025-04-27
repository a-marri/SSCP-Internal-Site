# sunwhale-alumni-pdr-71214

## SSCP - Sunwhale Alumni PDR 7/12/14

## Sunwhale Alumni PDR 7/12/14

Presentation:

#### Embedded Content

Embedded content: [Embedded Content](sunwhale-alumni-pdr-71214.md)

Alumni in attendance: Ben Stabler, Sam D'Amico, Adem Rudin (Minnesota), Rachel Fenichel, Ian Girard, John Shen, Dr. Toby, Greg Hall, Sasha Z, Nathan HS, Wesley Ford, Nathan Golshan, Paul Karplus (stopped by at end)

\= 3 boxes of donuts

Current members in attendance: 20+

Presentation Comments

ASC 2016: we would need to think about designing a car for both races. If we don't think about it now, we are saying 'no' to ASC2016. Rules will come out in October, but are expected to be similar to ASC2014 (with 4 wheels)

Goal of 10% speed improvement: should this be a net power improvement rather than net speed improvement?

We need WSC to state clearly how the bounding box is referenced to the ground. What about on a hill?

Make cardboard radio box mock-up to keep around shop

If we are the first team to bring up GaAs vs Silicon area tradeoff, we might get a benefit.

Be ready to vibe test the concentrators

Aero schedule: Sam pointed out that we had a good amount of time when the shells were layed up and just sitting there. Nathan: genesis of this schedule is that molds can be 6 months late and the car can still ship in time. It does have the benefit of giving us lots of testing time.

Adem: we should be churning out many many many designs before ever choosing a shape. Worried that we are laser-focusing on one design and haven't explored the design space. We are not iterating fast enough - we need faster iteration while we are choosing a style. Even if we just chose catamaran, there are a lot of ways to implement it. 20-25 iterations is not enough. We should just use a low-quality mesh and run it through Fluent quickly.&#x20;

Nathan: we need someone to make sure that the toolchain is always up and that we are always running through it.

Sam: could consider using the same injection molded parts and just removing a cell from each.

Nathan: how does door work? will there be aerodynamic features in the wheel wells? ARRAY STAND? Look up the guy at Tesla who did aero for wheels

NO REAR WHEEL STEERING - we can make the turning radius work without it.

Sam: is there a packaging issue with a 3-fairing design and leading-arm geometry? Aravind: no.

Ben and Nathan: some camber change is desired. The front leading arm suspension has to wrap around the wheel and will make the bounding box larger. Consider large moment of inertia, how we can make the suspensions similar but tuned properly.&#x20;

Nathan: we should double-check that the M12 pins can handle full current at 12V.&#x20;

Nathan: Max should talk to Google people about FMEA.&#x20;

Sasha: 12V electrical system would allow us to use an auxiliary battery so a DC-DC failure doesn't stop the car. Also recommends that we at least use a Digi Maxstream because it is lower power

Wesley: talk to Paul at Panasonic (in person, not via email) to see what cells we could legitimately get.&#x20;

John Shen: works at a battery startup now, find out if there are any other options

Let's talk with Matt Lambert or Chris ?? IN PERSON, privately, to find out what Sunpower can do with us

Sam: we should do a thermal simulation.&#x20;

Nathan: it's important to figure out who solders the array, because they've gotta do it right.

Greg: look into high-density tooling foam for a thermoforming plug. There was a company in Canada that was willing to do it out of high density tooling foam, but they have long lead times Ian: polished aluminum is the right way to do it. SLA then polished?&#x20;

Nathan: thermoforming design and direction needs to be included in the timeline and sent out with the molds. Also, ask Williams F1 about their paint stack-up, or what they did 2 years ago.

Sam: weight of composites could help us get the left/right weight balance correct

Nathan: see if we can get Virgin to sign a contract committing a car shipment for their sponsorship

Day before July 4 is a bad day.&#x20;

Rachel: need a battery ship date on there.

Ian: if all our improvement will come in Aero, we are sealing in that improvement early by shipping it in October. We should be giving ourselves more time if that's where we are making our improvements.&#x20;

Open Comments

Adem: there is very little analysis shown on how to deal with the bounding box. This is our one chance to make a huge gain in the design. If there is anything dubious about how we approach fitting within the rules, we need it in writing from the officials and published on the web and made aware to other teams

Is 12m^2 pointed at an incorrect angle better than 6m^2 pointed directly?

Nathan: we need to strongly weight the simplicity of a charging design. Maybe "movable" implies that we can lift the car, so it doesn't have to roll?

Adem: not a bad idea to place concentrators over the silicon array

Greg: ask Matt Lambert about concentrators.

Nathan: make the car structural and roll it on its side?

Greg: should we have a box of small cells around the car to capture vortices?

Ian: good job bringing up goals. Set out safety expectations so it doesn't come up later.

&#x20;   Our approach: solar cars are inherently dangerous, but&#x20;

Ben: concerned that there isn't any work into vehicle stability. Needs to be a #1 priority. Look more carefully at the weight balance spreadsheet. First, talk to Gerdes!!&#x20;

Nathan: try to copy Luminos' parameters like camber gain, etc. Safety: if we can't find drivers for the car, it's not safe enough. (Is this a standard of safety??)

Adem: look at historic weather for choosing crosswinds. Also, however safe the car is, human error on the road is the biggest source of danger.

Ian: maybe not relevant yet, but consider who would be taking spring quarter off. Greg and Wesley taking time off was hugely important.

Email Responses

Sasha: Some thoughts from the preliminary design review

Sorry I didn't stick around longer; I had a bad headache and really needed a nap. Some thoughts that came to mind that I didn't get a chance to share:

* I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirementsMaybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;
* I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirementsMaybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;
* I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.
* You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.
* I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.
* Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.
* Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).
* Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirements
* You can use much smaller relays, saving considerable weight and power.
* You can use fewer relays because the bus won't be considered "high voltage"
* You skip double-insulation requirements
* Maybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;
* I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirementsMaybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;
* I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.
* You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.
* I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.
* Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.
* Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).
* Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirements
* You can use much smaller relays, saving considerable weight and power.
* You can use fewer relays because the bus won't be considered "high voltage"
* You skip double-insulation requirements
* Maybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;

1. I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.
2. You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.
3. I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.
4. Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.
5. Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).
6. Maybe consider having a main bus of <=60 volts.You can use much smaller relays, saving considerable weight and power.You can use fewer relays because the bus won't be considered "high voltage"You skip double-insulation requirements
7. You can use much smaller relays, saving considerable weight and power.
8. You can use fewer relays because the bus won't be considered "high voltage"
9. You skip double-insulation requirements
10. Maybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;

I think it's great that y'all were organized enough to put this together. And while some flak was shot for incompleteness, I think it's a step beyond where previous teams have been. Good job.

You have what looks like a pretty slick aero simulation pipeline. I'd encourage continuing to develop both it and the people who use it to ensure that it's a sustainable resource both for the entirety of this cycle and for subsequent one. Agree that more iterations of hack concepts would be valuable for narrowing a wide problem space.

I'd be cautious about approaching both a catamaran car and solar concentration, especially given the array-standing rules. Seems maybe over-ambitious. Stanford's history is full of technical overreach, and the most successful teams have chosen to do the conservative thing everywhere and innovate on just one piece.

Personally I'd elect to refine the Luminos body shape and innovate on an integrated array stand and improve the battery pack insertion/removal/connection design. Leave the suspension parameters alone.

Send out the link to the site with the Cg estimates for a catamaran. At dinner a little bit of hack-math concluded it would be hard to achieve even 60/40 lateral balance. Also remember that Cg is important, but so is the distribution whenever turning (or accelerating in general).

Maybe consider having a main bus of <=60 volts.

1. You can use much smaller relays, saving considerable weight and power.
2. You can use fewer relays because the bus won't be considered "high voltage"
3. You skip double-insulation requirements

You can use much smaller relays, saving considerable weight and power.

[much smaller relays](http://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-k2w.pdf)

You can use fewer relays because the bus won't be considered "high voltage"

You skip double-insulation requirements

Maybe consider not having an isolated LV bus at all. Just send current-limited main pack voltage everywhere, assuming it's <=60 volts.&#x20;

* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.
* Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.
* Car turn-on becomes trivial and ditches secondary batteries.
* Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.
* Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.
* Car turn-on becomes trivial and ditches secondary batteries.
* Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.Car turn-on becomes trivial and ditches secondary batteries.Would require re-winding stators, but would reduce switching losses.
* No more worrying about DC/DC quiescent or dynamic loads.
* Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.
* Car turn-on becomes trivial and ditches secondary batteries.
* Would require re-winding stators, but would reduce switching losses.

1. No more worrying about DC/DC quiescent or dynamic loads.
2. Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.
3. Car turn-on becomes trivial and ditches secondary batteries.
4. Would require re-winding stators, but would reduce switching losses.

No more worrying about DC/DC quiescent or dynamic loads.

Not great selection of regulators, but enough to make this a workable solution. LTC363x series will be very handy.

Car turn-on becomes trivial and ditches secondary batteries.

Would require re-winding stators, but would reduce switching losses.

* There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.
* There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.
* There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.
* Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.
* I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.
* There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.
* There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.
* Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.
* I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.

1. There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.
2. Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.
3. I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.

There need to be a lot more composite test coupons and array encapsulation coupons. Not only do you get to figure out what stackups work well, you also refine a process before you're in a time-crunch to deploy it at vehicle-scale. I think the team could lose a lot of weight in the body and gain a lot of performance in the array if this is done early and often.

Go figure out how much temperature rise you actually see on cells both when stationary and when moving at different speeds. I volunteer to assist a current member in doing this. I have both a car and plenty of test equipment. You just need to supply some encapsulation stack coupons (with working - but of any goodness - cells) that you're willing to sacrifice.

I'm happy to mentor someone through a BMS spin. I've got some thoughts on how to improve integration and usability while reducing parts count and sticking to a monolithic architecture.

Adem: Agreed on #2 - I may have sounded overly negative in the meeting.  The process you're building sounds super cool and will be a major resource next time around as well; you just need some lower-fidelity, faster turnaround stuff to compliment it - especially in the early stages.

Ben: Vehicle dynamics on asymmetric cars

Hey all,

Following on from the design review today, I ran a couple simple simulations on a model that Alice Che and I built for Gerdes class.

Bear in mind that this model _doesn't include anything suspension related_ so it essentially assumes that you're on a perfect flat road, your suspension doesn't deflect at all, and you have no camber on the wheels.

The model also uses relatively sympathetic tires (based on what's on P1, which are lower pressure and wider so I believe they behave better in saturation than the ones on the solarcar).

I think there are also some bugs in the model in certain circumstances, but I believe what I have below holds.

I've used 60/40 weight distribution (L/R) and 48/52 (F/B). In reality I suspect the catamaran design would be less symmetric (L/R) and you will probably have to be careful that your F/B distribution is equal on each side.

Under cornering:

ModelSimulator(@UnassistedModel, @STurn) => SymmetricSTurn.png

ModelSimulator(@UnassistedAsymmetricModel, @STurn) => AsymmetricSTurn.png

There is a slight difference in lateral velocity due to cornering, which isn't a huge surprise (you're going to be in slightly different places on the friction curve if you have an unusual weight distribution, hence slightly different tyre deflections and you slide a bit). More importantly, notice the lateral force on each tyre (bottom left/right graphs). In the symmetric car your lateral force is the same on each front tyre (as we would expect). On the asymmetric car it's different- around 33% higher! You aren't going to lose friction noticeably sooner because friction is roughly proportional to normal force (at least in this simple model)- but you are going to wear through the tyre faster!

Under braking:

ModelSimulator(@UnassistedModel, @Brake) => SymmetricBrake.png

ModelSimulator(@UnassistedAsymmetricModel, @Brake) => AsymmetricBrake.png

This is a hard brake, around 15-20% below what would lock the tyres. With the symmetric design this is fine, with the asymmetric design the brakes on the lighter side of the car lock. There's also a small moment on the vehicle. Presumably these problems could be solved by carefully balancing the brakes L/R and training the driver, but they are issues you would certainly need to address.

I've attached the matlab code so you guys can play around. Unfortunately this model doesn't address anything to do with the suspension, and I think that's where the issues would really be, so please do some more homework and think about what happens there.

Final thought- I heard mention of moving the motor to the rear wheel. If you do this, remember that it's somewhat analogous to increasing the preload on the rear suspension (larger unsprung mass -> larger inertia, which means that under compression there's more effective mass on the wheel), which means that under cornering you are more likely to put yourself in a position of oversteer (limit or otherwise), which means unstable. You can compensate for this to some degree by increased tension on the front and moving mass forward, but remember that it's due to unsprung mass so it's going to be changing all the time as you drive, so you'll want to test under different conditions to ensure that you've covered the edge conditions.

Cheers,

Ben
