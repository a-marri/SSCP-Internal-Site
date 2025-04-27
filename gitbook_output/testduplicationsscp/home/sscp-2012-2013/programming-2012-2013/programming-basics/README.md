# SSCP - Programming Basics

# Programming Basics

Hey guys,

This page is to give some direction to the people interested in code who will be at the meeting this Saturday (1/21/12).  If you won't be around for that meeting you should still make yourself familiar with all of the things discussed on this page.

Today you'll be playing around with a spare copy of driver controls and one of our handy Kent displays (two-color e-ink screen).  The goal is just to get you to be familiar with the ARMs and with Ride7, and give you a way to figure out what you need to learn.  You'll be working with the tritium side of driver controls, not the elmo side.  (Don't worry, they're labeled on the board.)

The files you need should be in SunbadSVN/software-micro/teaching projects/kent_display_teaching and tritium_controller_teaching

The information here is meant to give you jumping-off points for getting into programming our ARMs, not step-by-step instructions.  When you get stuck you should go hunt down a member of our code team and ask them for help.  It's often easier to show you how to do these things than it is to describe it.  I've also provided some references in programming basics/references.  

Step 1: POWER!!!!

So you've got this board.  How do you turn it on?  You have a few options.  

* You can plug it into the car with the Phoenix cables and run it off the main CAN bus.  This is good if you need to do debugging with real inputs that you can't simulate off the car.  It's less good when the mech team wants to take apart the motor and the pedals at the same time and needs you to not be moving things around while they're upside down in various parts of the car.  
* You can also use one of the power supplies on the electrical workbenches to power the board directly.  If you do this you can either provide 28V to the inputs of the power modules or you can provide logic voltage (usually 3.3V or 5V) to the outputs of the power modules.

You can plug it into the car with the Phoenix cables and run it off the main CAN bus.  This is good if you need to do debugging with real inputs that you can't simulate off the car.  It's less good when the mech team wants to take apart the motor and the pedals at the same time and needs you to not be moving things around while they're upside down in various parts of the car.  

You can also use one of the power supplies on the electrical workbenches to power the board directly.  If you do this you can either provide 28V to the inputs of the power modules or you can provide logic voltage (usually 3.3V or 5V) to the outputs of the power modules.

You should figure out how to do both of these.  Ask one of the electrical guys what you need to do to run the boards with a power supply.  You can't run driver controls that way unless you pull it out of the box, which is a pain.  You can do it with the kent display board.

Step 2: Programming

Now you have to actually program the board.  

* Open up your code project with Ride7 Open up the folder, go to RIDE, and double-click on the file with a .rprj extension
* Open up the folder, go to RIDE, and double-click on the file with a .rprj extension
* Grab a programmer and plug it in to your computer and the boardProgrammers are in the drawer labeled "programming."  It's the top drawer on the right hand side of the workbench closest to the mech room.There is a 20-pin programming header on the board.  Find the "1" that should be on the board (sillkscreen or sharpie) and the "1" on the RLink adapter.  Match them up and plug it in.  Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.
* Programmers are in the drawer labeled "programming."  It's the top drawer on the right hand side of the workbench closest to the mech room.
* There is a 20-pin programming header on the board.  Find the "1" that should be on the board (sillkscreen or sharpie) and the "1" on the RLink adapter.  Match them up and plug it in.  Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.
* Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.
* Start debugging in Ride7Go to the "Debug" menu and click "Start", or find the icon with a blue "play" button and a yellow bug and click on that.Ride7 will think for a while, pop up some windows, shut down those windows, and open a few new boxes inside the main window.  You'll probably see the "Debug" view on the left, the "Memory View" on the right, and the "Disassembly View" and "Debug Output" on the bottom.
* Go to the "Debug" menu and click "Start", or find the icon with a blue "play" button and a yellow bug and click on that.
* Ride7 will think for a while, pop up some windows, shut down those windows, and open a few new boxes inside the main window.  You'll probably see the "Debug" view on the left, the "Memory View" on the right, and the "Disassembly View" and "Debug Output" on the bottom.
* At the point your code is loaded onto the board but isn't actually running.  This lets you set breakpoints, etc. before you start running the program.
* To actually start running your program, find the green "Play" arrow at the top of the screen and click on it.

Open up your code project with Ride7 

* Open up the folder, go to RIDE, and double-click on the file with a .rprj extension

Open up the folder, go to RIDE, and double-click on the file with a .rprj extension

Grab a programmer and plug it in to your computer and the board

* Programmers are in the drawer labeled "programming."  It's the top drawer on the right hand side of the workbench closest to the mech room.
* There is a 20-pin programming header on the board.  Find the "1" that should be on the board (sillkscreen or sharpie) and the "1" on the RLink adapter.  Match them up and plug it in.  Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.
* Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.

Programmers are in the drawer labeled "programming."  It's the top drawer on the right hand side of the workbench closest to the mech room.

There is a 20-pin programming header on the board.  Find the "1" that should be on the board (sillkscreen or sharpie) and the "1" on the RLink adapter.  Match them up and plug it in.  

* Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.

Get in the habit of checking for that pin so you don't plug your programmer in backwards.  Otherwise you'll end up with some funny errors.

Start debugging in Ride7

* Go to the "Debug" menu and click "Start", or find the icon with a blue "play" button and a yellow bug and click on that.
* Ride7 will think for a while, pop up some windows, shut down those windows, and open a few new boxes inside the main window.  You'll probably see the "Debug" view on the left, the "Memory View" on the right, and the "Disassembly View" and "Debug Output" on the bottom.

Go to the "Debug" menu and click "Start", or find the icon with a blue "play" button and a yellow bug and click on that.

Ride7 will think for a while, pop up some windows, shut down those windows, and open a few new boxes inside the main window.  You'll probably see the "Debug" view on the left, the "Memory View" on the right, and the "Disassembly View" and "Debug Output" on the bottom.

At the point your code is loaded onto the board but isn't actually running.  This lets you set breakpoints, etc. before you start running the program.

To actually start running your program, find the green "Play" arrow at the top of the screen and click on it.

Step 3: Debugging

Okay, the program is running.  But it's not running properly.  How do I figure out what's going on?

Ride7 is really good for some types of debugging, and really bad for other stuff.  It's really good because it exposes all of the board's peripherals and settings to you in a useful way.  You can also set breakpoints and see if you hit them, and step through your code.  Breakpoints tend to work best if you set them when the program is paused or not yet running.  They do not work very well if you try to set them up while the program is actively running. 

One thing Ride7 often fails at is showing you actual values of your local variables.  Sometimes you can get around this by declaring them as globals, volatiles, or both.  Be warned.

You can examine peripherals by double-clicking on the ones that interest you in the "Debug" pane on the left and poking around in the box that pops up.  This will be more interesting when you actually have something you want to look at.  Oddly enough, it's also a good way to figure out what some of the acronyms used in the code mean.

For example, go open up "ADC1" or "ADC2".  ADC stands for "Analog-To-Digital Converter".  If you expand some of the menus and highlight items, the text at the bottom of the box will change to give you some information about these items.  For now it's probably still incomprehensible.  Don't worry about it.

Step 4: Play around

Figure out how to do the following:

* Turn on an LED when you press a button
* Toggle an LED using only the debugger
* Send messages to the light boards to make the headlights/brake lights/tail lights have different behaviours (turn them up or down/on or off depending on how long someone holds down a button, etc.)
* ........?

Turn on an LED when you press a button

Toggle an LED using only the debugger

Send messages to the light boards to make the headlights/brake lights/tail lights have different behaviours (turn them up or down/on or off depending on how long someone holds down a button, etc.)

........?

Well, that's about it for basics.  If you want a project that will let you fool around with boards on the car, check with JBo that the light boards are on the car and figure out how to make the turn signals auto-cancel (so if the driver turned on the right turn signal, turned right, and then turned back to center the right turn signal would automatically turn off.)  You'll have to figure out which microcontroller on the board should be sending those messages and what information the two micros will have to share to make that happen.  You shouldn't need to change code on the light boards themselves.

Another project: Take the Kent display and make it listen to the CAN messages from the battery pack and display them on the screen if one of the buttons was pressed.  Make different buttons display different useful information.

Program the light boards and the tritium side of driver controls to make the brake lights' brightness vary with how far the brake pedal is depressed.

