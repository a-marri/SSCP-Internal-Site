# SSCP - BMS 6.5 Array Current Sensor Board

# BMS 6.5 Array Current Sensor Board

## Design:

[](#h.ypmi4226jll8)

Introduction:

The iteration of BMS that raced in Australia (BMS 6.5) generally has very good measurement capabilities; however, the array current sensor is noisy when the car is driving due to the poor PSSR of the VDD supply rail and the inherent noise sensitivity of the SAR type ADC that is built into the STM32s. To get better on board ADC performance would require a major redesign of the way that the processor is powered which is not feasable without spinning another rev of the BMS board. Due to the complexity of the layout, and cost of the components on the board it was decided that simply adding a hacked on board would be preferable as it would save significant amounts of money and time. 

[SAR](http://en.wikipedia.org/wiki/Successive_Approximation_ADC)

Goals:

When the car was driving the array current sensor has so much noise that it is useless and the array data during WSC2013 was measured by getting the raw data from the MPPTs which fortunately have very clean measurements. The main shunt on the battery pack has very good performance with 15 bits of non-noise resolution when driving. The goal of the update was to bring that level of performance to the array sensing. 

Execution:

The current sense circuitry used is copied from the BMS 6.5 schematic so it has already been validated, has over 3k test miles, and has no known issues. At a high level the circuit is built around a differential 24 bit delta sigma ADC, programable Sin-x filter with a 124x PGA(programmable gain amplifier) differential analog front end with a sampling rate of up to 2k. This chip has a number of properties which make it ideal for sensing current in a noisy environment. Firstly, it features a delta sigma type converter which offers a number of advantages in noisy environments. Because delta sigma converters work by significantly oversampling a signal and then using digital filters to extract more bits out of a signal they are inherently more noise immune and have a much larger PSSR than converters based on other typologies. In addition, because the filter points are programmable they can be reset to reject the primary noise frequencies on the car (which happens to be the switching frequency of the motor controller and its harmonics). Having a PGA that was differential reduced the chip count and made noise less of a problem since all the analog processing was contained on one piece of silicon. This greatly simplified the design as there are no single chip differential amplifiers with the noise and voltage offset specifications to easily beat the built in PGA. This means that a design would have to be made out of normal op amps which would be more complicated. Finally the fact that the chip is fully differential means that it rejects common mode noise very well. 

[ delta sigma](http://en.wikipedia.org/wiki/Delta-sigma_modulation)

Because we want to be able to sense both positive and negative array current (negative in the case of a fault condition) this requires a bipolar supply so that voltages below ground potential can be measured. In addition because we want high side current sensing (which makes it easier to detect fault conditions) the board needs its own bipolar isolate power supply, and digital isolators to support communication with the processor which is at a different potential.  

## Bring Up:

[](#h.rsfm6fdhn15k)

## Change Log:

[](#h.5m1hsqxdi5bh)

## Future Recommendations:

[](#h.p1xov7abxb07)

