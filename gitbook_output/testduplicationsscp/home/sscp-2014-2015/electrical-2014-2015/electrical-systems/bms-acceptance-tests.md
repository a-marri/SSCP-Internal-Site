# bms-acceptance-tests

## SSCP - BMS Acceptance Tests

## BMS Acceptance Tests

✓ Precharge into short, low resistance - precharge fail tone after 10 seconds

✓ Turn on and off as rapidly as possible - low side contactor FET gets uncomfortably hot \[increased drive strength from 10k resistor to 1k resistor]

✓ 24V bus overcurrent protection activates at 3.75A +/- 0.25A - activates at \~3.65A, does not turn back on without power cycling

✓ Turn on 24V bus into short - bus never turns on, still turns on after power cycle with short removed

✓ Test software shunt current limits - triggered as expected \[NOTE possibility of test induced errors here - BMS samples faster than the constant current loop in the power supply can regulate

✓ Push power into motor controller bus while at high voltage/low voltage - confirmed avoids false alarms and catches real alarms

✓ Probe high voltage sense buffer, agrees? - agrees to better than 0.1% after buffer

✓ Do not start at high and low voltage - overcharged won't start; undercharged contactors close and then permakill \~1s later

✓ Remove ring terminal for low side contactor sense - doesn't precharge until reconnected \[FEATURE REQUEST: buzz in this case]

✓ Unplug sense connectors - won't precharge, hard fault

✓ Unplug pack connectors  - won't start, turns off if on

Open contactor while driving current - no ill effects to contactor or FET after breaking 10A

✓ Add cap to 24v bus - charged 1 mF cap 10 times, the final time immediately followed by a dead short, without incident; started into 3A load

Supercap charge current - \[will lower charge resistor value to 4.99k to charge at 1 mA in next build]

Power with can debugger

Rapidly unplug steering wheel

✓ Turn car on and off over and over (complete cycles up to 24V bus enable)- OK if nominal

Bleed current - Flir confirmed

✓ Max temperature on board - \~39°C in LTC3639 5V supply and LTC4218 hot swap controller area at high 24V bus load

Unplug thermistors - \[TODO currently does not cause fault]

✓ ADCs value check - magnitude correct. sign correct.

\[POTENTIAL MITIGATED FAILURE MODE INHERENT IN DESIGN DISCOVERED]

Precharge can still bootstrap itself if nothing is connected. If the motor controllers have an intermittent connection and close after contactors have closed - BOOM. Not a real case though, because HVIL and high voltage conductors are in same connector and cannot mate/demate separately.
