# SSCP - Xenith Telemetry Network Topology

# Xenith Telemetry Network Topology

The old networking topology, which we tested in Summer 2011 and used in WSC 2011, is a bit of a cluster.

Summary

* Chase provides the sscp_car access point using a Picostation (long-range WiFi). It does not provide DHCP or DNS.Xenith constantly tries to connect via WiFi to sscp_car.Chase has a telemetry server which connects to the Picostation. It constantly tries to connect via TCP to Xenith.
* Chase provides the sscp_car access point using a Picostation (long-range WiFi). It does not provide DHCP or DNS.
* Xenith constantly tries to connect via WiFi to sscp_car.
* Chase has a telemetry server which connects to the Picostation. It constantly tries to connect via TCP to Xenith.

* Chase provides the sscp_car access point using a Picostation (long-range WiFi). It does not provide DHCP or DNS.
* Xenith constantly tries to connect via WiFi to sscp_car.
* Chase has a telemetry server which connects to the Picostation. It constantly tries to connect via TCP to Xenith.

Chase provides the sscp_car access point using a Picostation (long-range WiFi). It does not provide DHCP or DNS.

Xenith constantly tries to connect via WiFi to sscp_car.

Chase has a telemetry server which connects to the Picostation. It constantly tries to connect via TCP to Xenith.

So the telemetry connection happens as follows: when the telemetry systems in chase and Xenith are both on and in range, Xenith connects to the WiFi network, then the telemetry server connects to Xenith. As soon as Xenith accepts this connection, it starts sending a stream of CAN packets.

Hardware details

* The Picostation runs on 12-volt PoE (power over ethernet), so it requires a PoE injector. We've been using a 110-volt PoE injector, so it also requires an inverter in chase. Do not connect it to a PoE injector at more than 12 volts.Xenith's telemetry board has a Roving embedded WiFi chip with an antenna in the bubble (since carbon fiber is blocks the signal)The WiFi setup has good range--tested to more than half a mile--but generally requires line-of-sight
* The Picostation runs on 12-volt PoE (power over ethernet), so it requires a PoE injector. We've been using a 110-volt PoE injector, so it also requires an inverter in chase. Do not connect it to a PoE injector at more than 12 volts.
* Xenith's telemetry board has a Roving embedded WiFi chip with an antenna in the bubble (since carbon fiber is blocks the signal)
* The WiFi setup has good range--tested to more than half a mile--but generally requires line-of-sight

* The Picostation runs on 12-volt PoE (power over ethernet), so it requires a PoE injector. We've been using a 110-volt PoE injector, so it also requires an inverter in chase. Do not connect it to a PoE injector at more than 12 volts.
* Xenith's telemetry board has a Roving embedded WiFi chip with an antenna in the bubble (since carbon fiber is blocks the signal)
* The WiFi setup has good range--tested to more than half a mile--but generally requires line-of-sight

The Picostation runs on 12-volt PoE (power over ethernet), so it requires a PoE injector. We've been using a 110-volt PoE injector, so it also requires an inverter in chase. Do not connect it to a PoE injector at more than 12 volts.

Xenith's telemetry board has a Roving embedded WiFi chip with an antenna in the bubble (since carbon fiber is blocks the signal)

The WiFi setup has good range--tested to more than half a mile--but generally requires line-of-sight

Networking details

* The Picostation has IP 192.168.1.20The telemetry server in chase must have IP 192.168.1.14. Note that the Picostation does not run DHCP, so the telemetry server and everything else connected to sscp_car must set its IP manually.The solar car has IP 192.168.1.22The solar car listens on port 2000. You can test your networking setup by connecting to sscp_car, then running `telnet 192.168.1.22 2000`, and you should see raw CAN messages streaming in.The telemetry server in chase listens on port 80 or 8000. So you can point your browser to http://192.168.1.14/ or http://192.168.1.14:8000/ for the telemetry dashboard.Put the following into your /etc/hosts file (or, on Windows, C:\Windows\System32\drivers\etc\hosts)
* The Picostation has IP 192.168.1.20
* The telemetry server in chase must have IP 192.168.1.14. Note that the Picostation does not run DHCP, so the telemetry server and everything else connected to sscp_car must set its IP manually.
* The solar car has IP 192.168.1.22
* The solar car listens on port 2000. You can test your networking setup by connecting to sscp_car, then running `telnet 192.168.1.22 2000`, and you should see raw CAN messages streaming in.
* The telemetry server in chase listens on port 80 or 8000. So you can point your browser to http://192.168.1.14/ or http://192.168.1.14:8000/ for the telemetry dashboard.
* Put the following into your /etc/hosts file (or, on Windows, C:\Windows\System32\drivers\etc\hosts)

* The Picostation has IP 192.168.1.20
* The telemetry server in chase must have IP 192.168.1.14. Note that the Picostation does not run DHCP, so the telemetry server and everything else connected to sscp_car must set its IP manually.
* The solar car has IP 192.168.1.22
* The solar car listens on port 2000. You can test your networking setup by connecting to sscp_car, then running `telnet 192.168.1.22 2000`, and you should see raw CAN messages streaming in.
* The telemetry server in chase listens on port 80 or 8000. So you can point your browser to http://192.168.1.14/ or http://192.168.1.14:8000/ for the telemetry dashboard.
* Put the following into your /etc/hosts file (or, on Windows, C:\Windows\System32\drivers\etc\hosts)

The Picostation has IP 192.168.1.20

The telemetry server in chase must have IP 192.168.1.14. Note that the Picostation does not run DHCP, so the telemetry server and everything else connected to sscp_car must set its IP manually.

The solar car has IP 192.168.1.22

The solar car listens on port 2000. You can test your networking setup by connecting to sscp_car, then running `telnet 192.168.1.22 2000`, and you should see raw CAN messages streaming in.

The telemetry server in chase listens on port 80 or 8000. So you can point your browser to http://192.168.1.14/ or http://192.168.1.14:8000/ for the telemetry dashboard.

Put the following into your /etc/hosts file (or, on Windows, C:\Windows\System32\drivers\etc\hosts)

192.168.1.14 chase

192.168.1.20 chasewifi

192.168.1.22 solarcar

Now you can do things like run `ping solarcar` to see if the solar car is there, `ping chase`, and you can point your browser to http://chase/ for the telemetry dashboard!

 

