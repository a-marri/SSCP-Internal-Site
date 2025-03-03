# SSCP - Stability

# Stability

## Angle of Attack Sweep

[](#h.4e5bvh7skkb0)

We will do an angle of attack sweep to look at forces and moments on the car in the full suspension pitch range. For a 1.8m wheelbase and a suspension that travels at most 6cm up and 6cm down (longer travel than actual to be conservative), the max angle from horizontal is arctan( 6cm / .9m). 

Therefore, the max pitch is +_3.81 degrees from horizontal. 

David will be running simulations on Sunwhale-019 in +- 1,2,3,4 degrees so that we can look at the stability. 

## Moment Effect

[](#h.70qxrw2pvknn)

Our aero simulations provide us aerodynamic moments about the 3 axes of the car. We are primarily concerned with the moment that the car experiences in a sidewind, so here is the analysis done on Sunwhale-014 in a 10m/s crosswind. The Mx is moment about the longitudinal axis of the car, as that is the axis that would cause the car to roll.

Mx= 34.5 Nm

Mcar = 190kg +80kg (driver) = 270kg. 

Wcar = 270kg * g = 2700N

TrackWidth= 1.31m

Normal contact from the port and starboard wheels and the delta between left and right is what counters this moment. 

In the nominal going forward case:

(TrackWidth/2) * (Fport) - (TrackWidth/2) * (Fstarboard) = Mx

Z-axis force balance:

Fport + Fstarboard = Mx

Solve:

(1.31/2) * (Fport) - (1.31/2) * (2700- Fstarboard) = 34.5

Fport = 1376N

Fstarboard  = 1323 N

Delta = Fport - Fstarboard = 53N

Given that the wheels on the port and starboard sides of the car normally support 2700/2 = 1350N each, this Delta of 53N indicates that a 10 m/s crosswind is still far from causing the car to roll. 

