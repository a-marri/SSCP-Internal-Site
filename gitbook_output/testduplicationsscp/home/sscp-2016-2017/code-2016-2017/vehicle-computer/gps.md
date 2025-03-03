# SSCP - GPS

# GPS

Datasheet

[Datasheet](https://www.u-blox.com/sites/default/files/products/documents/EVA-M8M-FW3_DataSheet_%28UBX-16007405%29.pdf)

Currently, we communicate via USART1 to the gps chip. Note that when using the gps chip, the antenna must be uncovered and outside, as the gps link is fairly weak.

Old Notes

Working branch 'GPS', using the 'IMU' project from last cycle. We comment out the Real Time Clock Configuration (RTC_Config) function in main because it causes the project to hang. This might be a mistake.

Hardware: original versions of the schematic had the transmit (Tx) and receive (Rx) USART channels flipped. This was fixed in the newer boards but be careful in development. If in doubt, the F4 datasheet (page 55) lists the correct functions for pins A9 and A10. The two other pins are reset and pulse per second (pps).

[ F4 datasheet](http://www.st.com/content/ccc/resource/technical/document/datasheet/ef/92/76/6d/bb/c2/4f/f7/DM00037051.pdf/files/DM00037051.pdf/jcr:content/translations/en.DM00037051.pdf)

Config: The old boards were written under a different code structure. The setup for GPS is therefore in imu_bsp.c (board support package). This sets up the pin definitions as well as the EXTI and NVIC

Pin Change: the pins have been changed and so have their definitions in code. In addition the interrupt setup has changed. Instead of EXTernal Interrupt (EXTI) Interupt ReQuest (IRQ) 0, EXTI0_IRQn, we are going to switch to EXTI9_5_IRQn, Which handles pins 5-9 on any port (A-D). Their Alternate Function is also changed to USART6. See here

[ here](https://stm32f4-discovery.net/2014/08/stm32f4-external-interrupts-tutorial/)

Interrupts:

The Nested Vector Interrupt Controller (NVIC) is also set up. It is a meta config that tells the board which interrupts are more important. Again I changed this to USART 6 to deal with the change of pins.

USART: Parity, word length etc remain unchanged because the GPS module is the same.

The interrupt handler is in the interrupt file 'stm32fxx_it.c' we also changed all of those handlers to usart6, but the change might be more involved than that. Also note the file usbd_cdc_vsp.c also has many references to this USART port.

GPS TASK: It goes through set up and then enters xQueueReceive. My understanding is this function acts as semaphore. It tells FreeRTOS to exit the method until it is unlocked in the interrupt handler. However when I ran it, FreeRTOS never exited this function properly. Be sure to check that it does when running with other tasks.

Interrupt vs Polling: The set up of the gps is made more complicated by the interrupt. However that code is already set up and switching to polling will not simplify things greatly. There are many things that add to this complexity that I glossed over here like the NMEA message format, the USART setup, module registers, and the fact that gps does not work indoors (make sure the antenna is attached if you are expecting data). I would caution against moving to polling without a better understanding of the code.

[ NMEA message format](http://www.gpsinformation.org/dale/nmea.htm)

Good Luck and lmk if you have more questions.

