# telemetry-server

## SSCP - Telemetry Server

## Telemetry Server

### Single Board Computers

#### Gumstix

Gumstix is a local San Jose company that makes single board computer the size of a stick of gum based on TI OMAP chips. They sponsored the project with \~1k of equipment for the Xenith HMD setup. Unfortunately, their hardware is 2-3 years!! out of date. In addition their wi-fi versions only have up to 40kps throughput with double digit cpu usage. Finally, they do not have good documentation or support and designing a board around it is challenging as well as getting drivers to work on modern os with their dated hardware. A version of telemetry was built using a gumstix IronStorm; however, due to hardware limitations and extreme software difficulties getting CAN and WIFI it was decided designing around the gumstix was a bad idea.&#x20;

[Gumstix](http://www.gumstix.com/)

#### Panda Board

On the advice of DC we tried the opensource PandaBoard which features more modern hardware and much much much better support. We were able to get hardware can, and fast host mode wifi up and running with minimal amounts of trouble. It is mechanically not convenient to integrate.&#x20;

[PandaBoard](http://pandaboard.org/)

#### Nitrogen 6x

&#x20;A new board with the most modern hardware (4core ARM and DDR3!) it lacks documentation and good support but is the most modern and is thus the most likely to be well supported by the community. This is what the team has acquired and will integrate this into the vehicle.

[This](http://boundarydevices.com/products/nitrogen6x-som/)
