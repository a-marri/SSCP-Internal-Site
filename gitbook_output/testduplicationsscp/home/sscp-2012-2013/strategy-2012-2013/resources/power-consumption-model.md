# power-consumption-model

## SSCP - Power Consumption Model

## Power Consumption Model

This Page is for listing the larger structure of the power consumption and generation in the car. It should incorporate the subsystems in a larger model of the car.

Work in this field can be found in the code base under strategy > speculation.

### .go files

The .go files and related .xlsx in the speculation folder are set to simulate a cruiser race based on different car parameters. This model is well-suited towards running different car parameters against each other in a simple model.

The main algorithm for SOC (Battery Pack's State of Charge) is as follows (simplified):

Note calculations by energy.

Note solar energy a fn of average array power.

for a:=0; a < distance; a++ {

&#x20;       // PHYSICS:

energyAero float64 = 1000 \* 0.5 \* airDensity \* Cd \* A \* speed \* speed

energyRolling float64 = 1000 \* Crr \* mass \* gravity

energySolar float64 = avgArrayPower \* 1000 / speed

&#x20;               ...

// Update pack state

remainingEnergy -= (energyAero + energyRolling - energySolar)

&#x20;               // Check against overuse

&#x20;               if remainingEnergy < 0

return -1.0

&#x20;       }

See Gavin for more details on this simulation run.

### .m files

Too-many .m files will be found within speculation > class\_comparison. Check the README as a glossary and first line of defense against confusion. While Challenger vs. Cruiser is more or less a resolved discussion, the code found within runrace.m may still be of use.

The runrace.m code has a fair amount of overhead for variable parameters and sweeping possible battery pack size (non-applicable to challenger class). The challenger class will likely only use the command runrace(0) in MATLAB, which indicates 0 charge stops across Australia.

The main algorithm for SOC (Battery Pack's State of Charge) is as follows (simplified):

Note calculations by power.

Note solar power a function of more complex calc\_insolation\_1 model.

% Power Consumption:

&#x20;       power\_aero    = 0.&#x35;_&#x61;irdensit&#x79;_&#x43;&#x64;_&#x41;_(speedvect\*meterspersecond).^3;

&#x20;       power\_rolling = Cr&#x72;_&#x6D;as&#x73;_&#x67;_speedvec&#x74;_&#x6D;eterspersecond;

&#x20;       P\_used = (power\_rolling + power\_aero + power\_static) ./ 1000;

&#x20;       e\_used = P\_used .\* drivehours;

&#x20;

&#x20;      ...

% Power Production:

&#x20;      for    days = 1 :  ceil(drivehours / dayhrs)

&#x20;               ...

&#x20;               power\_curve = calc\_insolation\_1(october, date, \[startday:precision:fin], lat, 1);

&#x20;                       %% ^^ grabs insolation values over daylight hours of the drive,

&#x20;                       %% ^^ with simplifying assumption of position as 1/2\*(start\_latitude + end\_latitude) for the day

&#x20;                       %% See Insolation Models for further detail on calc\_insolation\_1

&#x20;                e\_in = e\_in + (trapz(power\_curve) \* precision \* scalefactor);

&#x20;                       %% ^^ integrate over power\_curve, then scale by WSC data fudgefactor to match model to expected avgArrayPower

&#x20;      end

&#x20;      % Check against overuse only at the end of each day's measurements:

&#x20;            if    (e\_used >= (e\_in + batteryvals))

&#x20;                   speedvect = -1;

&#x20;            end
