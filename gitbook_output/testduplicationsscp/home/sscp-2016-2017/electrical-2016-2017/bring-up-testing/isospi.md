# isospi

## SSCP - isoSPI

## isoSPI

This test plan applies for both the isoSpi test coupon and the isoSpi portion of Vehicle Computer. For steering wheel, test slave mode only (do only steps 7 and 8 of the communication functionality test).

Board not shorted

1. Connect board to a power supply at +5V and GND terminals.
2. Set current limit to 20mA and voltage limit to +5V.
3. Turn on power supply. Verify current is well below the limit and 5V rail between 4.95 and 5.05V.

Power Rails Up

1. Using DMM, verify 5V rail between 4.95 and 5.05V.
2. Using DMM, verify 3.3V rail between 3.25 and 3.35V.
3. Verify continuity between test points of the same voltage level/all test points at correct voltage.
4. Turn off power supply, then power board via USB port. Check that 3.3V and 5V rails are within tolerance.

Spi loopback (without MCU)

1\.&#x20;

Spi loopback (with MCU)

1. Program MCU successfully with isoSpi master mode code.
2. Send SPI packets and use oscilloscope to verify MCU is transmitting.
3. Use logic analyzer and/or oscilloscope and/or oscilloscope to verify packets from MCU->LT6820 are correct.
4. Send packets between two isoSpi/Vehicle Computer boards: use jumpers to select the master code board as master and the slave code board as slave.  Then repeat with the roles reversed (unless testing steering wheel).
