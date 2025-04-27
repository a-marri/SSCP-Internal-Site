# luminos-strategy-planning

## SSCP - Luminos: Strategy Planning

## Luminos: Strategy Planning

A Discussion on the Optimality of Constant Speed

The simplest strategy method is choosing a constant speed - something which makes sense for a perfectly efficient vehicle on flat road with constant insolation. It remains to be seen whether or not our vehicle will benefit from a non-constant speed or if the imperfections are lost in the noise of the data from the car, but here is a discussion we had via email. Attached is the Aurora paper mentioned below.

About the optimality of constant speed.

8 messages

To: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

Hey all,&#x20;

I think I need to disabuse people on the team from the notion that constant speed is optimal.

Driving at a constant speed is only optimal under the following assumptions: (in decreasing level of importance)

* Insolation does not depend on time or location.
* The road is perfectly flat.
* The battery pack is an ideal energy storage device (no losses).
* The array's efficiency does not depend on temperature or vehicle velocity.
* Regenerative breaking is perfactly efficient at recapturing energy.

If you are interested in a rigorous derivation of the effects of these assumptions, please take a look at the attached Aurora paper.

Since these assumptions are roughly true to a first order approximation, previously, we have been simply choosing a constant speed. However, we know that these assumptions are all false, and constant speed is not optimal.&#x20;

This is the reason Jason and I have been working on discarding some of these unrealistic assumptions. We have been working with Stephen Boyd, and one of his grad students for the past few months. We now know that we can use convex optimization for this problem.  We already have a speed optimizer roughly running and Jason just incorporated realtime weather forecasts. I'm still working on building in the constraints for the control stops. (waiting for control stop locations from wesley) But the point it, the output of this optimization program will definitely be a more energy efficient velocity profile than a constant speed profile

Still, our optimizer still doesn't discarded all of the assumptions (namely the last 2). Perhaps those two assumptions will cancel each other out. But anyway, our output is still ultimately just a guideline for how fast to go.

Paul

Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Thu, Aug 8, 2013 at 10:28 AM

optimal\_energy\_management\_for\_solar\_powered\_cars.pdf

2839K

Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Thu, Aug 8, 2013 at 10:41 AM

To: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

Oh and since weather forecasts are never that accurate, during the race, we will need to repeatedly rerun the optimization as new weather information becomes available.

\[Quoted text hidden]

To: Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Cc: Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

Thanks for the email Paul - that all makes a lot of sense. I have a few questions, after reading through Aurora's paper:

-Do you know how much the peak array power should vary from Darwin to Adelaide?&#x20;

-I understand that there is energy wasted in storing array power (either from the middle of the day, or from changing latitude), but what amount are we talking about?

-Can you quantify the energy gain of non-constant speed? Or, if our models are wrong, quantify the potential energy loss of using the optimizer? (This same question can be asked of constant speed strategy)

-When I ran the route with a constant speed, I only saw one instance (maybe a few tens of km?) where SOC was increasing, leading me to think that we rarely store array power while driving. Do you think the route has a significant enough amount of hills that we actually lose power by trying to store energy going downhill?

-In order to understand how inefficient our batteries are, how can I help? I have lots of data on the cells across current, voltage, and temperature. I could pretty easily find out how much energy is lost in a full charge-discharge cycle (versus discharge rate), if that helps.

Other stuff:

(Page 164: note that the winning team in 1999 was challenged by the problem of small bladders. Perhaps we can find out what their solution was)

We probably didn't think about this because there was no noticeable wind near Chico - how can we get an idea of the wind in Australia? Maybe have scout stop periodically and set up the Weatherhawk? It does not work very well on top of vehicles.

Max

\[Quoted text hidden]

To: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com)

Cc: Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

1. According to historic weather data, the average peak insolation in Oct. in Darwin is about 1600 kJ/m^2, in Adelaide is about 1400 kJ/m^2. Keep in mind we have 6 m^2 of panels, so this difference is not insignificant.
2. Energy waste from storage is from the battery... I'm not super familiar with this, but I think since we are using brand new batteries, this should not be too bad? Max, do you have some ohmic loss models? maybe I can look into incorporating this.
3. I will be able to quantify the energy gain hopefully by next week. But also, from the looks of it, the optimal velocity profile we output might be pertty close to constant speed after all...&#x20;
4. I didn't know, so you might be right. I'll be able to give you a more informed answer when I get everything to run.
5. Yes, if you could find out how much energy each charge-discharge loses, that would be very informative.
6. Wind is really random, and generally averages out, so I wasn't planning on including the realtime wind info into my program. But we will be monitoring wind from the forecasts (and of course the weatherhawk on our roof) to see if there is a strong prevailing wind. Which will then be factored into our calculations manually. &#x20;

\[Quoted text hidden]

To: Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Cc: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

I'll note that we have two Weatherhawks, so we can put one on chase. Scout can take one further ahead down the race course. This presumes both currently work.&#x20;

Paul, did you try both Weatherhawks when you set up the one?

-Wesley

\--&#x20;

T. Wesley Ford

+1-650-387-6374

[+1-650-387-6374](tel:%2B1-650-387-6374)

PO Box 14243

Stanford, CA 94309

\[Quoted text hidden]

To: "T. Wesley Ford" [twsford@gmail.com](mailto:twsford@gmail.com)

Cc: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

I just randomly took one and set it up, i don't think the other one would be any different.

\[Quoted text hidden]

To: Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Cc: Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

Unless we broke it. Do you mind checking the other one one evening?

They weren't packaged very carefully last time.

T. Wesley Ford

(650) 387-6374

[(650) 387-6374](tel:%28650%29%20387-6374)

PO Box 14243

Stanford, CA 94309&#x20;

(sent from my iPhone)

\[Quoted text hidden]

To: "T. Wesley Ford" [twsford@gmail.com](mailto:twsford@gmail.com)

Cc: Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu), Jason Jong [jjong@stanford.edu](mailto:jjong@stanford.edu), Theodore Wesley Ford [twford@stanford.edu](mailto:twford@stanford.edu), Gregory Hall [hall.gregory10@gmail.com](mailto:hall.gregory10@gmail.com), Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu)

Hopefully this gives you an idea of how much energy is lost in a full charge/discharge cycle of the cells - I am calculating "loss" as the difference in energy from charging and discharging between 4.2V and 2.5V, divided by the nominal energy in the cell (3.35 Ah \* 3.6V). The current is per-cell, so multiply by 16 for total battery current.

Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com)

Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

T. Wesley Ford [twsford@gmail.com](mailto:twsford@gmail.com)

T. Wesley Ford [twsford@gmail.com](mailto:twsford@gmail.com)

Paul Chen [pochuan@stanford.edu](mailto:pochuan@stanford.edu)

Max Praglin [mpraglin@gmail.com](mailto:mpraglin@gmail.com)

Thu, Aug 8, 2013 at 9:02 PM

Thu, Aug 8, 2013 at 12:24 PM

Thu, Aug 8, 2013 at 5:55 PM

Thu, Aug 8, 2013 at 9:43 PM

Thu, Aug 8, 2013 at 5:45 PM

Fri, Aug 9, 2013 at 1:43 PM

Below are some VERY early thoughts on strategy. They were not carried over into the race strategy for Luminos

* Drag test (drag the solar car behind a trailer while measuring tension on the ropeCoast down test (Roll the solar car down a slope on a flat surface until it stops. Measure velocity and distance)
* Drag test (drag the solar car behind a trailer while measuring tension on the rope
* Coast down test (Roll the solar car down a slope on a flat surface until it stops. Measure velocity and distance)
* Drag test (drag the solar car behind a trailer while measuring tension on the rope
* Coast down test (Roll the solar car down a slope on a flat surface until it stops. Measure velocity and distance)

Drag test (drag the solar car behind a trailer while measuring tension on the rope

Coast down test (Roll the solar car down a slope on a flat surface until it stops. Measure velocity and distance)

http://www.iwilltry.org/b/how-to-measure-the-drag-coefficient-of-your-car/

[http://www.iwilltry.org/b/how-to-measure-the-drag-coefficient-of-your-car/](http://www.iwilltry.org/b/how-to-measure-the-drag-coefficient-of-your-car/)

Highest level:

Power production - power consumption = coulombs

> > then determine optimal speed based off of Power Avail - losses to terrain, losses from weather, wind, tires, etc.

Power production(time, location, weather, terrain, temperature, MPPT eff) {

&#x20;   Insolation(time, location, terrain, weather, temp)

return power production

}

5/12/12: matlab power\_produced(filename, temperature)

> insolation measurement based off of weatherzone data

> pv\_efficiency given by a temperature-dependent standard input

(**still need a way to measure/calculate input temperatures**)

> dynamic prompting for time/dates

> \*\* still no response to transient weather dependency (ex: cloud cover)

\*\*array temperatures: ambient temp, extra heating, wind cooling

Power consumption(speed, terrain, wind, tire, motor ) {

powercurve(speed)

potentialenergy(terrain)

aerodrag(wind)

rollingresistance(tire)

return consumption

}

5/12/12: matlab poweratspeed(speed)

> returns expected power consumption based off of WSC11 data curve (Excel 2nd order polynomial fit)

action items:

get terrain data, insolation data, route data.

> distance\_between(start\_lat, start\_long, end\_lat, end\_long) for route simulation

Test array eff dependency on temp

> 0.32% gain/loss in efficiency per degC off of STD (25degC)

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1RTJqsfurj-whB6JYLanMzLa-sLzeJWEk#list)
