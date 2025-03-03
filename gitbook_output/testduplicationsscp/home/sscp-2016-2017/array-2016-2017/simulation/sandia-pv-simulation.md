# SSCP - Sandia PV Simulation

# Sandia PV Simulation

Had first success with Sandia PV simulation routines tonight thanks to a kick start from Gawan. (https://pvpmc.sandia.gov/) Produced this plot of apparent sun elevation angle and sun azimuth when curves in the road are taken into account.

[https://pvpmc.sandia.gov/](https://pvpmc.sandia.gov/)

![](../../../../../assets/image_387e188b81.png)

And simulate each irradiance component.

Global Horizontal Irradiance (GHI) is the amount of terrestrial irradiance falling on a surface horizontal to the surface of the earth.

Direct Normal Irradiance (DNI) is the terrestrial irradiance received by a surface normal to the sun exclusive diffuse irradiance

Diffuse Horizontal Irradiance (DHI) is the terrestrial irradiance received by a horizontal surface which has been scattered or diffused by the atmosphere.

Now we can do things like combine this data with the McGeehee absorption data:

![](../../../../../assets/image_64d5caa1d8.png)

![](../../../../../assets/image_4715517aa6.png)

To come up with which array absorbed more light and make decisions about to make sundae even better.

Logan Herrera

