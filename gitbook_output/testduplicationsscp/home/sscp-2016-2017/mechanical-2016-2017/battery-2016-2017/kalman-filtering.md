# SSCP - Kalman Filtering

# Kalman Filtering

Goal

Explore the use of Kalman Filtering as a method of combining IVT and Amp-hour counting SoC determination methods. 

History

Max Praglin's SoC calculations for Luminos (WSC2013) used a complementary filter, which was simpler to implement than the Kalman filter and relatively effective.

(From Max)

To combine voltage/current/temperature (IVT) based SOC and amp-hour counting, a Kalman filter would be ideal. I opted for the simple approach of a complementary filter, which essentially low-pass-filters the IVT lookup and high-pass-filters the amp-hour counting. This combination does introduce some amount of phase lag because it is implemented as an IIR (although this phase lag can be lessened by relying more on amp-hour counting). The benefit of this approach is that an incorrectly guessed total capacity will be ignored over a long timespan of low current (such as when the car is sitting). This is important because the capacity of the cell at 0.01C versus 1.0C is significant - it varied from 3.19 Ah to 3.37 Ah depending on the current and temperature of the discharge. 

(Max cont.)

I highly recommend that the next team use a complementary filter (it is simple, easy to tune by visual inspection, and computationally light). If further work is to be done, I recommend that it be put into calibration of the amp-hour counter, because it drifted by multiple percentage points over the course of the race. The NCR18650B model worked well and required perhaps hundreds of hours of effort and data collection, and it's not worth repeating unless we get new cells. The complementary filter did a splendid job of utilizing both data sets. The pack cut out when MATLAB reported 1-2% SOC.

Implementation

http://www.mathworks.com/help/control/ug/kalman-filtering.html

### Kalman Filtering

[](#h.2fpj1ccsjqc)

To overcome the shortcomings of the Voltage method and the Current integration method, a Kalman filter can be used. The battery can be modeled with an electrical model which the Kalman filter will use to predict the over-voltage, due to the current. In combination with coulomb counting, it can make an accurate estimation of the state of charge. The strength of a Kalman filter is that it is able to adjust its trust of the battery voltage and coulomb counting in real time. (Wikipedia)

[Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter)

Literature

Simplified EKF (isothermal) 

https://www.mathworks.com/tagteam/76108_SAE%202013%20-%20Simplified%20EKF%20Battery%20Model.pdf

[https://www.mathworks.com/tagteam/76108_SAE%202013%20-%20Simplified%20EKF%20Battery%20Model.pdf](https://www.mathworks.com/tagteam/76108_SAE%202013%20-%20Simplified%20EKF%20Battery%20Model.pdf)

General KF

http://www.mathworks.com/help/control/ug/kalman-filtering.html

[http://www.mathworks.com/help/control/ug/kalman-filtering.html](http://www.mathworks.com/help/control/ug/kalman-filtering.html)

http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf

[http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf](http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf)

Parameter Estimation

http://www.mathworks.com/videos/estimating-parameters-of-a-battery-68957.html

[http://www.mathworks.com/videos/estimating-parameters-of-a-battery-68957.html](http://www.mathworks.com/videos/estimating-parameters-of-a-battery-68957.html)

http://www.mathworks.com/videos/automating-battery-model-parameter-estimation-using-experimental-data-81987.html?form_seq=conf1386&elqsid=1471936367580&potential_use=Student&country_code=US

[http://www.mathworks.com/videos/automating-battery-model-parameter-estimation-using-experimental-data-81987.html?form_seq=conf1386&elqsid=1471936367580&potential_use=Student&country_code=US](http://www.mathworks.com/videos/automating-battery-model-parameter-estimation-using-experimental-data-81987.html?form_seq=conf1386&elqsid=1471936367580&potential_use=Student&country_code=US)

Simplified explanations:

http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/#mjx-eqn-kalpredictfull

[http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/#mjx-eqn-kalpredictfull](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/#mjx-eqn-kalpredictfull)

http://www.cl.cam.ac.uk/~rmf25/papers/Understanding%20the%20Basis%20of%20the%20Kalman%20Filter.pdf

[http://www.cl.cam.ac.uk/~rmf25/papers/Understanding%20the%20Basis%20of%20the%20Kalman%20Filter.pdf](http://www.cl.cam.ac.uk/~rmf25/papers/Understanding%20the%20Basis%20of%20the%20Kalman%20Filter.pdf)

Description of implementation (for an Arduino-based IMU)

http://blog.tkjelectronics.dk/2012/09/a-practical-approach-to-kalman-filter-and-how-to-implement-it/

[http://blog.tkjelectronics.dk/2012/09/a-practical-approach-to-kalman-filter-and-how-to-implement-it/](http://blog.tkjelectronics.dk/2012/09/a-practical-approach-to-kalman-filter-and-how-to-implement-it/)

Description of how a Li-ion ECM was created (including param estimation)

http://uu.diva-portal.org/smash/get/diva2:946064/FULLTEXT01.pdf

[http://uu.diva-portal.org/smash/get/diva2:946064/FULLTEXT01.pdf](http://uu.diva-portal.org/smash/get/diva2:946064/FULLTEXT01.pdf)

Comparative Study of 18650 Cells (including ECMs and Params)

http://jes.ecsdl.org/content/162/8/A1592.full

[http://jes.ecsdl.org/content/162/8/A1592.full](http://jes.ecsdl.org/content/162/8/A1592.full)

Complementary Filter 

https://b94be14129454da9cf7f056f5f8b89a9b17da0be.googledrive.com/host/0B0ZbiLZrqVa6Y2d3UjFVWDhNZms/filter.pdf

[https://b94be14129454da9cf7f056f5f8b89a9b17da0be.googledrive.com/host/0B0ZbiLZrqVa6Y2d3UjFVWDhNZms/filter.pdf](https://b94be14129454da9cf7f056f5f8b89a9b17da0be.googledrive.com/host/0B0ZbiLZrqVa6Y2d3UjFVWDhNZms/filter.pdf)

[](https://drive.google.com/folderview?id=1dVQeBXUpfc6GzhOrAZHjpfemEjMfQ2XT)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1dVQeBXUpfc6GzhOrAZHjpfemEjMfQ2XT#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1dVQeBXUpfc6GzhOrAZHjpfemEjMfQ2XT#list" frameborder="0"></iframe>

