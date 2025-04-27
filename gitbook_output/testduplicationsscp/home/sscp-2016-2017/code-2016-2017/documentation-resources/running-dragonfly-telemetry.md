# SSCP - Running Dragonfly Telemetry

# Running Dragonfly Telemetry

The main difference from previous cycles' configurations is that computers will generally want to connect to the router computer's access point instead of the car; the router computer is a middleman. 

You will need:

* Two computersOne Toughbook for routing (Rocky, Sally, or Happy #2. Happy #1 cannot route due to its broken ethernet port!!!)One other laptop for running the Dragonfly server (Mac or Linux only. Rocky does not have Ubuntu installed, and Sally has issues!!!!!!)
* One Toughbook for routing (Rocky, Sally, or Happy #2. Happy #1 cannot route due to its broken ethernet port!!!)
* One other laptop for running the Dragonfly server (Mac or Linux only. Rocky does not have Ubuntu installed, and Sally has issues!!!!!!)
* One wireless access point
* One PoE injector + charging cable
* Two ethernet cables

Two computers

* One Toughbook for routing (Rocky, Sally, or Happy #2. Happy #1 cannot route due to its broken ethernet port!!!)
* One other laptop for running the Dragonfly server (Mac or Linux only. Rocky does not have Ubuntu installed, and Sally has issues!!!!!!)

One Toughbook for routing (Rocky, Sally, or Happy #2. Happy #1 cannot route due to its broken ethernet port!!!)

One other laptop for running the Dragonfly server (Mac or Linux only. Rocky does not have Ubuntu installed, and Sally has issues!!!!!!)

One wireless access point

One PoE injector + charging cable

Two ethernet cables

Instructions:

* Car sideTurn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Turn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Turn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Equivalently, run a vehicle computer board and attach a wireless access point to it
* Router computer

Car side

* Turn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Turn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Equivalently, run a vehicle computer board and attach a wireless access point to it

* Turn on the solar carEquivalently, run a vehicle computer board and attach a wireless access point to it
* Equivalently, run a vehicle computer board and attach a wireless access point to it

Turn on the solar car

* Equivalently, run a vehicle computer board and attach a wireless access point to it

Equivalently, run a vehicle computer board and attach a wireless access point to it

Router computer

* Get a toughbook (booted into Windows) and attach a second wireless access point to it over ethernet. You may need a PoE (power over ethernet) injector.Make sure that the router computer is connected to the car's wifi network (this is the only computer connected to the car's wifi network).Run python forward.py, which is located at routing/forward.py in the Dragonfly repoBasically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.
* Get a toughbook (booted into Windows) and attach a second wireless access point to it over ethernet. You may need a PoE (power over ethernet) injector.
* Make sure that the router computer is connected to the car's wifi network (this is the only computer connected to the car's wifi network).
* Run python forward.py, which is located at routing/forward.py in the Dragonfly repoBasically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.
* Basically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.

* Get a toughbook (booted into Windows) and attach a second wireless access point to it over ethernet. You may need a PoE (power over ethernet) injector.
* Make sure that the router computer is connected to the car's wifi network (this is the only computer connected to the car's wifi network).
* Run python forward.py, which is located at routing/forward.py in the Dragonfly repoBasically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.
* Basically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.

Get a toughbook (booted into Windows) and attach a second wireless access point to it over ethernet. You may need a PoE (power over ethernet) injector.

Make sure that the router computer is connected to the car's wifi network (this is the only computer connected to the car's wifi network).

Run python forward.py, which is located at routing/forward.py in the Dragonfly repo

* Basically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.

Basically, what the script does is read all packets coming in on port 33333 and broadcast all packets on port 22222.

* Server computer

Server computer

* Get a second computer that can run Dragonfly telemetry (does not need to be a toughbook).If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.The Ubuntu computer can now receive packets from the access point.Configure the telemetry server to read on port 22222 (check telemetry_config.ini to choose the listening port)If you don't need the router computer, configure the port to 33333.Connect the server computer to the toughbook's wifi network.Run the Dragonfly telemetry server as usual:source venv/bin/activate # activate the virtual environmentinvoke run_ui # run the front end servertelemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the databasetelemetry carlogger # run the car logger to log, parse, and write packets to the databaseObtain the ip address of the server computer via the command ifconfig
* Get a second computer that can run Dragonfly telemetry (does not need to be a toughbook).If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.The Ubuntu computer can now receive packets from the access point.
* If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.
* Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.
* Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.
* The Ubuntu computer can now receive packets from the access point.
* Configure the telemetry server to read on port 22222 (check telemetry_config.ini to choose the listening port)If you don't need the router computer, configure the port to 33333.
* If you don't need the router computer, configure the port to 33333.
* Connect the server computer to the toughbook's wifi network.
* Run the Dragonfly telemetry server as usual:source venv/bin/activate # activate the virtual environmentinvoke run_ui # run the front end servertelemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the databasetelemetry carlogger # run the car logger to log, parse, and write packets to the database
* source venv/bin/activate # activate the virtual environment
* invoke run_ui # run the front end server
* telemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the database
* telemetry carlogger # run the car logger to log, parse, and write packets to the database
* Obtain the ip address of the server computer via the command ifconfig

* Get a second computer that can run Dragonfly telemetry (does not need to be a toughbook).If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.The Ubuntu computer can now receive packets from the access point.
* If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.
* Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.
* Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.
* The Ubuntu computer can now receive packets from the access point.
* Configure the telemetry server to read on port 22222 (check telemetry_config.ini to choose the listening port)If you don't need the router computer, configure the port to 33333.
* If you don't need the router computer, configure the port to 33333.
* Connect the server computer to the toughbook's wifi network.
* Run the Dragonfly telemetry server as usual:source venv/bin/activate # activate the virtual environmentinvoke run_ui # run the front end servertelemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the databasetelemetry carlogger # run the car logger to log, parse, and write packets to the database
* source venv/bin/activate # activate the virtual environment
* invoke run_ui # run the front end server
* telemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the database
* telemetry carlogger # run the car logger to log, parse, and write packets to the database
* Obtain the ip address of the server computer via the command ifconfig

Get a second computer that can run Dragonfly telemetry (does not need to be a toughbook).

* If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.
* Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.
* Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.
* The Ubuntu computer can now receive packets from the access point.

If this second computer is running on Ubuntu, go to the WiFi menu and hit edit connections. Then edit the connection for the toughbook's wifi network.

Go to the IPv4 settings tab, and change the method from automatic to manual. Otherwise, the ubuntu laptop will not be able to communicate properly with the access point.

Set the address to the same IP address as the WiFi router, except with the last set of 8 bits different (i.e if 192.168.10.42, change the 42 to something else). Set the netmask to 255.255.255.0 and the gateway to 0.0.0.0.

The Ubuntu computer can now receive packets from the access point.

Configure the telemetry server to read on port 22222 (check telemetry_config.ini to choose the listening port)

* If you don't need the router computer, configure the port to 33333.

If you don't need the router computer, configure the port to 33333.

Connect the server computer to the toughbook's wifi network.

Run the Dragonfly telemetry server as usual:

* source venv/bin/activate # activate the virtual environment
* invoke run_ui # run the front end server
* telemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the database
* telemetry carlogger # run the car logger to log, parse, and write packets to the database

source venv/bin/activate # activate the virtual environment

invoke run_ui # run the front end server

telemetry apiserver --db sqlite:///<db_name> # run the api server which reads from the database

telemetry carlogger # run the car logger to log, parse, and write packets to the database

Obtain the ip address of the server computer via the command ifconfig

* Other computers who want to view the server

Other computers who want to view the server

* Connect other computers to the toughbook's wifi network. The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)The api server will be run at <ip address>:8000 (for querying raw data)
* Connect other computers to the toughbook's wifi network. The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)The api server will be run at <ip address>:8000 (for querying raw data)
* The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)
* The api server will be run at <ip address>:8000 (for querying raw data)

* Connect other computers to the toughbook's wifi network. The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)The api server will be run at <ip address>:8000 (for querying raw data)
* The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)
* The api server will be run at <ip address>:8000 (for querying raw data)

Connect other computers to the toughbook's wifi network. 

* The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)
* The api server will be run at <ip address>:8000 (for querying raw data)

The telemetry server will be run at <ip address>:8080/dashboard (for viewing charts)

The api server will be run at <ip address>:8000 (for querying raw data)

Debugging

* On the toughbook, try switching from Linux to Windows (or vice versa).Run Wireshark to check that the car is actually sending packets, or that the router computer is actually sending packetsMake sure that the computers are connected to the correct networksSometimes, you might have multiple versions of the api server running, which can lead to strange data readings. In a terminal, type ps aux | grep telemetry which will show all instances of telemetry applications running. Then, manually kill applications using kill -9 <PID>.
* On the toughbook, try switching from Linux to Windows (or vice versa).
* Run Wireshark to check that the car is actually sending packets, or that the router computer is actually sending packets
* Make sure that the computers are connected to the correct networks
* Sometimes, you might have multiple versions of the api server running, which can lead to strange data readings. In a terminal, type ps aux | grep telemetry which will show all instances of telemetry applications running. Then, manually kill applications using kill -9 <PID>.

* On the toughbook, try switching from Linux to Windows (or vice versa).
* Run Wireshark to check that the car is actually sending packets, or that the router computer is actually sending packets
* Make sure that the computers are connected to the correct networks
* Sometimes, you might have multiple versions of the api server running, which can lead to strange data readings. In a terminal, type ps aux | grep telemetry which will show all instances of telemetry applications running. Then, manually kill applications using kill -9 <PID>.

On the toughbook, try switching from Linux to Windows (or vice versa).

Run Wireshark to check that the car is actually sending packets, or that the router computer is actually sending packets

Make sure that the computers are connected to the correct networks

Sometimes, you might have multiple versions of the api server running, which can lead to strange data readings. In a terminal, type ps aux | grep telemetry which will show all instances of telemetry applications running. Then, manually kill applications using kill -9 <PID>.

More Information

* http://sscp.github.io/Dragonfly/
* https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/wifi-infrastructure

http://sscp.github.io/Dragonfly/

[http://sscp.github.io/Dragonfly/](http://sscp.github.io/Dragonfly/)

https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/wifi-infrastructure

[https://sites.google.com/a/stanfordsolarcar.com/sscp/home/sscp-2016-2017/code-2016-2017/documentation-resources/wifi-infrastructure](/home/sscp-2016-2017/code-2016-2017/documentation-resources/wifi-infrastructure)

