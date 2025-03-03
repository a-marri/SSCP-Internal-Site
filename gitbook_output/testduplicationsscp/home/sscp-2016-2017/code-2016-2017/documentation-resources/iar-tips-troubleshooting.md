# SSCP - IAR Tips & Troubleshooting

# IAR Tips & Troubleshooting

Tips

To make a copy of an existing project:

* Copy all project files to new folder.Remove workspace files from new folder (*.eww and ./settings/*.wsdt, NOT *.ewp.wsdt)Change all filenames in folder to new name (don't worry about things in "settings" folder).From IAR, create a new workspace (by exiting out of your current one), click project->add existing project, select the *.ewp file in the new project folder.Save workspace in new project folder.
* Copy all project files to new folder.
* Remove workspace files from new folder (*.eww and ./settings/*.wsdt, NOT *.ewp.wsdt)
* Change all filenames in folder to new name (don't worry about things in "settings" folder).
* From IAR, create a new workspace (by exiting out of your current one), click project->add existing project, select the *.ewp file in the new project folder.
* Save workspace in new project folder.

* Copy all project files to new folder.
* Remove workspace files from new folder (*.eww and ./settings/*.wsdt, NOT *.ewp.wsdt)
* Change all filenames in folder to new name (don't worry about things in "settings" folder).
* From IAR, create a new workspace (by exiting out of your current one), click project->add existing project, select the *.ewp file in the new project folder.
* Save workspace in new project folder.

Copy all project files to new folder.

Remove workspace files from new folder (*.eww and ./settings/*.wsdt, NOT *.ewp.wsdt)

Change all filenames in folder to new name (don't worry about things in "settings" folder).

From IAR, create a new workspace (by exiting out of your current one), click project->add existing project, select the *.ewp file in the new project folder.

Save workspace in new project folder.

If your variables aren't showing up in watch:

The compiler is probably optimizing them out. Go to project options -> C/C++compiler -> Optimizations -> Turn optimizations off.

Packing structs:

IAR uses a different keyword for struct packing than GCC.

[keyword ](http://netstorage.iar.com/SuppDB/Public/SUPPORT/005609/Example%205.pdf)

(If you don't know what struct packing is, don't worry about this)

If your printfs aren't showing up:

Make sure you have \n at the end of the line.  It won't flush it out otherwise.

Common Fixes

Before running any projects, make sure that the following is configured or set up:

* Debugger ConfigurationsIn the file menu, right click on the project name and go to options.In the Debugger category:In the Setup tab, check that the Driver is set to ST-LINK.In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.
* In the file menu, right click on the project name and go to options.
* In the Debugger category:In the Setup tab, check that the Driver is set to ST-LINK.In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.
* In the Setup tab, check that the Driver is set to ST-LINK.
* In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.
* Device connectionMake sure that the ST-LINK device is connected to the computer and the board.Also, make sure that the ST-LINK device has power.Power will be indicated by a glowing red light on the ST-LINK deviceMake sure that the pins for the connections are aligned. Some of the boards have marks indicating the orientation of connections; make sure you follow these marks.
* Make sure that the ST-LINK device is connected to the computer and the board.
* Also, make sure that the ST-LINK device has power.Power will be indicated by a glowing red light on the ST-LINK device
* Power will be indicated by a glowing red light on the ST-LINK device
* Make sure that the pins for the connections are aligned. Some of the boards have marks indicating the orientation of connections; make sure you follow these marks.
* Device driverIn Windows, search for the device manager and go to the other devices tab.Make sure that ST-link is a connected device. If it is not, you will need to install the driver for ST-link.
* In Windows, search for the device manager and go to the other devices tab.
* Make sure that ST-link is a connected device. If it is not, you will need to install the driver for ST-link.
* Using the STM processorWhen running a project using the STM processor, you may get a long list of inscrutable errors.Make sure that the processor for the project is set to the correct device:In the file menu, right click on the project name and go to options.In the General Options category, look at the Processor variant section.Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG
* When running a project using the STM processor, you may get a long list of inscrutable errors.
* Make sure that the processor for the project is set to the correct device:In the file menu, right click on the project name and go to options.In the General Options category, look at the Processor variant section.Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG
* In the file menu, right click on the project name and go to options.
* In the General Options category, look at the Processor variant section.
* Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG
* If your device is connected to the car, make sure the car is turned on.

Debugger Configurations

* In the file menu, right click on the project name and go to options.
* In the Debugger category:In the Setup tab, check that the Driver is set to ST-LINK.In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.
* In the Setup tab, check that the Driver is set to ST-LINK.
* In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.

In the file menu, right click on the project name and go to options.

In the Debugger category:

* In the Setup tab, check that the Driver is set to ST-LINK.
* In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.

In the Setup tab, check that the Driver is set to ST-LINK.

In the Download tab, check that the following elements are checked: "Verify Download" and "Use Flash Loader." Don't override the default .board file.

Device connection

* Make sure that the ST-LINK device is connected to the computer and the board.
* Also, make sure that the ST-LINK device has power.Power will be indicated by a glowing red light on the ST-LINK device
* Power will be indicated by a glowing red light on the ST-LINK device
* Make sure that the pins for the connections are aligned. Some of the boards have marks indicating the orientation of connections; make sure you follow these marks.

Make sure that the ST-LINK device is connected to the computer and the board.

Also, make sure that the ST-LINK device has power.

* Power will be indicated by a glowing red light on the ST-LINK device

Power will be indicated by a glowing red light on the ST-LINK device

Make sure that the pins for the connections are aligned. Some of the boards have marks indicating the orientation of connections; make sure you follow these marks.

Device driver

* In Windows, search for the device manager and go to the other devices tab.
* Make sure that ST-link is a connected device. If it is not, you will need to install the driver for ST-link.

In Windows, search for the device manager and go to the other devices tab.

Make sure that ST-link is a connected device. If it is not, you will need to install the driver for ST-link.

Using the STM processor

* When running a project using the STM processor, you may get a long list of inscrutable errors.
* Make sure that the processor for the project is set to the correct device:In the file menu, right click on the project name and go to options.In the General Options category, look at the Processor variant section.Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG
* In the file menu, right click on the project name and go to options.
* In the General Options category, look at the Processor variant section.
* Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG

When running a project using the STM processor, you may get a long list of inscrutable errors.

Make sure that the processor for the project is set to the correct device:

* In the file menu, right click on the project name and go to options.
* In the General Options category, look at the Processor variant section.
* Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG

In the file menu, right click on the project name and go to options.

In the General Options category, look at the Processor variant section.

Set the variant to Device and click on the side drop down menu. Choose ST -> ST32F407 -> ST32F407VG

If your device is connected to the car, make sure the car is turned on.

Common Errors

Error: Missing Files

* Try downloading the lib folder in addition to the project that you are working on. It will also probably be worth it to download all of the projects from software-micro.

Try downloading the lib folder in addition to the project that you are working on. It will also probably be worth it to download all of the projects from software-micro.

Error: Failed to load flash loader

* Click the project name then options and in ST-Link set reset to "normal"
* Your USB cable might not work, try another one

Click the project name then options and in ST-Link set reset to "normal"

Your USB cable might not work, try another one

Fatal Error: ST link, no MCU device

* Connection issue: try unplugging and replugging the cables. The problem might fix itself.
* You're working with two debugging sessions and the other did not close completely.
* Are you sure the connection isn't failing on other components of the car as well?
* The board itself might not working; try using a different board.
* Try reverting to a more recent copy of the code.
* Depending on the board you are using, you may have to change the interface from SWD to JTAG. Most of the boards in solar car use SWD, though:In the file menu, right click on the project name and go to options.In the ST-LINK category, change the interface from SWD to JTAG.
* In the file menu, right click on the project name and go to options.
* In the ST-LINK category, change the interface from SWD to JTAG.

Connection issue: try unplugging and replugging the cables. The problem might fix itself.

You're working with two debugging sessions and the other did not close completely.

Are you sure the connection isn't failing on other components of the car as well?

The board itself might not working; try using a different board.

Try reverting to a more recent copy of the code.

Depending on the board you are using, you may have to change the interface from SWD to JTAG. Most of the boards in solar car use SWD, though:

* In the file menu, right click on the project name and go to options.
* In the ST-LINK category, change the interface from SWD to JTAG.

In the file menu, right click on the project name and go to options.

In the ST-LINK category, change the interface from SWD to JTAG.

Fatal Error: ST link connection error

* Check the common fixes (above). 99% of the time the error will be fixed by those.

Check the common fixes (above). 99% of the time the error will be fixed by those.

License check failed: Found no license for ARM.EW.COMPILER

* You may need to download a slightly older version of IAR.
* Under c/c++ options make sure the directories for the pre processor are correct. Also make sure to have selected the correct preprocessor. (check a working project for help)

You may need to download a slightly older version of IAR.

Under c/c++ options make sure the directories for the pre processor are correct. Also make sure to have selected the correct preprocessor. (check a working project for help)

Error: cannot call intrinsic function "x" from y mode in this architecture

* Right click on Project -> Options -> General Options -> Target. Select 'Device' instead of 'Core', and choose the correct version.
* Right click on Project -> Options -> General Options -> Target. Select 'Device' instead of 'Core', and choose the correct version.

* Right click on Project -> Options -> General Options -> Target. Select 'Device' instead of 'Core', and choose the correct version.

Right click on Project -> Options -> General Options -> Target. Select 'Device' instead of 'Core', and choose the correct version.

Error[Pe1696]: cannot open any of the source files 

* Under c/c++ options make sure the directories for the pre processor are correct. Also make sure to have selected the correct preprocessor. (check a working project for help)
* Make sure that the license server is set up correctly.
* Make sure you're in release mode

Under c/c++ options make sure the directories for the pre processor are correct. Also make sure to have selected the correct preprocessor. (check a working project for help)

Make sure that the license server is set up correctly.

Make sure you're in release mode

Broken project options on startup + project files not found

* This has something to do with IAR backward compatibility. Try installing the latest version of IAR from FTP

This has something to do with IAR backward compatibility. Try installing the latest version of IAR from FTP

Code appears to run, but nothing happens on board

* You are in simulation mode
* Right click on root of project tree -> options -> debugger -> setup, change DRIVER field to "ST-LINK"
* Right click on root of project tree -> options -> debugger -> download, check "Verify download" and "Use flash loader(s)"

You are in simulation mode

Right click on root of project tree -> options -> debugger -> setup, change DRIVER field to "ST-LINK"

Right click on root of project tree -> options -> debugger -> download, check "Verify download" and "Use flash loader(s)"

When beginning to flash code, IAR appears to be stuck on the stage: Updating Build Tree.

* Also, when you halt debugging, IAR may mention being unable to connect to the license server.Check your internet connection to make sure that IAR has contact with the license server.
* Also, when you halt debugging, IAR may mention being unable to connect to the license server.
* Check your internet connection to make sure that IAR has contact with the license server.

* Also, when you halt debugging, IAR may mention being unable to connect to the license server.
* Check your internet connection to make sure that IAR has contact with the license server.

Also, when you halt debugging, IAR may mention being unable to connect to the license server.

Check your internet connection to make sure that IAR has contact with the license server.

Fatal error: Failed the search for probes, ensure that the USB drivers are installed.   Session aborted! 

* Make sure that the device is plugged in and turned on, as indicated by the red light.

Make sure that the device is plugged in and turned on, as indicated by the red light.

Code will not start when you power cycle:

* Make sure you have no calls to printf in your code. Calls to printf that go to IAR's terminal I/O cannot run outside of debug mode (unless you have written your own putchar).

Make sure you have no calls to printf in your code. Calls to printf that go to IAR's terminal I/O cannot run outside of debug mode (unless you have written your own putchar).

When you run code and get an error of the type: 

"Verify error at address 0x0........., target byte: 0x.., byte in file: 0x.."

* The computer isn't writing the program correctly to the board, so right click on the project and go to Options ->Debugger ->Download and make sure that the "Use flash loader(s)" box is checked.

The computer isn't writing the program correctly to the board, so right click on the project and go to Options ->Debugger ->Download and make sure that the "Use flash loader(s)" box is checked.

Please update this page to include any errors that people may encounter.

