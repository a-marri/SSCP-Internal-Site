# black-box

## SSCP - Black Box

## Black Box

The black box board records all of the messages sent across the CAN (Controller Area Network) onto an SD card. &#x20;

Data is normally recorded by a laptop connected to the solar car's wifi network (telemetry server).  However, a laptop is not always recording data from the car while it is running.  Thus, when we want to retrieve car data that has not been captured by telemetry, we read it off of the SD card where it has been recorded by the Black Box.

Evaluation board

This is the board we've been using: http://www.digikey.com/product-detail/en/STM3240G-EVAL/497-11454-ND/2711744

[http://www.digikey.com/product-detail/en/STM3240G-EVAL/497-11454-ND/2711744](http://www.digikey.com/product-detail/en/STM3240G-EVAL/497-11454-ND/2711744)

Link to manual: http://www.st.com/web/en/resource/technical/document/user\_manual/DM00036746.pdf

[http://www.st.com/web/en/resource/technical/document/user\_manual/DM00036746.pdf](http://www.st.com/web/en/resource/technical/document/user_manual/DM00036746.pdf)

We're using the STM32F407IGH6 micro-controller. Datasheet here: http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00037051.pdf

[http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00037051.pdf](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00037051.pdf)

Running our starter code on F407IG

The startup\_stm32F4xx.s and system\_stm32F4xx.c files need to be copied from a working demo for the F407IG. &#x20;

The HSE clock for this chip, for instance, needs a different configuration than our other boards.  After getting the correct files, you may also need to edit defined symbols (rclick project->options->compiler and add HSE\_VALUE=25000000 to "defined symbols")

Include paths to use stm32cubef4 firmware

$PROJ\_DIR$

$PROJ\_DIR$..\inc\\

$PROJ\_DIR$..\src\\

$PROJ\_DIR$............\Drivers\STM32F4xx\_HAL\_Driver\inc\\

$PROJ\_DIR$............\Drivers\STM32F4xx\_HAL\_Driver\src\\

$PROJ\_DIR$............\Drivers\CMSIS\Device\ST\STM32F4xx\Include

$PROJ\_DIR$............\Drivers\CMSIS\Include\\

$PROJ\_DIR$............\Drivers\BSP\STM324xG\_EVAL

$PROJ\_DIR$............\Middlewares\Third\_Party\FatFs\src

$PROJ\_DIR$............\Middlewares\Third\_Party\FatFs\src\drivers

Notes

* Project is still named f4starter, though it is not actually the standard starter file anymore.&#x20;
* Project is still named f4starter, though it is not actually the standard starter file anymore.&#x20;
* Project is still named f4starter, though it is not actually the standard starter file anymore.&#x20;

Project is still named f4starter, though it is not actually the standard starter file anymore.&#x20;

* Code pushed on the repo is the version that compiles correctly with our starter code.&#x20;
* Code on the toughbook is an attempt to get it to compile with the eval board code, to get read/write of the sd card working. This code is not compiling. To get it to compile, we need to replace their code with our APIs:sd\_diskio.c - included from main. It depends on HAL\_SD\_CardInfoTypedef - should rewrite this structstm324xg\_eval\_sd.c/h - this code is specific to the eval board.Need to replace all their GPIO functions with our pin.h need to replace their BSP functions with our own BSP functionsReplace anything with HAL with our codeSo far those are the only 2 files throwing errorsTo do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package) Goals of projectSee how fast the board can read/write CAN messages. Compare this to how fast the car writes messagesIf board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* sd\_diskio.c - included from main. It depends on HAL\_SD\_CardInfoTypedef - should rewrite this struct
* stm324xg\_eval\_sd.c/h - this code is specific to the eval board.Need to replace all their GPIO functions with our pin.h need to replace their BSP functions with our own BSP functionsReplace anything with HAL with our codeSo far those are the only 2 files throwing errorsTo do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;
* Need to replace all their GPIO functions with our pin.h&#x20;
* need to replace their BSP functions with our own BSP functions
* Replace anything with HAL with our code
* So far those are the only 2 files throwing errors
* To do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;
* Goals of projectSee how fast the board can read/write CAN messages. Compare this to how fast the car writes messagesIf board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* See how fast the board can read/write CAN messages. Compare this to how fast the car writes messages
* If board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* Need roll own ram usage (the eval code doesn't have this built in, afaik)
* in system\_stm32f4xx.c - turn on extRam on line 96

Code pushed on the repo is the version that compiles correctly with our starter code.&#x20;

Code on the toughbook is an attempt to get it to compile with the eval board code, to get read/write of the sd card working. This code is not compiling. To get it to compile, we need to replace their code with our APIs:

* sd\_diskio.c - included from main. It depends on HAL\_SD\_CardInfoTypedef - should rewrite this struct
* stm324xg\_eval\_sd.c/h - this code is specific to the eval board.Need to replace all their GPIO functions with our pin.h need to replace their BSP functions with our own BSP functionsReplace anything with HAL with our codeSo far those are the only 2 files throwing errorsTo do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;
* Need to replace all their GPIO functions with our pin.h&#x20;
* need to replace their BSP functions with our own BSP functions
* Replace anything with HAL with our code
* So far those are the only 2 files throwing errors
* To do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;
* Goals of projectSee how fast the board can read/write CAN messages. Compare this to how fast the car writes messagesIf board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* See how fast the board can read/write CAN messages. Compare this to how fast the car writes messages
* If board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* Need roll own ram usage (the eval code doesn't have this built in, afaik)
* in system\_stm32f4xx.c - turn on extRam on line 96

sd\_diskio.c - included from main. It depends on HAL\_SD\_CardInfoTypedef - should rewrite this struct

stm324xg\_eval\_sd.c/h - this code is specific to the eval board.

* Need to replace all their GPIO functions with our pin.h&#x20;
* need to replace their BSP functions with our own BSP functions
* Replace anything with HAL with our code
* So far those are the only 2 files throwing errors
* To do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;

Need to replace all their GPIO functions with our pin.h&#x20;

need to replace their BSP functions with our own BSP functions

Replace anything with HAL with our code

So far those are the only 2 files throwing errors

To do this I've been comparing the old imu code to the STM32xG\_EVAL SD demo code (given with the stm32cubef4 code package)&#x20;

Goals of project

* See how fast the board can read/write CAN messages. Compare this to how fast the car writes messages
* If board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.Need roll own ram usage (the eval code doesn't have this built in, afaik)in system\_stm32f4xx.c - turn on extRam on line 96
* Need roll own ram usage (the eval code doesn't have this built in, afaik)
* in system\_stm32f4xx.c - turn on extRam on line 96

See how fast the board can read/write CAN messages. Compare this to how fast the car writes messages

If board is not fast enough, need to write to SD card in larger chunks. To store a large enough chunk, use RAM.

* Need roll own ram usage (the eval code doesn't have this built in, afaik)
* in system\_stm32f4xx.c - turn on extRam on line 96

Need roll own ram usage (the eval code doesn't have this built in, afaik)

in system\_stm32f4xx.c - turn on extRam on line 96

Writing to SD with FAT Filesys

We're using a FAT library for embedded devices written by ChaN (ff.c).  You'll see that his FAT project directory (in software-micro/lib/fatfs../) contains diskio.c, a template that allows you to fill in details for your specific processor.  The diskio.c SD implementation for STM32 we are using is in diskio\_sdio.c; is a layer over sdio\_stm32f4.c, which interacts directly with STM32 low-level functions.

[ChaN](http://elm-chan.org/fsw/ff/00index_e.html)

user -> ff.c -> diskio\_sdio.c -> sdio\_stm32f4.c -> low-level stm32 code.

Status:

1. Read and write bytes to sd card
2. Mount and create files in FATFS system
3. Write files to Fatfs
4. Record fake CAN messages

[CAN](https://www.google.com/webhp?sourceid=chrome-instant\&ion=1\&espv=2\&ie=UTF-8#q=can%20protocol)

5. Stress-test to recreate packet-drop problem(400 MPS?)
6. Buffer packets in ram and write in 512KB chunks

History

The imu board served as the black box in Luminos, recording CAN data to an SD card along with its various other tasks.  Unfortunately, it could not record all CAN packets accurately, its creators suspected that writing to SD in larger chunks would fix the problem.

\---------- Forwarded message ----------

From: Sasha Zbrozek [s.zbrozek@gmail.com](mailto:s.zbrozek@gmail.com)

[s.zbrozek@gmail.com](mailto:s.zbrozek@gmail.com)

Date: Wed, Feb 12, 2014 at 2:02 PM

Subject: Re: SD Card Logging?

To: Max Praglin [mpraglin@stanford.edu](mailto:mpraglin@stanford.edu)

[mpraglin@stanford.edu](mailto:mpraglin@stanford.edu)

Cc: Eric Thong [ethong@stanford.edu](mailto:ethong@stanford.edu), Harry Johnson [harrymj@stanford.edu](mailto:harrymj@stanford.edu), Jack Zhu [jackzhu@stanford.edu](mailto:jackzhu@stanford.edu)

[ethong@stanford.edu](mailto:ethong@stanford.edu)

[harrymj@stanford.edu](mailto:harrymj@stanford.edu)

[jackzhu@stanford.edu](mailto:jackzhu@stanford.edu)

It's a block size vs throughput problem. The SD card is _really_ fast if you write in large blocks (512KB to 4MB). I didn't have enough RAM to cache such large blocks prior to write, so the repeated overhead of starting and stopping writes was so large that it made my throughput too small. In particular, the latency jitter between filling a buffer and writing it out meant that I would often overrun my incoming buffer.

There are a number of solutions. The brute force one is to just add an external SRAM on the parallel port of the STM32F4 that's large (4-8 MB would be awesome). Alternatively, carefully crafting the RAM space and eliminating multiple levels of buffering (the write code has a buffer, fatfs has a buffer, the packet assembler has a buffer...) could get you up to a 32 or 64 KB block, which will probably be fast enough. But doing that would require significant re-plumbing of the FAT and SD paths, all of which is code I got from the intertubes and don't understand very well.

So for expediency's sake, I optimized the IMU's performance as a CAN-Ethernet bridge and let the SD logging suck. More work can make it better.

On Wed, Feb 12, 2014 at 1:48 PM, Max Praglin [mpraglin@stanford.edu](mailto:mpraglin@stanford.edu) wrote:

[mpraglin@stanford.edu](mailto:mpraglin@stanford.edu)

Hey Sasha,

Hopefully this is a quick question - could you explain the current problem with logging to the SD card on the IMU? My rough understanding from Australia (I only heard briefly) was that you ran into an issue with the SD card block size not fitting in the F4, but I don't understand why that would be the case.

Thanks!

Max
