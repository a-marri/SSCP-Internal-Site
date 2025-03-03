# SSCP - STM32W development (Tire pressure sensing)

# STM32W development (Tire pressure sensing)

### Development board

[](#h.8sgn24e3d0z3)

-- Is there a FreeRTOS port for the STM32W? Not important

-- Do the demo boards transmit from the wheel fairing to the driver fairing on battery power? Yes

-- How do you make the board sleep? Done

-- Setup for 2 transmitters and one receiver. Done

-- Setup for 4 transmitters and two receivers (make sure there isn't crosstalk; make sure you always know which sender you're getting messages from.  How to identify?)

-- Write and complete a test plan for various physical environments

-- Make checksums work Done

intelligent power off

awake constantly until response_timeout>5mins

Then, go to deeper sleep. -> Wake up every 10 to check sender

Error states:

Sudden tire pressure change. Sender->Receiver, Receiver->CAN

Minimum tire pressure threshold/Maximum tire pressure threshold. Receiver->CAN

Low battery. Sender->Receiver, Receiver->CAN

No response from Sender -> CAN. No message received from Sender X for 6 mins.

5 min avg

sample rate 1 sec.

Deliverables

-- "wireless.c/h" files

* Send and receive functionsHardware initialization functions (only additional configuration needed should be any pins that are being connected)
* Send and receive functions
* Hardware initialization functions (only additional configuration needed should be any pins that are being connected)

* Send and receive functions
* Hardware initialization functions (only additional configuration needed should be any pins that are being connected)

Send and receive functions

Hardware initialization functions (only additional configuration needed should be any pins that are being connected)

-- FreeRTOS port (?)

-- Completed test plan

### Tire pressure board

[](#h.p7q7dyca26zh)

-- When should you sleep?

-- What is the hardware interface with the pressure sensors?

Deliverables

-- Tire pressure sensing!  (IAR projects for senders and receivers that can be configured for IDs)

____________________________

Sleep works--transmitter sends a packet every 5 minutes--should this be more or less frequent?  Sends a five minute average, checking values every 1 s and sleeping between checks.  Sends alerts if anything changes too much.  Sender does averaging. Done

Receiver W receives, storing average for each sender and alert status for each sender. Done

Need to communicate between receiver W and the f4.

Idea for deeper sleep:

Receiver F4 responds to a CAN message and sets a register in the W saying that the car is still not moving.

Transmitter W goes to deep sleep for X seconds, wakes up, checks if should go back to sleep.

Also monitor battery status? And send an alert when the battery is low.

Checklist:

What min transmit power?

What max transmit power?

What channel number? probably any will do. Maybe use ST_RadioChannelIsClear to get clear/busy status. Downside: unpredictable

When to sleep?

When to check for radio recalibration do to temperature?

Make sure radioTransmitConfig.appendCrc is true

Make sure to set correct node id, PAN id.

To encrypt or not to encrypt plaintext packets?(This chip has a hardware AES coprocessor)

ST_RadioEnableOverflowNotification to true

ST_RadioOverflowIsrCallback make to report overflow

ST_RadioEnableReceiveCrc What to do with packets that fail CRC?

A cool feature: ST_RadioGetRandomNumbers generates true random numbers using radio hardware

5 nodes.

4 senders and a 2 receivers.

Sender generates some data, calculates checksum. Sends data.

Receiver recieves data, calculates checksum.

Recieves sends checksum to sender.

Sender compares checksums and throws error if checksums don't match.

Repeat.

Checksums per packet (128 bytes).

Email from an ST engineer about this:

"Sounds good.   We were discussing that it would be better to use the ST modules.   Let me check with Jeff before I place the order.   He’s out today and all next week.  (He’ll be in Orlando at an IPSO meeting.)

 

The kit that you have has the SmartMAC which will allow you to transmits/receive frames.    The “Zigbee Pro”  stack is licensed (more expensive) and has an IP stack but also other stuff like Home Automation for sensors in the home etc.   I recommend having someone get familiar with the software that’s on the kit (as Jeff is) and do some experiments sending frames with incrementing sequence numbers (1, 2, 3, 4…) so at the receiver you can compute the number of frames received/frames transmitted.   I’m confident you will get signal through the tires (and probably everywhere outside the car thereafter), but I’m not too sure about your fairing and aluminum frame.    I think we need to do this “sanity check” early.

 

Probably the easiest thing to do would be to get the software debugged on the bench first…one radio talking to the other.   Then fix one radio to the top of one of the rear wheels, put the tire on, with radio antennas point up.   Then put the other radio on the chassis of the car and close the top.

 

Afterward, we can experiment with rotating the tires and the effect of the wheel being in the direct path, and we can order the modules in parallel."

