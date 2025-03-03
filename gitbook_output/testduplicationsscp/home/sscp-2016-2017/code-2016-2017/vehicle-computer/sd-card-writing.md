# SSCP - SD Card Writing

# SD Card Writing

The IMU Board in Luminos and Arctan was not able to write all the data seen by the STM32 to its SD card.  This data included raw can packets (file 1) being sent between all the boards (including MPPT and tritium data) as well as detailed gps data (file 2) and barometer data (file 3) from hardware on the IMU board.

Goal:

Gawan believes that Arctan generates 1800 packets/sec.  A packet is 27 bytes.  27 * 1800 = 48,600 bytes 

 50 Kilobytes/sec.  We can connect laptop to Arctan with ethernet cable and use Wireshark to get exact number.

**We want to write data faster than 50kb/sec; preferably much faster so SD writing can handle a data-intensive catalog on the new ethernet network.**

Code:

The code from Luminos/Arctan writes 512 bytes at a time to the SD card at a time.  The current code uses a fat-filesystem implementation for embedded systems written by ChaN, which communicates with an SD library from (?somewhere on the internet) which in tern communicates with ST's libraries for the stm32.  

[ ChaN](http://elm-chan.org/fsw/ff/00index_e.html)

Code snippet from highest level in this hierarchy.

[Code snippet from highest level in this hierarchy](https://github.com/sscp/sundae-micro/blob/master/software-micro/imu_2-x/src/main.c#L254)

The pin definition is in https://github.com/sscp/sundae-micro/blob/master/imu_2-x/src/sdio_stm32f4.c#L206

Should be able to move production to a discovery board and off the IMU.

How to accomplish with code:

1. Just write code in larger chunks

    - There is overhead for each write.  So, writing 512 bytes twice takes more time than writing 1024 bytes once.

    - We want to accomplish this without external RAM; hopefully by using the internal RAM of the stm32

2. Don't use a filesystem like FATfs.

    - FATfs allows us to take the SD card out of the board, plug it into a computer, and read files directly.  However, maintaining data on a filesystem takes overhead.

    - If we just write raw bytes to the disk, we may be able to write faster.  This would require us to write an additional data extraction/parsing tool to get the data off of the SD card, onto a laptop, in a usable form.

3. Write less data.  Only write data that we really need.

How to accomplish, possible hardware additions:

1. Get better SD card?  Maybe we don't have the fastest hardware?

2. Add some kind of external memory to chip to allow more buffering of more data.

    - Only necessary if we determine that 

            1) bigger-chunk-writing will indeed increase write speed

            2) STM32 internal memory is too small for buffering

~First steps~:

Try to write code in larger chunks (How to Accomplish with code #1) by increasing write chunk size in code to more than 512 bytes.

Run imu code on Arctan or Luminos IMU and add items to SD card write buffer at 50 KB/s.

(So you'd have two tasks, one adding to queue and one removing from queue and writing to SD card.)

See if data is being written fast enough by:

    Making sure queue does not get clogged (add to buffer step fails because queue is not being unloaded by SD writing fast enough).

    Making sure all written data is correctly transferred to output chip (use micro-SD card reader in code drawer to be able to view micro-SD card on computer with SD card slot)

![](../../../../../assets/image_48de49a0d4.png)

