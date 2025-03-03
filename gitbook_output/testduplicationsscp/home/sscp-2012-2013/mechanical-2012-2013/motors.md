# SSCP - Motors

# Motors

This page is a directory to various motors used for solar car purposes:

Motor Overall Requirements

A motor used for the World Solar Challenge, in general, must meet the following specs:

1. Be direct drive. Indirect drive introduces an efficiency hit, even with a well designed chain, belt or gear drive. No transmission is 100% efficient

2. Be designed for an operating voltage from ~100V to ~150V. Since the dominant controller, the Tritium Wavesculptor22, is happiest operating in this range, we tend to select motors that match this voltage.

3. Must have a peak torque of 50 N-m for climbing the steepest hill in Australia. This specification is based on the original CSIRO design. The new MARAND design is tested to 130 N-m.

4. Must be ready to meet the GM GMW3172 specification for shock and vibration for an unsprung mass. 

    The specification lists the shock specification for unsprung mass as a 100g shock, 11ms half-sine, 20 times in the direction of loading.

    The vibration specification is ??????????

5. Must meet the static FEA 4-2-1 loading scenario detailed under the Mechanical Engineering -> suspension without any interference

6. Must be designed for a fatigue life of 10,000 miles of road driving. 10,000 mi/(11in*2*pi ) = 9.167*10^6 rotation cycles.

7. Must have temperature feedback

8. Must have at least 200V DC isolation from any winding to case

9. Must have a method to retain the wheel nut. Wheel loosening is a big problem that affects the NGM design. Any motor should be designed or hacked to support wheel nut locks.

10. Must be designed for no maintenance for the duration of the race and testing in Australia (~3000 miles)

