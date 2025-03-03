# SSCP - What Ifs (Hypothetical Design Tradeoffs)

# What Ifs (Hypothetical Design Tradeoffs)

This page contains a list of design tradeoffs and specific questions that they pose.  Please add questions.

As we determine the answers to these questions, we will add numbers and other details here.

Requires Simulation

Requires Math

Requires Testing

Done

In Progress

Array Normalization

How much power do we gain by normalizing at rest stops?

    - Best case scenario (mornings and evenings) / Worst case scenario (stops are mid-day)

    - Normalization gains vary a lot depending on time of day:

        - Beginning of day: 80-90% increase

        - Middle of day: near 0% increase

        - End of day: ~100% increase

    - Remember to take into account that much less power is being made at the beginning and end of the day.

How quickly would we need to set up and take down our array?

    - Time only starts after driver has set things up.

    - A rough average over the day is around 30 seconds.

Is motor-actuated normalization worth it?

    - How much power would a motor use?

    - No, it is not (topshell too heavy, motor too slow)

What time of day will we hit rest stops?

    - Roughly the same time of day as 2015, assuming same control stop locations

    - May need route guide to do this calculation again with 2015 rest stop locations.

Array, General

How much power does cooling make us?

GaAs vs Silicon

    - Are Alta or Sunpower cells better? -> Sunpower

    - How do we account for differences in encapsulation?

Are bypass diodes worth it?

        - Yes, in some modules with shading or higher curvature.

Does voltage of GaAs cells (closer to battery) make up for lower efficiency?

    - How many W are saved in MPPT conversion?

How do cutouts on the back shell affect heat of cells?

Aero

How much does curvature affect the array?

    - How would Luminos power change if it were flat?

    - Max P. did some analysis on this Arctan cycle, using command-line Shellpower and many different aerobody models. (find link)

Mechanicaldrive

    - How much does weight affect power consumptions (factoring in non-conservative Frr)

Batteries

Li-Ion

    - How much time does 18650G vs 18650B save us?

        - 18650B: 243 Wh/kg = 4.86 kWh pack

        - 18650G: 256 Wh/kg = 5.12 kWh pack

        - That's a 0.26 kWh difference ~= 6W ~= 4 minutes

    - How much do cells degrade over time?

        - Ian mentioned that time is a big factor in performance, maybe bigger than discharge cycles.

        - We will characterize a cell when we receive it and another as close to the race as possible.

Li-S

    - How much time do they gain us?

        - With current estimates (240-300 Wh/kg), they won't gain us any time.

Li-Si

    - How much time would these gain us?

        - Not feasible

Code 

Will narrowing cruise control speed variance save power?

    - How much?

    - What about adapting to inclines?

Composites

How many watts do we gain per subtracted kg?

    - Without refined Crr calculations, .473

Motors

What is our projected cruising speed for a 4m^2 array car?

    - With current aero estimates (~29N in October) it is around 85 kph

    - Do we need to modify the motors to be optimal at this speed?

        - No

    - Do we need to change battery pack voltage?

        - Yes, to avoid speed limiting. (nominal voltage increased to 125V)

[Gawan Fiore - gfiore@stanford.edu]

Last updated Oct 2, 2017

