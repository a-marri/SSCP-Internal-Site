# nrf-radio

## SSCP - NRF Radio

## NRF Radio

Bring up power (skip if already verified in a previous step)

1. Power vehicle computer using power supply set to 12V.  Attach to 12V0\_Raw test point and any ground.  Set current limit to 50mA.
2. Turn on power supply and verify current is well below the limit and voltage is 11.95-12.05V.
3. Verify the 3.3V rail is powered and within 3.25-3.35V.

Verify basic transmission/receipt capabilities: send packets and receive via Arduino/discover board, then reverse

1. Power vehicle computer using power supply set to 12V.  Attach to 12V0\_Raw test point and any ground.  Set current limit to 1A. Turn on power supply.
2. Flash F4 with NRF transmit code using JTAG connector.
3. Using oscilloscope, verify NRF chip is transmitting to antenna by probing SMA connector.
4. Attach antenna to SMA connector.
5. Receive packets on Arduino/discover board, and verify packets are correct.
6. Flash F4 with NRF receive code using JTAG connector.
7. Transmit from Arduino/discover board and receive using vehicle computer.  Verify packets are correct.

Verify transmission/receipt of large packets: send large packets and receive via Arduino/discover board, then reverse

1. Power vehicle computer using power supply set to 12V.  Attach to 12V0\_Raw test point and any ground.  Set current limit to 1A. Turn on power supply.
2. Flash F4 with NRF transmit code (large packet version) using JTAG connector.
3. Receive packets on Arduino/discover board, and verify packets are correct.
4. Flash F4 with NRF receive code using JTAG connector.
5. Transmit from Arduino/discover board (large packets) and receive using vehicle computer.  Verify packets are correct.

Can also do the two above tests using another vehicle computer as transmitter/receiver instead of Arduino/discover board, provided some have already been validated.
