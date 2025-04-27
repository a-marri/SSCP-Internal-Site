# tire-pressure-monitoring

## SSCP - Tire pressure monitoring

## Tire pressure monitoring

Nordic semiconductor nrf51 sample code for STM32: http://www.st.com/web/en/catalog/tools/PF260792

PDF

Code

We are trying to reverse engineer an off-the-shelf wireless tire pressure monitoring system (TPMS) so that we can integrate it into one of the boards on the car.  We are currently looking at the FOBO Bike system, which communicates over Bluetooth 4.0. This system is designed for bikes and motorcycles, but it is rated for 0-87psi, which is well within our tire's nominal pressure (\~45psi), so it should work well. The system is designed to communicate with an Android or iOS app.

[FOBO Bike](https://my-fobo.com/Product/FOBOBike)

Useful Information

FOBO Bike uses Bluetooth Low Energy (BLE), a.k.a. Bluetooth Smart. This tutorial describes reverse engineering a BLE light bulb and is relevant to what we're doing. There are several iOS apps that can connect to BLE devices and examine the GATT services they offer—LightBlue appears to work well. For Android, nRF Master Control Panel is quite nice.

[This tutorial](https://learn.adafruit.com/reverse-engineering-a-bluetooth-low-energy-light-bulb/overview)

[LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8)

We have downloaded and decompiled the FOBO Bike Android app. Here are Google Drive links to the app package and decompiled source code. There is a list of the names and UUIDs of all the characteristics provided by the pressure sensor in the decompiled source code. It's located at /src/com/fobo/bike/utils/FBBikeUUIDs.java. That list will probably be very useful in determining the meaning of data we receive from the sensors.

[app package](https://drive.google.com/file/d/0B9fQ5itW-jflcE03c1pyZGMtRFg5NU1aVVI5dUNSRWRBczl3/view?usp=sharing)

[decompiled source code](https://drive.google.com/file/d/0B9fQ5itW-jflMWNJT1podVRxZS1RcHNoYm5Xbk5LeU05aHFN/view?usp=sharing)

Android makes it possible to save all the Bluetooth packets sent/received by a device to a file, so hopefully we will be able to run the FOBO Bike app on an Android device and view the packets it is using to communicate with the sensors.

[makes it possible](http://stackoverflow.com/questions/23877761/sniffing-logging-your-own-android-bluetooth-traffic)

Here are instructions for emulating Android, including Bluetooth LE, on a desktop computer, which may allow us to view the packets that FOBO Bike is sending to/receiving from the pressure sensors. I have been able to get Android-x86 to run under Virtual Box and VMware Fusion, but I have only been able to get Bluetooth working using VMware, so I recommend using that (you can get a free license from the Software at Stanford store). However, using an actual Android device is easier and more flexible.

[instructions](http://chrislarson.me/blog/emulate-android-and-bluetooth-le-hardware.html)

[Software at Stanford store](http://web.stanford.edu/dept/its/cgi-bin/services/software/portal/)

Current Progress

We have the FOBOBike sensors. This can be registered to only one account and they are currently registered under windowsvm@stanfordsolarcar.com.  We have not found an easy way to promiscuously sniff Bluetooth packets so that we can see what packets the pressure sensors and app are sending between each other. There are devices like this one that would allow us to do that if necessary.

[windowsvm@stanfordsolarcar.com](mailto:windowsvm@stanfordsolarcar.com)

[this one](https://www.adafruit.com/product/2269)

Using Android's developer tools, we have successfully viewed the Bluetooth packets sent/received by a physical Android device communicating with a Bluetooth 4.0 (not LE) speaker. We'll try to do the same with the FOBO Bike sensors when they arrive.

Instructions for capturing Bluetooth packets sent/received by an Android device:

* First, install the Android SDK (this gives you access to Android Debug Bridge (adb), which lets you transfer files from an Android device or emulator to your computer). Plug the Android device into the computer via USB.
* On the Android device, look for Settings -> Developer options. If Developer options is not available, go to About phone and tap on Build number 7 times. Developer options should now be available. Under developer options, tap USB debugging to turn it on. When you are ready to start capturing Bluetooth packets, turn on Enable Bluetooth HCI snoop log. The Android device will immediately start keeping a log of all packets sent/received. When you are finished logging packets, uncheck Enable Bluetooth HCI snoop log. The log will be stored in a file on the Android device called btsnoop\_hci.log. The file is probably located in the directory /sdcard.
* Use adb to copy the file to your computer. adb is located in the platform-tools directory within the Android SDK folder; on Mac OS X, this is probably at /Users//Library/Android/sdk/platform-tools. Navigate into that directory and run adb in terminal as follows:

First, install the Android SDK (this gives you access to Android Debug Bridge (adb), which lets you transfer files from an Android device or emulator to your computer). Plug the Android device into the computer via USB.

On the Android device, look for Settings -> Developer options. If Developer options is not available, go to About phone and tap on Build number 7 times. Developer options should now be available. Under developer options, tap USB debugging to turn it on. When you are ready to start capturing Bluetooth packets, turn on Enable Bluetooth HCI snoop log. The Android device will immediately start keeping a log of all packets sent/received. When you are finished logging packets, uncheck Enable Bluetooth HCI snoop log. The log will be stored in a file on the Android device called btsnoop\_hci.log. The file is probably located in the directory /sdcard.

Use adb to copy the file to your computer. adb is located in the platform-tools directory within the Android SDK folder; on Mac OS X, this is probably at /Users//Library/Android/sdk/platform-tools. Navigate into that directory and run adb in terminal as follows:

./adb pull

In my case this looked like the following:

./adb pull /sdcard/btsnoop\_hci.log /Users/jackswiggett/Documents/Stanford/Solar\ Car/TPMS/device\_btsnoop/my\_btsnoop.log

* You should now have a my\_btsnoop.log file in the directory. You can open this file in Wireshark to get detailed information about all of the Bluetooth packets the Android device was sending/receiving.

You should now have a my\_btsnoop.log file in the directory. You can open this file in Wireshark to get detailed information about all of the Bluetooth packets the Android device was sending/receiving.

Sources: Sniffing/logging your own Android Bluetooth traffic. Using the ADB commands. Information about doing this with VMware here; I have tried this and it works but I'm not sure it is capturing all the packets.

[Sniffing/logging your own Android Bluetooth traffic](http://stackoverflow.com/questions/23877761/sniffing-logging-your-own-android-bluetooth-traffic)

[Using the ADB commands](http://www.droidviews.com/push-pull-files-android-using-adb-commands/)

[here](http://stackoverflow.com/questions/10648009/debugging-using-a-virtual-machine-like-vmware-virtualbox)

All the information below is related to our original attempt to reverse engineer a TireTech On system. The TireTech On monitoring system communicates with a handheld receiver at 433 MHz, but there are enough challenges reverse engineering that system that it may not be possible.

The instructions below are from here.

[here](http://www.rtl-sdr.com/receiving-decoding-tire-pressure-monitor-systems-using-rtl-sdr/)

First steps:

http://sdr.osmocom.org/trac/wiki/rtl-sdr#Buildingthesoftware

Download and build the software for the RTL2832U using the link above. If you have issues after installing the software, you may have to blacklist the kernel driver.

> sudo rmmod dvb\_usb\_rtl28xxu rtl2832&#x20;

A helpful GUI:

https://github.com/csete/gqrx

[https://github.com/csete/gqrx](https://github.com/csete/gqrx)

This gui lets you see radio frequencies from the RTL2832 device.

ATTEMPT 1:

Recording signals from TireTech monitor:

Resources on RTL2832U receiver:

http://sdr.osmocom.org/trac/wiki/rtl-sdr

[http://sdr.osmocom.org/trac/wiki/rtl-sdr](http://sdr.osmocom.org/trac/wiki/rtl-sdr)

https://github.com/steve-m/librtlsdr

[https://github.com/steve-m/librtlsdr](https://github.com/steve-m/librtlsdr)

Used the rtl-sdr command line tool from the librtlsdr repo linked to above, and the RTL2832U (black ezcap DVB-TFMDAB) hardware, captured signals.  This was done on a laptop running Ubuntu 14.04. &#x20;

Used this command:

> ./rtl\_sdr /tmp/capture.bin -s 1.8e6 -f 433.92e6

The tiretech pressure monitoring system that we uses broadcasts at 433.92MHz.

If you want to play radio signals just to see that you have things connected properly, use the below command (hip-hop station).

> rtl\_fm -f 95.7e6 -M wbfm -s 200000 -r 48000 - | aplay -r 48k -f S16\_LE

This one frequency yields pretty strong sine waves.  Import capture.bin as "raw data" into Audacity to see them.  If you use the gui program above, you'll see a big spike at this frequency.

> ./rtl\_sdr /tmp/capture.bin -s 1.8e6 -f 633.585e6

Converting the signals:

Now we need to convert these signals to a cfile with gnuradio. &#x20;

Decoding the signals:

Resources on decoding tire pressure signals:

http://www.rtl-sdr.com/receiving-decoding-tire-pressure-monitor-systems-using-rtl-sdr/

[http://www.rtl-sdr.com/receiving-decoding-tire-pressure-monitor-systems-using-rtl-sdr/](http://www.rtl-sdr.com/receiving-decoding-tire-pressure-monitor-systems-using-rtl-sdr/)

https://github.com/jboone/tpms/

[https://github.com/jboone/tpms/](https://github.com/jboone/tpms/)

DEAD END

ATTEMPT 2:

Record signals using the tool that this guy made.

[this guy](http://www.rtl-sdr.com/receiving-decoding-tire-pressure-monitor-systems-using-rtl-sdr/)

https://github.com/jboone/gr-tpms

[https://github.com/jboone/gr-tpms](https://github.com/jboone/gr-tpms)

It took awhile to resolve all of the dependencies.  After you Google around and install those, you may need to do this to add the right file to your path:

> export LD\_LIBRARY\_PATH=/usr/local/lib:$LD\_LIBRARY\_PATH

Now, the command line tool runs with instructions provided on the Github page:

> tpms\_rx --source rtlsdr --if-rate 400000 --tuned-frequency 315000000

Letting the above command run gets outputs like this, every minute or so:

> 20150321035752 fsk 9910 00111111001 diffman 1111101010110000010101010000011000011111001000001101000010010101101

These are likely from cars around VAIL.  Apparently all passenger cars in the United States make after 2008 must have tire pressure monitoring systems, and 315Mhz is the most common American frequency.

Here is is a raw output and the corresponding decoded output side-py-side

> 20150322015921 fsk 9910 00111111001 raw 0110011001011010010110010101010101101001011010010101010101100101010101100110011010011010101010100101011010101001010101100101010110011111001111100000110010001100100001000000100101110110001110110011101100100011000001110011001011100000011111010010100010001110

> 20150322015921 fsk 9910 00111111001 diffman 111110101011000001010101000001100001111101100000100100010001100011

For the tire pressure monitor sensor that we are using, however, the frequency is 433Mhz.  Running the command:

> tpms\_rx --source rtlsdr --if-rate 400000 --tuned-frequency 433000000

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1OIcp_ZkyIZkCjXT5njhXfJLsaF-ilnWk#list)
