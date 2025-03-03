# SSCP - WiFi Infrastructure

# WiFi Infrastructure

Older page on WiFi Infrastructure: https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2014-2015/code-2014-2015/wifi-infrastructure

WiFi Overview

* The vehicle computer keeps track of its internal state using the DataMessage struct.Periodically, the vehicle computer sends its internal state over Ethernet to our WiFi router (AKA ethernet bridge).Our WiFi router broadcasts packets. A computer in the chase vehicle connects to the WiFi router.The chase vehicle computer runs a script which logs and parses the WiFi packets for Telemetry.
* The vehicle computer keeps track of its internal state using the DataMessage struct.
* Periodically, the vehicle computer sends its internal state over Ethernet to our WiFi router (AKA ethernet bridge).
* Our WiFi router broadcasts packets. A computer in the chase vehicle connects to the WiFi router.
* The chase vehicle computer runs a script which logs and parses the WiFi packets for Telemetry.

* The vehicle computer keeps track of its internal state using the DataMessage struct.
* Periodically, the vehicle computer sends its internal state over Ethernet to our WiFi router (AKA ethernet bridge).
* Our WiFi router broadcasts packets. A computer in the chase vehicle connects to the WiFi router.
* The chase vehicle computer runs a script which logs and parses the WiFi packets for Telemetry.

The vehicle computer keeps track of its internal state using the DataMessage struct.

Periodically, the vehicle computer sends its internal state over Ethernet to our WiFi router (AKA ethernet bridge).

Our WiFi router broadcasts packets. A computer in the chase vehicle connects to the WiFi router.

The chase vehicle computer runs a script which logs and parses the WiFi packets for Telemetry.

Setup

We're experimenting with the Xiaomi Mi WiFi Nano. Eric Thong (thongerick@gmail.com) installed a custom firmware, since the original interface is in Chinese.

Openwrt instructions: https://wiki.openwrt.org/toh/xiaomi/nano

[https://wiki.openwrt.org/toh/xiaomi/nano](https://wiki.openwrt.org/toh/xiaomi/nano)

LEDE firmware, which is on the board: https://lede-project.org/toh/hwdata/xiaomi/xiaomi_miwifi_nano

[https://lede-project.org/toh/hwdata/xiaomi/xiaomi_miwifi_nano](https://lede-project.org/toh/hwdata/xiaomi/xiaomi_miwifi_nano)

Changing Settings

* Power the Xiaomi WiFi router over micro USB.
* Connect an ethernet cable from the router to a laptop. Make sure the ethernet cable is connected to a LAN port (white), not a WAN port (blue).
* On the laptop, navigate to 10.0.0.1. Username: root, Password: solarpower

Power the Xiaomi WiFi router over micro USB.

Connect an ethernet cable from the router to a laptop. Make sure the ethernet cable is connected to a LAN port (white), not a WAN port (blue).

On the laptop, navigate to 10.0.0.1. Username: root, Password: solarpower

Connecting to the router

* The router is currently named sscp-xiaomi (or some variant of that).
* Password: solarpower
* This router, marked as "EVA", can be connected to from a distance of about 55 feet when the topshell and canopy are fully closed.
* Note that you don't need to set your IP address to anything.
* Run the udp parser script in Dragonfly to read packets. (Currently a work in progress.)

The router is currently named sscp-xiaomi (or some variant of that).

Password: solarpower

This router, marked as "EVA", can be connected to from a distance of about 55 feet when the topshell and canopy are fully closed.

Note that you don't need to set your IP address to anything.

Run the udp parser script in Dragonfly to read packets. (Currently a work in progress.)

Old Setup

This is the setup used for Xenith, Luminos, and Arctan.

WiFi Router

We used PicoStation2HP ethernet bridges on Xenith, Luminos, and Arctan. We plan to continue to use these for future cars. A reference manual for these devices: http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf. A reference manual for AirOS 3 is here: http://wiki.ubnt.com/AirOS_3

[http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf](http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf)

[http://wiki.ubnt.com/AirOS_3](http://wiki.ubnt.com/AirOS_3)

The ethernet bridge is powered over ethernet. If you need to use the ethernet bridge without the car, you will need a POE injector (se.g. https://www.amazon.com/gp/product/B004EFHN66/ref=od_aui_detailpages00?ie=UTF8&psc=1). There should be several lying around the shop.

Setting up the WiFi Router

This should have already been done. But, if you find yourself with a new router, or you have reset an existing router, there are steps you have to do:

* Connect the WiFi Router to the laptop directly using a POE injector.Edit the IP address of your computer (you can change it back later)Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20In your web browser, navigate to 192.168.1.20.To login, Username: ubnt, Password: ubntYou should have access to the settings of the WiFi router!Choose the Wireless tab, and change the Wireless Mode to Access Point.Navigate to settings, and change the settings to correspond with the table below. Or, add a new entry if you have a completely new WiFi router.
* Connect the WiFi Router to the laptop directly using a POE injector.
* Edit the IP address of your computer (you can change it back later)Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20
* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20
* IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 192.168.1.20
* In your web browser, navigate to 192.168.1.20.
* To login, Username: ubnt, Password: ubnt
* You should have access to the settings of the WiFi router!
* Choose the Wireless tab, and change the Wireless Mode to Access Point.
* Navigate to settings, and change the settings to correspond with the table below. Or, add a new entry if you have a completely new WiFi router.

* Connect the WiFi Router to the laptop directly using a POE injector.
* Edit the IP address of your computer (you can change it back later)Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20
* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20
* IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 192.168.1.20
* In your web browser, navigate to 192.168.1.20.
* To login, Username: ubnt, Password: ubnt
* You should have access to the settings of the WiFi router!
* Choose the Wireless tab, and change the Wireless Mode to Access Point.
* Navigate to settings, and change the settings to correspond with the table below. Or, add a new entry if you have a completely new WiFi router.

Connect the WiFi Router to the laptop directly using a POE injector.

Edit the IP address of your computer (you can change it back later)

* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 192.168.1.20
* IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 192.168.1.20

Navigate to Network Connections on your PC.

Right click on Local Area Connection, and go to Properties.

In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.

Mark "Use the following IP address", and input:

* IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 192.168.1.20

IP address: 192.168.1.21 (the IP address just needs to be different from that of the router)

Subnet mask: 255.255.255.0

Default gateway: 192.168.1.20

In your web browser, navigate to 192.168.1.20.

To login, Username: ubnt, Password: ubnt

You should have access to the settings of the WiFi router!

Choose the Wireless tab, and change the Wireless Mode to Access Point.

Navigate to settings, and change the settings to correspond with the table below. Or, add a new entry if you have a completely new WiFi router.

Using an existing WiFi Router

For testing WiFi routing code using a Discovery Board, reference the telemetry_discovery project.

* Editing network settings/viewing settingsConnect the WiFi Router to the laptop directly using a POE injector.Edit the IP address of your computer (you can change it back later):Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1Depending on the WiFi router that you have, navigate to the IP address listed in the table below.To login, Username: admin, Password: s0larpowerYou should have access to the settings of the WiFi router!
* Connect the WiFi Router to the laptop directly using a POE injector.
* Edit the IP address of your computer (you can change it back later):Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* IP address: 10.0.0.x (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 10.0.0.1
* Depending on the WiFi router that you have, navigate to the IP address listed in the table below.
* To login, Username: admin, Password: s0larpower
* You should have access to the settings of the WiFi router!
* Using the WiFi router for testing/etc.If you haven't already, clone the Dragonfly telemetry project from the SSCP github.Flash and run the code on a discovery board, or turn on the car.Connect to the WiFi router. The WiFi network name is usually something like "sscp-wds" or "sscp-testing".In the Dragonfly directory, navigate to udp_logger and run udp_logger.py.
* If you haven't already, clone the Dragonfly telemetry project from the SSCP github.
* Flash and run the code on a discovery board, or turn on the car.
* Connect to the WiFi router. The WiFi network name is usually something like "sscp-wds" or "sscp-testing".
* In the Dragonfly directory, navigate to udp_logger and run udp_logger.py.

Editing network settings/viewing settings

* Connect the WiFi Router to the laptop directly using a POE injector.
* Edit the IP address of your computer (you can change it back later):Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* IP address: 10.0.0.x (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 10.0.0.1
* Depending on the WiFi router that you have, navigate to the IP address listed in the table below.
* To login, Username: admin, Password: s0larpower
* You should have access to the settings of the WiFi router!

Connect the WiFi Router to the laptop directly using a POE injector.

Edit the IP address of your computer (you can change it back later):

* Navigate to Network Connections on your PC.Right click on Local Area Connection, and go to Properties.In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* IP address: 10.0.0.x (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 10.0.0.1

* Navigate to Network Connections on your PC.
* Right click on Local Area Connection, and go to Properties.
* In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.
* Mark "Use the following IP address", and input:IP address: 10.0.0.x (the IP address just needs to be different from that of the router)Subnet mask: 255.255.255.0Default gateway: 10.0.0.1
* IP address: 10.0.0.x (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 10.0.0.1

Navigate to Network Connections on your PC.

Right click on Local Area Connection, and go to Properties.

In Properties, navigate to Internet Protocol Version 4 (TCP/IPv4), and click Properties.

Mark "Use the following IP address", and input:

* IP address: 10.0.0.x (the IP address just needs to be different from that of the router)
* Subnet mask: 255.255.255.0
* Default gateway: 10.0.0.1

IP address: 10.0.0.x (the IP address just needs to be different from that of the router)

Subnet mask: 255.255.255.0

Default gateway: 10.0.0.1

Depending on the WiFi router that you have, navigate to the IP address listed in the table below.

To login, Username: admin, Password: s0larpower

You should have access to the settings of the WiFi router!

Using the WiFi router for testing/etc.

* If you haven't already, clone the Dragonfly telemetry project from the SSCP github.
* Flash and run the code on a discovery board, or turn on the car.
* Connect to the WiFi router. The WiFi network name is usually something like "sscp-wds" or "sscp-testing".
* In the Dragonfly directory, navigate to udp_logger and run udp_logger.py.

If you haven't already, clone the Dragonfly telemetry project from the SSCP github.

Flash and run the code on a discovery board, or turn on the car.

Connect to the WiFi router. The WiFi network name is usually something like "sscp-wds" or "sscp-testing".

In the Dragonfly directory, navigate to udp_logger and run udp_logger.py.

* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.
* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.
* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.

* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.
* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.

* udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.

udp_logger.py may mention something about disabling the Firewall. This may not be necessary, but you should double-check for sanity.

* You should be able to see packet snippets from the discovery board or from the car!
* You should be able to see packet snippets from the discovery board or from the car!

* You should be able to see packet snippets from the discovery board or from the car!

You should be able to see packet snippets from the discovery board or from the car!

Summary of WiFi settings

* Ubiquiti Credentials: admin/s0larpowerSSID: "sscp-solarcar-nearnet"Channel: 11Configuration: all Picostationsare configured as "Access Point WDS"Security: Password is "chickslovemybigdata" long storyBridge IP: StaticIP: 10.0.0.xNetmask: 255.255.255.0Gateway IP: 10.0.0.1Primary DNS IP: 8.8.8.8Network Mode: Bridge
* Ubiquiti Credentials: admin/s0larpower
* SSID: "sscp-solarcar-nearnet"
* Channel: 11
* Configuration: all Picostationsare configured as "Access Point WDS"
* Security: Password is "chickslovemybigdata" long story
* Bridge IP: Static
* IP: 10.0.0.x
* Netmask: 255.255.255.0
* Gateway IP: 10.0.0.1
* Primary DNS IP: 8.8.8.8
* Network Mode: Bridge

* Ubiquiti Credentials: admin/s0larpower
* SSID: "sscp-solarcar-nearnet"
* Channel: 11
* Configuration: all Picostationsare configured as "Access Point WDS"
* Security: Password is "chickslovemybigdata" long story
* Bridge IP: Static
* IP: 10.0.0.x
* Netmask: 255.255.255.0
* Gateway IP: 10.0.0.1
* Primary DNS IP: 8.8.8.8
* Network Mode: Bridge

Ubiquiti Credentials: admin/s0larpower

SSID: "sscp-solarcar-nearnet"

Channel: 11

Configuration: all Picostationsare configured as "Access Point WDS"

Security: Password is "chickslovemybigdata" long story

Bridge IP: Static

IP: 10.0.0.x

Netmask: 255.255.255.0

Gateway IP: 10.0.0.1

Primary DNS IP: 8.8.8.8

Network Mode: Bridge

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

Relaying Packets

Having too many computers connect to the solar car wifi can draw a lot of power, which is undesirable. To fix this, I am proposing the following structure:

* Exactly one computer connects to the solar car network. This computer is also connected via ethernet to an access point.
* This computer runs the script attached below (WIP). The script basically listens for any packets on the network on one port and broadcasts the packets over a different port.
* A second computer connects to the chase access point and runs dragonfly telemetry as usual.
* Other laptops can connect to the chase access point wifi as well and view telemetry on their browsers.

Exactly one computer connects to the solar car network. This computer is also connected via ethernet to an access point.

This computer runs the script attached below (WIP). The script basically listens for any packets on the network on one port and broadcasts the packets over a different port.

A second computer connects to the chase access point and runs dragonfly telemetry as usual.

Other laptops can connect to the chase access point wifi as well and view telemetry on their browsers.

This new structure requires two designated laptops: one to forward packets and one to run telemetry. This new structure will also require one access point in the chase vehicle. However, we may be able to simplify this structure by using a router instead of the laptop+ access point.

How to use the system (during test drives, actual drives, etc.)

* All the information is here: https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/running-dragonfly-telemetry

All the information is here: https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/running-dragonfly-telemetry

[https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/running-dragonfly-telemetry](/stanford.edu/testduplicationsscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/running-dragonfly-telemetry)

