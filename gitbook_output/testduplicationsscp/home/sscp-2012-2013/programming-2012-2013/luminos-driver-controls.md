# SSCP - Luminos Driver Controls

# Luminos Driver Controls

Requirements:

Pedals:

1. Calibration function to get min and max values of pedals.

2. Deadzone the input so minor rattling does not trigger brakes/throttle.

Brakes:

1. The car brakes if both pedals are pressed.

2. Pressing the brake turns on all three rear red lights (brake lights).

3. The brake value varies from 0 at not pressed to -1 depressed to the point of the hydraulic brakes for the brake pedal, and stays at -1 for the entire range of the hydraulic brakes.

4. Unplugging the brakes should not result in full regen.

Throttle:

1. Coast if throttle input is well beyond maximum. Allow throttle once again if below maximum. Add hysterisis if needed.

Cruise:

4. Pressing cruise up turns on cruise control with the setpoint at the current speed, not previous setpoint. It should also clear the cruise control PID loop "I" term.

5. Pressing cruise down when not in cruise control does nothing (manual or manual reverse.

6. Do not allow cruise in reverse.

7. Pressing brake or pressing cruise down all the way to 0 should kick out of cruise. Cruise should not go below zero.

8. Throttle should work in cruise, but not change the set-point.

Implementation notes:

Tritium:

1. Tritium expects a motor velocity (rpm) and motor current. The motor current is a float that goes from [0.0, 1.0]

2. There are two modes of operation: torque control and velocity control.

We will be using torque control because the Tritium's velocity control is not very good. We have our own velocity control for cruise implemented as a PID loop.

3. To go forward, send the tritium an unobtainable velocity (100,000rpm) and a motor current. The motor current should be controlled by the throttle pedal.

4. To go backwards, send the tritium an unobtainable negative velocity (-100,000rpm) and a motor current, same as above.

5. To regen brake, send 0rpm and a motor current controlled by the brake pedal.

6. To brake without regen, send 0rpm and a motor current of 0.

The driver controls board, along with BMS, are the two boards that the car needs in order to drive.

