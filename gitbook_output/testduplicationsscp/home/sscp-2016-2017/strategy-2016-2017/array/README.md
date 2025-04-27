# SSCP - Array

# Array

Control Stop Array Normalization

    Goals:

    + Figure out how much power we expect to make by normalizing at a control stops as opposed to not normalizing.

    + Determine race time that that extra power equates to.

    + Determine maximum setup + takedown time for normalization to still be worth doing.

    Process: First I determined when we were driving and when we array standing at control stops (see the control stop indexes in the Arctan WSC Baseline doc). Then I normalized the time of day (in Darwin's timezone: UTC+9:30) in the array data for each race day so that I could plot all of the days of array data on top of each other, all starting with t=0 being 8am. I did this for driving array data and control stop array standing data separately. In order to separate the array data into two data sets, I extracted the relevant data segments using a script I wrote (sundae-strategy/matlab/extractDataSegments.m).

[ Arctan WSC Baseline](/home/sscp-2016-2017/strategy-2016-2017/arctan-wsc-baseline)

    Then, for the driving data only (because there was so much of it), I took a cubic fit of each day first, and took a final cubic fit of those single-day fits plotted on top of each other (Figure 1,2). For the control stop array standing data I plotted all of the data (normalized to time of day as mentioned earlier) on one chart and took the cubic fit of it (Figure 3 - green cubic fit was used, not quadratic). The cubic fit is actually a pretty good approximation of the sinusoidal function that is array power - on most days the fit was pretty much perfect. (Figure 4 shows the plot from 2 & 3 on the same chart).

    Subtracting the driving fit from the control stop fit yielded the difference in power while normalized at control stops vs. driving over the course of an average race day (Figure 5).

The next issue in determining how much power array standing gains us was figuring out how to separate out the control stop power gains due to water cooling and those that were actually due to normalization. The difficulty is that no temperature data for the array or the water was taken during the race. The next segment below discusses how we (Gawan Fiore + John Stayner) figured out the temperature factor.

IN PROGRESS... GOING TO DO SOME ARRAY TEMPERATURE TESTS AT THE END OF OCTOBER 2016

Assumptions required to fill in data gaps:

    - Temperature of solar cells was ~50˚C while driving and ~70˚C when stopped.

    - Temperature of water that sat in convoy vehicles was ~75˚ F

Control stop ambient temperatures:

---- Day 1 ---------------------------------

      Katherine         @ 12:30pm: 35˚C

---- Day 2 ---------------------------------

      Dunmarra        @ 8:15am: 25.5˚C

      Tennant Creek  @ 1:00pm: 31.5˚C

      Barrow Creek   @ 4:30pm: 35˚C

---- Day 3 ---------------------------------

      Alice Springs    @ 10:30am: 35˚C

      Kulgera           @ 4:00pm: 34˚C

---- Day 4 ---------------------------------

      Coober Pedy    @ 11:00am: 20˚C

      Glendambo      @ 2:30pm: 21˚C

---- Day 5 ---------------------------------

      Port Augusta    @ 9:45am: 12˚C

Figure 1

![](../../../../assets/image_91af60e953.png)

Figure 2

![](../../../../assets/image_d32f124b07.png)

Figure 3

![](../../../../assets/image_0e196cd591.png)

Figure 4

![](../../../../assets/image_2d25e04d0e.png)

Figure 5

![](../../../../assets/image_03b20f4a4e.png)

[Gawan Fiore - gfiore@stanford.edu]

