# SSCP - Aero

# Aero

Projected race speed based on drag (@ 24.59 m/s - calculated for 27-35N)

    Goal: Find projected race speeds based on theoretical drag numbers. These will allow aero team to run CFD at a more accurate speed and get better drag numbers. These numbers are a rough estimate, but they will help be more targeted with our core hours.

    Process: I wrote a script (sundae-strategy/matlab/findFitFromDrag.m) to find a new power at 24.59 m/s based on the input drag and Arctan's drag (36.07N) and then scaled Arctan's power-to-drive polyfit curve such that it output that new power @ 24.59 m/s. Then, I ran the strategy simulation code to find the optimal race speed given that power-to-drive profile (and predicted array numbers -> 4m^2 array of Sunpower bin M cells). That speed was then multiplied by 1.0132 in order to get expected average race cruise speed from overall average race speed (avg cruise speed eliminated acceleration, deceleration, and slow driving - eg. into and out of control stops). Note: the simulation code (at time of calculations) is built to run speeds in steps. Thus, these speeds may be slightly lower or higher than true simulated optimal speed.

* 25N = 90.27 kph = 25.08 m/s26N = 88.96 kph = 24.71 m/s27N = 88.05 kph = 24.46 m/s28N = 86.32 kph = 23.98 m/s29N = 85.21 kph = 23.67 m/s30N = 84.10 kph = 23.36 m/s31N = 83.08 kph = 23.08 m/s32N = 82.17 kph = 22.83 m/s33N = 81.36 kph = 22.60 m/s34N = 80.45 kph = 22.35 m/s35N = 79.64 kph = 22.12 m/s
* 25N = 90.27 kph = 25.08 m/s
* 26N = 88.96 kph = 24.71 m/s
* 27N = 88.05 kph = 24.46 m/s
* 28N = 86.32 kph = 23.98 m/s
* 29N = 85.21 kph = 23.67 m/s
* 30N = 84.10 kph = 23.36 m/s
* 31N = 83.08 kph = 23.08 m/s
* 32N = 82.17 kph = 22.83 m/s
* 33N = 81.36 kph = 22.60 m/s
* 34N = 80.45 kph = 22.35 m/s
* 35N = 79.64 kph = 22.12 m/s

* 25N = 90.27 kph = 25.08 m/s
* 26N = 88.96 kph = 24.71 m/s
* 27N = 88.05 kph = 24.46 m/s
* 28N = 86.32 kph = 23.98 m/s
* 29N = 85.21 kph = 23.67 m/s
* 30N = 84.10 kph = 23.36 m/s
* 31N = 83.08 kph = 23.08 m/s
* 32N = 82.17 kph = 22.83 m/s
* 33N = 81.36 kph = 22.60 m/s
* 34N = 80.45 kph = 22.35 m/s
* 35N = 79.64 kph = 22.12 m/s

25N = 90.27 kph = 25.08 m/s

26N = 88.96 kph = 24.71 m/s

27N = 88.05 kph = 24.46 m/s

28N = 86.32 kph = 23.98 m/s

29N = 85.21 kph = 23.67 m/s

30N = 84.10 kph = 23.36 m/s

31N = 83.08 kph = 23.08 m/s

32N = 82.17 kph = 22.83 m/s

33N = 81.36 kph = 22.60 m/s

34N = 80.45 kph = 22.35 m/s

35N = 79.64 kph = 22.12 m/s

[Gawan Fiore - gfiore@stanford.edu]

