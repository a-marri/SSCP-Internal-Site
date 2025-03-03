# SSCP - Wifi Infrastructure

# Wifi Infrastructure

We used PicoStation2HP ethernet bridges on Xenith, Luminos and plan to use them again for Arctan. A reference manual for these devices: http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf. A reference manual for AirOS 3 is here: http://wiki.ubnt.com/AirOS_3

[http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf](http://www.afrikanet.net/help/d2/WLAN/ubiquiti/picostations/User-Guide-Pico%20station.pdf)

[http://wiki.ubnt.com/AirOS_3](http://wiki.ubnt.com/AirOS_3)

We're using the XS2.ar2316.v4.0.4.5074.150724.1340-8M.bin firmware. The official docs and more up-to-date firmware are here.

[XS2.ar2316.v4.0.4.5074.150724.1340-8M.bin](http://xs2.ar2316.v4.0.4.5074.150724.1340-8m.bin)

[ here](https://www.ubnt.com/download/airmax-legacy/picostation-2/picostation2hp)

To reset to defaults: 

1.  Network settings of PC: IP:192.168.1.254; subnet:255.255.255.0

2. Release the reset button ~10 seconds (but not longer) after turning the device on. You will know it's ready when the LEDs change.

3. Ping 192.168.1.20 (Be a static IP like 192.168.1.21

4. Success!

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

A configuration file for UBNT3 and UBNT in mesh mode is attached.

The "Pit" ubiquiti may serve as a bridge between the WDS mesh and a network in the pits having internet connectivity. In the shop, it is plugged in to the "solarcar" router, such that you can connect to "solarcar" and simultaneously see packets from the car and surf the web.

After 2013 WSC notes: We discovered that the WDS setup didn't really work as anticipated. The problem is that the Ubiquiti access points are not designed to be mobile. Signal drops between the WDS nodes meant that network throughput plummeted as the convoy vehicles spread apart.

Also, upon a closer reading of the Ubiquiti user manual, it says not to configure the APs in a mesh type setup, or any network topology with loops. However, even after making the WDS nodes point-to-point, network throughput was still not good.

We ended up dropping the WDS setup all together and configured two Ubiquitis in Access Point mode and two Ubiquitis in Base station mode. The solar car AP would connect with the chase base station. The chase base station would connect via ethernet to the chase AP. Then, the lead base station would be connected to the chase AP. The solarcar-chase WiFi connection was on a different WiFi channel than the chase-lead connection. In this way, we hoped to isolate the vital solarcar-chase connection from the rest of the network.

Even though this setup was vastly better than the previous setups, I found that the chase laptop got more packets/sec from just connecting to the solar car AP directly, instead of connecting to the chase AP. We should investigate this further if we want a convoy network for the next race (for IRC, FTP). For the race, the chase strategy laptop was connected to the solar car AP directly.

[](https://drive.google.com/folderview?id=1Um4zROWsy9xLiJCThCuYGNT5n-sGCfPq)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1Um4zROWsy9xLiJCThCuYGNT5n-sGCfPq#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=1Um4zROWsy9xLiJCThCuYGNT5n-sGCfPq#list" frameborder="0"></iframe>

