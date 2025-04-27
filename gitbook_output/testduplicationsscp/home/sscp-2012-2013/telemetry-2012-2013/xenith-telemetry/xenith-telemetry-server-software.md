# xenith-telemetry-server-software

## SSCP - Xenith Telemetry Server Software

## Xenith Telemetry Server Software

The telemetry server is in Chase. During WSC, I (DC) used my Thinkpad as the telemetry server. The setup was functional but not pretty. Read Xenith Telemetry Network Topology first to see how things fit together.

* Check out the /xenith/software-pc and /website from SVNNote that if you are on a Mac, the rest significantly more complex, since Mac does not have apt. Come find Paul or DCSet up networking. See Xenith Telemetry Network Topology for details.
* Check out the /xenith/software-pc and /website from SVN
* Note that if you are on a Mac, the rest significantly more complex, since Mac does not have apt. Come find Paul or DC
* Set up networking. See Xenith Telemetry Network Topology for details.
* Check out the /xenith/software-pc and /website from SVN
* Note that if you are on a Mac, the rest significantly more complex, since Mac does not have apt. Come find Paul or DC
* Set up networking. See Xenith Telemetry Network Topology for details.

Check out the /xenith/software-pc and /website from SVN

Note that if you are on a Mac, the rest significantly more complex, since Mac does not have apt. Come find Paul or DC

Set up networking. See Xenith Telemetry Network Topology for details.

ifconfig&#x20;

## find which interface is Ethernet on the telemetry server, which should be connected to the Picostation, eg. en0

ifconfig en0 192.168.1.14 netmask 255.255.255.0

* Install packages, create and setup the telemetry database
* Install packages, create and setup the telemetry database
* Install packages, create and setup the telemetry database

Install packages, create and setup the telemetry database

cd /xenith/software-pc/telem2

./setup.sh

* Compile and run the telemetry software
* Compile and run the telemetry software
* Compile and run the telemetry software

Compile and run the telemetry software

cd /xenith/software-pc/telem2/C

make clean build

./logger --simple

* You should now see packets coming in. Periods (.) represent success, crosses (x) represent eg. checksum failure. Due to a hardware issue on the Xenith telemetry board, only about 80-90 % of the packets are going to be successful.If you see something like "0 measurements loaded" instead of "175 measurements loaded" (eg) on logger startup, go and check that the DB is properly initialized. See /xenith/software-pc/telem2/Protocol, ask Paul or DCInstall and run the telemetry web dashboard
* You should now see packets coming in. Periods (.) represent success, crosses (x) represent eg. checksum failure. Due to a hardware issue on the Xenith telemetry board, only about 80-90 % of the packets are going to be successful.
* If you see something like "0 measurements loaded" instead of "175 measurements loaded" (eg) on logger startup, go and check that the DB is properly initialized. See /xenith/software-pc/telem2/Protocol, ask Paul or DC
* Install and run the telemetry web dashboard
* You should now see packets coming in. Periods (.) represent success, crosses (x) represent eg. checksum failure. Due to a hardware issue on the Xenith telemetry board, only about 80-90 % of the packets are going to be successful.
* If you see something like "0 measurements loaded" instead of "175 measurements loaded" (eg) on logger startup, go and check that the DB is properly initialized. See /xenith/software-pc/telem2/Protocol, ask Paul or DC
* Install and run the telemetry web dashboard

You should now see packets coming in. Periods (.) represent success, crosses (x) represent eg. checksum failure. Due to a hardware issue on the Xenith telemetry board, only about 80-90 % of the packets are going to be successful.

If you see something like "0 measurements loaded" instead of "175 measurements loaded" (eg) on logger startup, go and check that the DB is properly initialized. See /xenith/software-pc/telem2/Protocol, ask Paul or DC

Install and run the telemetry web dashboard

cd /website/trunk/nodejs/telemweb

## install Node.JS and NPM if you haven't already&#x20;

./setup.sh

## on a Mac, run ./setup\_mac.sh instead

sudo node telemetry.js

## you need sudo to run on port 80, you don't to run on port 8000, read up on Unix networking to see why

## edit the top of telemetry.js (constants) to change between the two

* Set up your /etc/hosts file as described in Xenith Telemetry Network TopologyGo to http://chase/ and graph a few measurements (eg pack\_voltage and current), turn on Auto Update, zoom in.
* Set up your /etc/hosts file as described in Xenith Telemetry Network Topology
* Go to http://chase/ and graph a few measurements (eg pack\_voltage and current), turn on Auto Update, zoom in.
* Set up your /etc/hosts file as described in Xenith Telemetry Network Topology
* Go to http://chase/ and graph a few measurements (eg pack\_voltage and current), turn on Auto Update, zoom in.

Set up your /etc/hosts file as described in Xenith Telemetry Network Topology

Go to http://chase/ and graph a few measurements (eg pack\_voltage and current), turn on Auto Update, zoom in.

* Badass

Badass
