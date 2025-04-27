# libraries

## SSCP - Libraries

## Libraries

Catalog--documented under telemetry.

canrouter: Use this to set up CAN hardware on your board and manage incoming messages.  Here's Sasha's summary email:

What it does:

* Configures the CAN peripheral for you, including bit timing calculations based on the clock speed at time of configurationProvides an automatically managed, interrupt-driven transmit buffer. Now you can send more than three packets at a time!Subscription model for receiving packets. Ask to subscribe to any packet that matches a mask and an ID, provide a target receive queue, and it'll automagically drop matching packets into your buffer. All filtering is done in software, so any configuration of filters is possible.
* Configures the CAN peripheral for you, including bit timing calculations based on the clock speed at time of configuration
* Provides an automatically managed, interrupt-driven transmit buffer. Now you can send more than three packets at a time!
* Subscription model for receiving packets. Ask to subscribe to any packet that matches a mask and an ID, provide a target receive queue, and it'll automagically drop matching packets into your buffer. All filtering is done in software, so any configuration of filters is possible.
* Configures the CAN peripheral for you, including bit timing calculations based on the clock speed at time of configuration
* Provides an automatically managed, interrupt-driven transmit buffer. Now you can send more than three packets at a time!
* Subscription model for receiving packets. Ask to subscribe to any packet that matches a mask and an ID, provide a target receive queue, and it'll automagically drop matching packets into your buffer. All filtering is done in software, so any configuration of filters is possible.

Configures the CAN peripheral for you, including bit timing calculations based on the clock speed at time of configuration

Provides an automatically managed, interrupt-driven transmit buffer. Now you can send more than three packets at a time!

Subscription model for receiving packets. Ask to subscribe to any packet that matches a mask and an ID, provide a target receive queue, and it'll automagically drop matching packets into your buffer. All filtering is done in software, so any configuration of filters is possible.

Quick start checklist:

* \#include \<canrouter.h>Populate a Can struct as defined in canrouter.hConfigure your peripheral with CAN\_ConfigEnable at least one hardware filter with CAN\_InitHwFCall CAN\_TxIsr from your CAN transmit interrupt routinesCall CAN\_RxIsr from each of your two CAN receive interrupt routinesSubscribe to some interesting messages with CAN\_SubscribeSend messages with CAN\_Enqueue
* Populate a Can struct as defined in canrouter.h
* Configure your peripheral with CAN\_Config
* Enable at least one hardware filter with CAN\_InitHwF
* Call CAN\_TxIsr from your CAN transmit interrupt routines
* Call CAN\_RxIsr from each of your two CAN receive interrupt routines
* Subscribe to some interesting messages with CAN\_Subscribe
* Send messages with CAN\_Enqueue

\#include \<canrouter.h>

* Populate a Can struct as defined in canrouter.h
* Configure your peripheral with CAN\_Config
* Enable at least one hardware filter with CAN\_InitHwF
* Call CAN\_TxIsr from your CAN transmit interrupt routines
* Call CAN\_RxIsr from each of your two CAN receive interrupt routines
* Subscribe to some interesting messages with CAN\_Subscribe
* Send messages with CAN\_Enqueue

Populate a Can struct as defined in canrouter.h

Configure your peripheral with CAN\_Config

Enable at least one hardware filter with CAN\_InitHwF

Call CAN\_TxIsr from your CAN transmit interrupt routines

Call CAN\_RxIsr from each of your two CAN receive interrupt routines

Subscribe to some interesting messages with CAN\_Subscribe

Send messages with CAN\_Enqueue

Where to get it:

* Immediately available in SVN under software-micro\lib\drivers\canrouter.{c,h}

Immediately available in SVN under software-micro\lib\drivers\canrouter.{c,h}

Caveats:

* Remember that you must enable a hardware filter to receive any packets. I recommend two null filters, one for standard IDs and one for extended IDs.
* I may change the way you populate the Can structure to better encapsulate it and prevent higher level code from reaching down into canrouter's data.
* Software filtering consumes RAM and CPU time. We have powerful processors and so this likely won't matter, but don't go completely nuts and put in a thousand filters.

Remember that you must enable a hardware filter to receive any packets. I recommend two null filters, one for standard IDs and one for extended IDs.

I may change the way you populate the Can structure to better encapsulate it and prevent higher level code from reaching down into canrouter's data.

Software filtering consumes RAM and CPU time. We have powerful processors and so this likely won't matter, but don't go completely nuts and put in a thousand filters.

Code snippets:

Basic use of canrouter: set up hardware.  Do this by filling out a CAN struct with the relevant information.  For instance:

Can mainCan = {

&#x20;   .canPeriph = CAN1,

&#x20;   .clock = RCC\_APB1Periph\_CAN1,

&#x20;   .rccfunc = &(RCC\_APB1PeriphClockCmd),

&#x20;   .canTx = {

&#x20;       .port = GPIOD,

&#x20;       .pin = GPIO\_Pin\_1,

&#x20;       .pinsource = GPIO\_PinSource1,

&#x20;       .clock = RCC\_AHB1Periph\_GPIOD,

&#x20;       .rccfunc = &(RCC\_AHB1PeriphClockCmd),

&#x20;       .af = GPIO\_AF\_CAN1

&#x20;   },

&#x20;   .canRx = {

&#x20;       .port = GPIOD,

&#x20;       .pin = GPIO\_Pin\_0,

&#x20;       .pinsource = GPIO\_PinSource0,

&#x20;       .clock = RCC\_AHB1Periph\_GPIOD,

&#x20;       .rccfunc = &(RCC\_AHB1PeriphClockCmd),

&#x20;       .af = GPIO\_AF\_CAN1

&#x20;   },

&#x20;   .initialized = false,

&#x20;   .nextSubscriber = NULL,

};

Note that these pins and this CAN peripheral may not be correct for your device.  Check against the schematic to make sure that you are configuring the correct hardware.

Then call&#x20;

CAN\_Config(\&mainCan, 125000, 256);

where 125000 is the baud rate and 256 the size of the queue for incoming messages that this function will create.

and

CAN\_InitHwF(\&mainCan, 0x0, 0x0, 1, 0);

which will set up a hardware filter to allow all ExtId messages through.  (This is obviously for the simple use case.  You can set up other filters as you wish.)

You also need to subscribe yourself to all catalog messages that are aimed at your device, but you need to do that after the call to catInitializeCatalog (this is where the CatalogRxQueue is initialized.  Rachel will probably clean up this dependency eventually):

CAN\_Subscribe(\&mainCan, CAT\_IDMASK\_DEVID, DEVICE\_ID << CAT\_IDSHIFT\_DEVID, true, CatalogRxQueue);

and if you expect to respond to CAN messages sent from other devices, you will need to set up a filter to catch other messages as well.  This sets up a filter to put all extended ID messages into a queue called the CanRxQueue; you will probably want a more restrictive filter.

CAN\_Subscribe(\&mainCan, 0x0, 0x0, true, CanRxQueue);

Call the canrouter interrupt handlers from the CAN interrupts. Note that the names vary by processor type; F3 and F4 are different. Here's the code for an F4:

void CAN1\_RX0\_IRQHandler(void){

&#x20;   CAN\_RxIsr(\&mainCan, CAN\_FIFO0);

}

void CAN1\_TX\_IRQHandler(void){

&#x20;   CAN\_TxIsr(\&mainCan);

}

If you copy these code snippets into your project and have compiler errors, make sure you've updated your lib folder and that you have declared everything that is being referenced: mainCan, DEVICE\_ID, CatalogRxQueue, and CanRxQueue.
