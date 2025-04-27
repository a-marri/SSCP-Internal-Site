# what-ifs-hypothetical-design-tradeoffs

## SSCP - What Ifs (Hypothetical Design Tradeoffs)

## What Ifs (Hypothetical Design Tradeoffs)

This page contains a list of design tradeoffs and specific questions that they pose.  Please add questions.

As we determine the answers to these questions, we will add numbers and other details here.

Requires Simulation

Requires Math

Requires Testing

Done

In Progress

Array Normalization

How much power do we gain by normalizing at rest stops?

&#x20;   \- Best case scenario (mornings and evenings) / Worst case scenario (stops are mid-day)

&#x20;   \- Normalization gains vary a lot depending on time of day:

&#x20;       \- Beginning of day: 80-90% increase

&#x20;       \- Middle of day: near 0% increase

&#x20;       \- End of day: \~100% increase

&#x20;   \- Remember to take into account that much less power is being made at the beginning and end of the day.

How quickly would we need to set up and take down our array?

&#x20;   \- Time only starts after driver has set things up.

&#x20;   \- A rough average over the day is around 30 seconds.

Is motor-actuated normalization worth it?

&#x20;   \- How much power would a motor use?

&#x20;   \- No, it is not (topshell too heavy, motor too slow)

What time of day will we hit rest stops?

&#x20;   \- Roughly the same time of day as 2015, assuming same control stop locations

&#x20;   \- May need route guide to do this calculation again with 2015 rest stop locations.

Array, General

How much power does cooling make us?

GaAs vs Silicon

&#x20;   \- Are Alta or Sunpower cells better? -> Sunpower

&#x20;   \- How do we account for differences in encapsulation?

Are bypass diodes worth it?

&#x20;       \- Yes, in some modules with shading or higher curvature.

Does voltage of GaAs cells (closer to battery) make up for lower efficiency?

&#x20;   \- How many W are saved in MPPT conversion?

How do cutouts on the back shell affect heat of cells?

Aero

How much does curvature affect the array?

&#x20;   \- How would Luminos power change if it were flat?

&#x20;   \- Max P. did some analysis on this Arctan cycle, using command-line Shellpower and many different aerobody models. (find link)

Mechanicaldrive

&#x20;   \- How much does weight affect power consumptions (factoring in non-conservative Frr)

Batteries

Li-Ion

&#x20;   \- How much time does 18650G vs 18650B save us?

&#x20;       \- 18650B: 243 Wh/kg = 4.86 kWh pack

&#x20;       \- 18650G: 256 Wh/kg = 5.12 kWh pack

&#x20;       \- That's a 0.26 kWh difference \~= 6W \~= 4 minutes

&#x20;   \- How much do cells degrade over time?

&#x20;       \- Ian mentioned that time is a big factor in performance, maybe bigger than discharge cycles.

&#x20;       \- We will characterize a cell when we receive it and another as close to the race as possible.

Li-S

&#x20;   \- How much time do they gain us?

&#x20;       \- With current estimates (240-300 Wh/kg), they won't gain us any time.

Li-Si

&#x20;   \- How much time would these gain us?

&#x20;       \- Not feasible

Code&#x20;

Will narrowing cruise control speed variance save power?

&#x20;   \- How much?

&#x20;   \- What about adapting to inclines?

Composites

How many watts do we gain per subtracted kg?

&#x20;   \- Without refined Crr calculations, .473

Motors

What is our projected cruising speed for a 4m^2 array car?

&#x20;   \- With current aero estimates (\~29N in October) it is around 85 kph

&#x20;   \- Do we need to modify the motors to be optimal at this speed?

&#x20;       \- No

&#x20;   \- Do we need to change battery pack voltage?

&#x20;       \- Yes, to avoid speed limiting. (nominal voltage increased to 125V)

\[Gawan Fiore - gfiore@stanford.edu]

Last updated Oct 2, 2017
