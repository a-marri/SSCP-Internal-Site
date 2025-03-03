# SSCP - References

# References

There are a bunch of files and folders that I use frequently as references while programming.  We use SVN to keep track of our files, so rather than attaching them here I'm going to tell you where they are and what they are.  You'll have to have SVN access to get at these files, so get on that soon.

All of these will be under SunbadSVN/software-micro/Teaching projects/References

* STM32F10xxx_reference_manual.pdf: this is the comprehensive manual for our set of processors.  You can look into this for information about peripherals and definitions of registers.  It's very dense.STM32F103x46_datasheet.pdf and STM32F105-107_datasheet.pdf: These are datasheets for specific processors that we use.You can look at the top of the micro to figure out which one you needWe use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another functionYou can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.STM32Lib-v340: Sample code!  This folder is great.  I spent a lot of time with this folder when I was learning how to program the ARMs.  You could say we're good friends nowInside you'll find "Libraries" and "Project""Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition""Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* STM32F10xxx_reference_manual.pdf: this is the comprehensive manual for our set of processors.  You can look into this for information about peripherals and definitions of registers.  It's very dense.
* STM32F103x46_datasheet.pdf and STM32F105-107_datasheet.pdf: These are datasheets for specific processors that we use.You can look at the top of the micro to figure out which one you needWe use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another functionYou can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* You can look at the top of the micro to figure out which one you need
* We use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.
* These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.
* After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.
* Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.
* Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* You can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* STM32Lib-v340: Sample code!  This folder is great.  I spent a lot of time with this folder when I was learning how to program the ARMs.  You could say we're good friends nowInside you'll find "Libraries" and "Project""Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition""Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* Inside you'll find "Libraries" and "Project"
* "Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files.
* "Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* For instance, you could go to "GPIO" and look at the files in "IOToggle"

* STM32F10xxx_reference_manual.pdf: this is the comprehensive manual for our set of processors.  You can look into this for information about peripherals and definitions of registers.  It's very dense.
* STM32F103x46_datasheet.pdf and STM32F105-107_datasheet.pdf: These are datasheets for specific processors that we use.You can look at the top of the micro to figure out which one you needWe use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another functionYou can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* You can look at the top of the micro to figure out which one you need
* We use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.
* These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.
* After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.
* Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.
* Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* You can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* STM32Lib-v340: Sample code!  This folder is great.  I spent a lot of time with this folder when I was learning how to program the ARMs.  You could say we're good friends nowInside you'll find "Libraries" and "Project""Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition""Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* Inside you'll find "Libraries" and "Project"
* "Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files.
* "Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* For instance, you could go to "GPIO" and look at the files in "IOToggle"

STM32F10xxx_reference_manual.pdf: this is the comprehensive manual for our set of processors.  You can look into this for information about peripherals and definitions of registers.  It's very dense.

STM32F103x46_datasheet.pdf and STM32F105-107_datasheet.pdf: These are datasheets for specific processors that we use.

* You can look at the top of the micro to figure out which one you need
* We use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.
* These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.
* After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.
* Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.
* Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function
* You can also find these datasheets from Ride7Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.
* Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.

You can look at the top of the micro to figure out which one you need

We use different processors depending on how powerful we need the boards to be.  For instance, the 107 has two CAN lines instead of one.  Both sides of driver controls have two CAN lines running to them, so both driver controls processors are 107s.

These datasheets are useful for figuring out which mode a given GPIO (General Purpose Input/Output) will be in.  

* There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.
* After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.
* Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.
* Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function

There is a table of "pin definitions".  This lists pin numbers, names, and functions.  You'll mostly be concerned with ones of the form P[A-E][number].  These are the GPIOs that you can play around with.

After reset a pin can be an input or an output.  It can be floating or have a pull-up or a pull-down resistor on the line.

Some pins have alternate functions.  Some can be used for analog to digital conversion (ADC); others can act as timers or communications lines for various protocols (including CAN).  When you configure a pin in config.c you can tell it to act as an alternate function.

Pins can have even more alternate functions!  If you really need more breathing room or need to use different peripherals, you can remap a pin to have it work as another function

You can also find these datasheets from Ride7

* Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.

Open up a project (any project--Ride7 will always have these), go to the "Help" menu at the top, and click "View Documentation".  A pane will open on the right side of the screen with a whole ton of PDFs.  You can ignore most of them; look for Ride7 Documentation-->Ride7 for ARM --> Datasheets.

STM32Lib-v340: Sample code!  This folder is great.  I spent a lot of time with this folder when I was learning how to program the ARMs.  You could say we're good friends now

* Inside you'll find "Libraries" and "Project"
* "Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source)."Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files."Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files.
* "Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* "Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheralFor instance, you could go to "GPIO" and look at the files in "IOToggle"
* For instance, you could go to "GPIO" and look at the files in "IOToggle"

Inside you'll find "Libraries" and "Project"

"Libraries" has the actual library code.  Click inside it and go down another level and you'll find two folders: "inc" (include) and "src" (source).

* "Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files.
* "Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implementedYou can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"
* You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"

"Inc" has all of the headers for the libraries.  There is a header file for every peripheral.  A lot of structs that we use in config are described in these files.

"Src" has all of the source for the same libraries.  If you want information about a given function and its arguments you can dive into these and look at the comments for that function.  You can also see how they are actually implemented

* You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"

You can also usually get to a function by right-clicking on it in Ride7 and clicking on "Go To Definition"

"Projects" has sample code for a lot of applications.  Ignore the templates folder for now and look in the examples folder instead.  You can see a bunch of folders--again, one for each peripheral.  These have sample code for doing a pretty wide variety of actions with the peripherals.  You can check these out if you're confused about how to use or configure a peripheral

* For instance, you could go to "GPIO" and look at the files in "IOToggle"

For instance, you could go to "GPIO" and look at the files in "IOToggle"

Sweet.  These are references.  I'm not going to try to describe everything in them.  If you want more information, go poke around.  If you don't understand what an acronym means (it happens a lot), come as one of us or google it.  You can also look around in SunflowerSVN/software-micro and ApogeeSVN/software-micro to look for examples of code using a given peripheral.  

They work best if you play them off against each other--look at a pin definition in the datasheet for a particular chip; look at that part of the programming manual to try to figure out what that peripheral does; google for a bit if there are terms that you don't understand; check out the sample code and read the readme files; go back to the programming manual to look up more terms, etc.

Other references that you will not find in the SVN: 

* Sam D'AmicoBryant TanGreg HallJohn BolanderAlice CheMarvin...Marvin.
* Sam D'Amico
* Bryant Tan
* Greg Hall
* John Bolander
* Alice Che
* Marvin...Marvin.

* Sam D'Amico
* Bryant Tan
* Greg Hall
* John Bolander
* Alice Che
* Marvin...Marvin.

Sam D'Amico

Bryant Tan

Greg Hall

John Bolander

Alice Che

Marvin...Marvin.

[](https://drive.google.com/folderview?id=160E7iZndGsbxHXZfwMW-njo9TOIjHfRM)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=160E7iZndGsbxHXZfwMW-njo9TOIjHfRM#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=160E7iZndGsbxHXZfwMW-njo9TOIjHfRM#list" frameborder="0"></iframe>

