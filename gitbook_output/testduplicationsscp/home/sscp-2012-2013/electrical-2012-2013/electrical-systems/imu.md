# SSCP - IMU

# IMU

Internal Measurement Unit (IMU) is a very useful system for telemetry so that they can accurately see where the car is and what is going on with it as far as inclination and such.

Requirements:

Record position data of the car as well as an accurate time stamp. Also record the inclination of the car and send out both an average as well as a roughly instantaneous reading. The instantaneous reading might give us a sense of how much the aero body is moving while the average gives us a slope of the road we are on.

Proposed Solutions:

Position and time sense: GPS seems like the most obvious solution. Good GPS data can be obtained from units made by U-Blox. This unit might be a good one.

[ U-Blox](http://www.u-blox.com/en/gps-modules/)

[ This](http://www.u-blox.com/en/gps-modules/u-blox-6-dead-reckoning-module/lea-6r.html)

Inclination Sense: A compass might be a great way to sense the incline of a road because the magnetic field lines on earth are pretty straight (double check all this). This chip may provide the resolution and accuracy we need. Whether it needs any calibration and how to do that needs to be looked into. (out of stock). Instead, this should provide the necessary measurements.

[ This](http://www.st.com/internet/analog/product/251940.jsp)

[this](http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/DM00026454.pdf)

Pressure Sensor: This pressure sensor from Measurement Specialties which has a 24bit integrated delta sigma looks like a good option for pressure sensing. 

[This](http://www.meas-spec.com/downloads/MS5803-01BA.pdf)

