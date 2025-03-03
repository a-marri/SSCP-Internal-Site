# SSCP - STM32 tips and tricks

# STM32 tips and tricks

## Peripherals

[](#h.scqoos7igtw6)

### GPIO

[](#h.bekbtdg1r1iz)

Physical pins on the chip package can go to a number of different places inside the chip. Right on the output is a multiplexer (mux) that selects where that pin connects. The general-purpose input-outputs (GPIO) pins on the processor are the most basic peripheral that you can connect pins to. You may use GPIOs to drive digital outputs or read digital inputs. Common use-cases include driving LEDs, MOSFETs, or reading switches.

There are several parameters to choose when configuring a GPIO pin:

* Mode: This field selects where the multiplexer closest to the pin connectsDigital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.Output type: This is only relevant when you've configured a GPIO as an output.Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.Speed: This is badly named. It's really a knob to adjust the slew rate of the output. Keep it set to the slowest speed you can tolerate and use an oscilloscope to verify the signal integrity. LEDs and relay drives should be set to 2MHz. Digital buses will require a little bit more science.Pull-up and pull-down: Open-drain lines require some leakage current to make sure their value is defined when the transistors are all off. Generally it's good practice to set pull-ups and pull-downs with real physical resistors, as all pins float on reset. This is very bad for pins with mission-critical states, like the contactor and precharge lines.No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.
* Mode: This field selects where the multiplexer closest to the pin connectsDigital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.
* Digital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.
* Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.
* Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.
* Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.
* Output type: This is only relevant when you've configured a GPIO as an output.Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.
* Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.
* Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.
* Speed: This is badly named. It's really a knob to adjust the slew rate of the output. Keep it set to the slowest speed you can tolerate and use an oscilloscope to verify the signal integrity. LEDs and relay drives should be set to 2MHz. Digital buses will require a little bit more science.
* Pull-up and pull-down: Open-drain lines require some leakage current to make sure their value is defined when the transistors are all off. Generally it's good practice to set pull-ups and pull-downs with real physical resistors, as all pins float on reset. This is very bad for pins with mission-critical states, like the contactor and precharge lines.No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.
* No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.
* Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.
* Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.

* Mode: This field selects where the multiplexer closest to the pin connectsDigital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.
* Digital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.
* Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.
* Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.
* Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.
* Output type: This is only relevant when you've configured a GPIO as an output.Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.
* Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.
* Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.
* Speed: This is badly named. It's really a knob to adjust the slew rate of the output. Keep it set to the slowest speed you can tolerate and use an oscilloscope to verify the signal integrity. LEDs and relay drives should be set to 2MHz. Digital buses will require a little bit more science.
* Pull-up and pull-down: Open-drain lines require some leakage current to make sure their value is defined when the transistors are all off. Generally it's good practice to set pull-ups and pull-downs with real physical resistors, as all pins float on reset. This is very bad for pins with mission-critical states, like the contactor and precharge lines.No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.
* No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.
* Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.
* Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.

Mode: This field selects where the multiplexer closest to the pin connects

* Digital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.
* Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.
* Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.
* Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.

Digital input (GPIO_Mode_IN): Pin goes to a Schmitt trigger and is used to read digital values driven by something else on the board. Use this when connecting to the output of a logic gate or another chip.

[Schmitt trigger](http://en.wikipedia.org/wiki/Schmitt_trigger)

Digital output (GPIO_Mode_OUT): Pin goes to a configurable output stage. See below for options.

Alternate function (GPIO_Mode_AF): Pin goes to another configurable multiplexer. This additional mux selects between all of the various other peripherals, like the CAN protocol generator.

Analog (GPIO_Mode_AN): Pin is unconnected from the alternate function mux. This reduces the parasitic leakage of the pin to either rail, but also makes it more vulnerable to ESD. Use this when reading or writing analog values.

Output type: This is only relevant when you've configured a GPIO as an output.

* Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.
* Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.

Open drain (GPIO_OType_OD): This connects the pin to the drain of a single low-side transistor. This means the processor can sink current but not source it. The off-state voltage at the pin is determined by external circuitry like a pull-up resistor. The on-state voltage is roughly zero. This is useful for tri-stated buses like I2C. It should be noted with care, however, that when "setting" a GPIO pin that's in open-drain configuration that its transistor is off and the processor expects the pin to be pulled high. You may read the pin's state to see if some other device on the bus is pulling the line down. This is also known as the open-collector configuration, named after bipolar junction transistors.

[ open-collector](http://en.wikipedia.org/wiki/Open_drain)

Push-pull (GPIO_OType_PP): It's like open-drain, but with a high-side transistor too. Totem-pole drives can both source and sink current. They do not share with other driving devices. This is a good "go-to" mode if you're doing things like driving LEDs, MOSFETs gates, or digital buses like 4-wire SPI.

[ Totem-pole](http://en.wikipedia.org/wiki/Push%E2%80%93pull_output)

Speed: This is badly named. It's really a knob to adjust the slew rate of the output. Keep it set to the slowest speed you can tolerate and use an oscilloscope to verify the signal integrity. LEDs and relay drives should be set to 2MHz. Digital buses will require a little bit more science.

Pull-up and pull-down: Open-drain lines require some leakage current to make sure their value is defined when the transistors are all off. Generally it's good practice to set pull-ups and pull-downs with real physical resistors, as all pins float on reset. This is very bad for pins with mission-critical states, like the contactor and precharge lines.

* No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.
* Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.
* Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.

No pull-resistors (GPIO_PuPd_NOPULL): Just like it sounds; no pull-up or pull-down resistors. Use this to let your line float. Also use this when using a push-pull drive to reduce power consumption.

Weak pull-up (GPIO_PuPd_UP): Connects a weak pull-up resistor to the line. This means that there will be current leakage from the positive power supply (usually 3.3v) to the pin.

Weak pull-down (GPIO_PuPd_DOWN): Connects a weak pull-down resistor to the line. This means there will be current leakage from the pin to ground.

### SPI

[](#h.cj6l8bfbht)

### I2C

[](#h.c652zy27hywf)

### CAN

[](#h.lptu0jie55o)

### TIM

[](#h.u6k8zhc30dgs)

* A great example of how to use timers can be found in the example code for the stm32f4 discovery boards. Alternatively, you can check out this site: http://amarkham.com/?p=37 .One note about TIM1 and TIM8. TIM1 and TIM8 are advanced timers that can do funky things general-purpose timers (TIM2-7, and TIM9-14) cannot do. Because they are advanced timers, we need to add these two lines of code to make them work like general-purpose timers:
* A great example of how to use timers can be found in the example code for the stm32f4 discovery boards. Alternatively, you can check out this site: http://amarkham.com/?p=37 .
* One note about TIM1 and TIM8. TIM1 and TIM8 are advanced timers that can do funky things general-purpose timers (TIM2-7, and TIM9-14) cannot do. Because they are advanced timers, we need to add these two lines of code to make them work like general-purpose timers:

* A great example of how to use timers can be found in the example code for the stm32f4 discovery boards. Alternatively, you can check out this site: http://amarkham.com/?p=37 .
* One note about TIM1 and TIM8. TIM1 and TIM8 are advanced timers that can do funky things general-purpose timers (TIM2-7, and TIM9-14) cannot do. Because they are advanced timers, we need to add these two lines of code to make them work like general-purpose timers:

A great example of how to use timers can be found in the example code for the stm32f4 discovery boards. Alternatively, you can check out this site: http://amarkham.com/?p=37 .

[ http://amarkham.com/?p=37](http://amarkham.com/?p=37)

One note about TIM1 and TIM8. TIM1 and TIM8 are advanced timers that can do funky things general-purpose timers (TIM2-7, and TIM9-14) cannot do. Because they are advanced timers, we need to add these two lines of code to make them work like general-purpose timers:

          /* TIM8 Main Output Enable */

          TIM_CtrlPWMOutputs(TIM8, ENABLE);

     

          // TIM IT enable

          TIM_ITConfig(TIM8, TIM_IT_Update, ENABLE);

          These lines of code should be put immediately after the configuration calls used to set up each channel, and immediately before calls to TIM_ARRPreloadConfig() and TIM_Cmd(). It worked when I did it this way, at least.

In no particular order until otherwise stated, here are some common mistakes and ways to fix them.

* Make sure you set the initial state of every output pin that you care about: don't assume that it has a specific initial state on its own.
* Make sure you set the initial state of every output pin that you care about: don't assume that it has a specific initial state on its own.

* Make sure you set the initial state of every output pin that you care about: don't assume that it has a specific initial state on its own.

Make sure you set the initial state of every output pin that you care about: don't assume that it has a specific initial state on its own.

Rachel’s Rules of Embedded Code

1. In the absence of external verification, it can be assumed that any embedded system is not plugged in.
2. If a connection has not been verified in the past five minutes, it can be assumed that the connection does not exist.
3. Any embedded system, in the absence of external stimuli, will spontaneously unplug itself.
4. Leaving a board alone for a full day guarantees that at least two connections have been broken.
5. The first n - 1 of n connections will probably be solid.  The nth is guaranteed to be broken.

In the absence of external verification, it can be assumed that any embedded system is not plugged in.

If a connection has not been verified in the past five minutes, it can be assumed that the connection does not exist.

Any embedded system, in the absence of external stimuli, will spontaneously unplug itself.

Leaving a board alone for a full day guarantees that at least two connections have been broken.

The first n - 1 of n connections will probably be solid.  The nth is guaranteed to be broken.

