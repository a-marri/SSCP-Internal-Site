# SSCP - Power Consumption Model

# Power Consumption Model

This Page is for listing the larger structure of the power consumption and generation in the car. It should incorporate the subsystems in a larger model of the car.

Work in this field can be found in the code base under strategy > speculation.

## .go files

[](#h.phihpbb5029r)

The .go files and related .xlsx in the speculation folder are set to simulate a cruiser race based on different car parameters. This model is well-suited towards running different car parameters against each other in a simple model.

The main algorithm for SOC (Battery Pack's State of Charge) is as follows (simplified):

Note calculations by energy.

Note solar energy a fn of average array power.

for a:=0; a < distance; a++ {

        // PHYSICS:

energyAero float64 = 1000 * 0.5 * airDensity * Cd * A * speed * speed

energyRolling float64 = 1000 * Crr * mass * gravity

energySolar float64 = avgArrayPower * 1000 / speed

                ...

// Update pack state

remainingEnergy -= (energyAero + energyRolling - energySolar)

                // Check against overuse

                if remainingEnergy < 0

return -1.0

        }

See Gavin for more details on this simulation run.

## .m files

[](#h.xw3okwih68qp)

Too-many .m files will be found within speculation > class_comparison. Check the README as a glossary and first line of defense against confusion. While Challenger vs. Cruiser is more or less a resolved discussion, the code found within runrace.m may still be of use.

The runrace.m code has a fair amount of overhead for variable parameters and sweeping possible battery pack size (non-applicable to challenger class). The challenger class will likely only use the command runrace(0) in MATLAB, which indicates 0 charge stops across Australia.

The main algorithm for SOC (Battery Pack's State of Charge) is as follows (simplified):

Note calculations by power.

Note solar power a function of more complex calc_insolation_1 model.

% Power Consumption:

        power_aero    = 0.5*airdensity*Cd*A*(speedvect*meterspersecond).^3;

        power_rolling = Crr*mass*g*speedvect*meterspersecond;

        P_used = (power_rolling + power_aero + power_static) ./ 1000;

        e_used = P_used .* drivehours;

 

       ...

% Power Production:

       for    days = 1 :  ceil(drivehours / dayhrs)

                ...

                power_curve = calc_insolation_1(october, date, [startday:precision:fin], lat, 1);

                        %% ^^ grabs insolation values over daylight hours of the drive,

                        %% ^^ with simplifying assumption of position as 1/2*(start_latitude + end_latitude) for the day

                        %% See Insolation Models for further detail on calc_insolation_1

                 e_in = e_in + (trapz(power_curve) * precision * scalefactor);

                        %% ^^ integrate over power_curve, then scale by WSC data fudgefactor to match model to expected avgArrayPower

       end

       % Check against overuse only at the end of each day's measurements:

             if    (e_used >= (e_in + batteryvals))

                    speedvect = -1;

             end

