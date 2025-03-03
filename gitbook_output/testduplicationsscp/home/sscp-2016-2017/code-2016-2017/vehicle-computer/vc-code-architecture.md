# SSCP - VC Code Architecture

# VC Code Architecture

SSCP_Lib:

These should be structured as APIs with private functions for operation but public getter/setter (sender/receiver) functions.

* lib_pin.c/h (pin set high, pin set low, SPI control)lib_can.c/h (for handling CAN messages to/from Tritiums)lib_ethernet.c/h (for send/receive ethernet)lib_nrf.c/h (for send over NRF)lib_sd.c/h (SD card writing)
* lib_pin.c/h (pin set high, pin set low, SPI control)
* lib_can.c/h (for handling CAN messages to/from Tritiums)
* lib_ethernet.c/h (for send/receive ethernet)
* lib_nrf.c/h (for send over NRF)
* lib_sd.c/h (SD card writing)

* lib_pin.c/h (pin set high, pin set low, SPI control)
* lib_can.c/h (for handling CAN messages to/from Tritiums)
* lib_ethernet.c/h (for send/receive ethernet)
* lib_nrf.c/h (for send over NRF)
* lib_sd.c/h (SD card writing)

lib_pin.c/h (pin set high, pin set low, SPI control)

lib_can.c/h (for handling CAN messages to/from Tritiums)

lib_ethernet.c/h (for send/receive ethernet)

lib_nrf.c/h (for send over NRF)

lib_sd.c/h (SD card writing)

User:

There will be two layers here: dev_ for drivers, config, and setup and app_ for logic and sending/receiving of data. We can structure most of these at both layers as mostly private functions with some public APIs.

* dev_imu_config.c/h (driver/setup/API for IMU chips -- maybe divide into three)dev_motor_config.c/h (driver/setup/API to talk to motor)dev_tritium_config.c/h (driver/setup/API to talk to tritium)dev_bms_config.c/h (API to receive from BMS)dev_external_config.c/h (API for all else, if there is anything -- may not be necessary)dev_drive_config.c/h (other config for driver controls -- may not be necessary)dev_steering_wheel_config.c/h (driver/setup/API for steering wheel -- relevant to VC because we use the API)dev_lights_config.c/h (driver/setup/API for lights -- relevant to VC because we use the API)app_send_data.c/h (logic to collate and send out structs to telemetry)app_cruise_control.c/h (PID loop for cruise control)app_pedals.c/h (pedal debouncing, calibrating, and regen vs mechanical braking)app_lights.c/h (send commands to light board)app_ethernet_packets.c/h (API for ethernet send/receive -- used by others)app_steering.c/h (query from steering wheel and send to steering wheel)app_imu_gyroscope.c/h (read from gyroscope)app_imu_accelerometer.c/h (read from accelerometer)app_imu_magnetometer.c/h (read from magnetometer)
* dev_imu_config.c/h (driver/setup/API for IMU chips -- maybe divide into three)
* dev_motor_config.c/h (driver/setup/API to talk to motor)
* dev_tritium_config.c/h (driver/setup/API to talk to tritium)
* dev_bms_config.c/h (API to receive from BMS)
* dev_external_config.c/h (API for all else, if there is anything -- may not be necessary)
* dev_drive_config.c/h (other config for driver controls -- may not be necessary)
* dev_steering_wheel_config.c/h (driver/setup/API for steering wheel -- relevant to VC because we use the API)
* dev_lights_config.c/h (driver/setup/API for lights -- relevant to VC because we use the API)
* app_send_data.c/h (logic to collate and send out structs to telemetry)
* app_cruise_control.c/h (PID loop for cruise control)
* app_pedals.c/h (pedal debouncing, calibrating, and regen vs mechanical braking)
* app_lights.c/h (send commands to light board)
* app_ethernet_packets.c/h (API for ethernet send/receive -- used by others)
* app_steering.c/h (query from steering wheel and send to steering wheel)
* app_imu_gyroscope.c/h (read from gyroscope)
* app_imu_accelerometer.c/h (read from accelerometer)
* app_imu_magnetometer.c/h (read from magnetometer)

* dev_imu_config.c/h (driver/setup/API for IMU chips -- maybe divide into three)
* dev_motor_config.c/h (driver/setup/API to talk to motor)
* dev_tritium_config.c/h (driver/setup/API to talk to tritium)
* dev_bms_config.c/h (API to receive from BMS)
* dev_external_config.c/h (API for all else, if there is anything -- may not be necessary)
* dev_drive_config.c/h (other config for driver controls -- may not be necessary)
* dev_steering_wheel_config.c/h (driver/setup/API for steering wheel -- relevant to VC because we use the API)
* dev_lights_config.c/h (driver/setup/API for lights -- relevant to VC because we use the API)
* app_send_data.c/h (logic to collate and send out structs to telemetry)
* app_cruise_control.c/h (PID loop for cruise control)
* app_pedals.c/h (pedal debouncing, calibrating, and regen vs mechanical braking)
* app_lights.c/h (send commands to light board)
* app_ethernet_packets.c/h (API for ethernet send/receive -- used by others)
* app_steering.c/h (query from steering wheel and send to steering wheel)
* app_imu_gyroscope.c/h (read from gyroscope)
* app_imu_accelerometer.c/h (read from accelerometer)
* app_imu_magnetometer.c/h (read from magnetometer)

dev_imu_config.c/h (driver/setup/API for IMU chips -- maybe divide into three)

dev_motor_config.c/h (driver/setup/API to talk to motor)

dev_tritium_config.c/h (driver/setup/API to talk to tritium)

dev_bms_config.c/h (API to receive from BMS)

dev_external_config.c/h (API for all else, if there is anything -- may not be necessary)

dev_drive_config.c/h (other config for driver controls -- may not be necessary)

dev_steering_wheel_config.c/h (driver/setup/API for steering wheel -- relevant to VC because we use the API)

dev_lights_config.c/h (driver/setup/API for lights -- relevant to VC because we use the API)

app_send_data.c/h (logic to collate and send out structs to telemetry)

app_cruise_control.c/h (PID loop for cruise control)

app_pedals.c/h (pedal debouncing, calibrating, and regen vs mechanical braking)

app_lights.c/h (send commands to light board)

app_ethernet_packets.c/h (API for ethernet send/receive -- used by others)

app_steering.c/h (query from steering wheel and send to steering wheel)

app_imu_gyroscope.c/h (read from gyroscope)

app_imu_accelerometer.c/h (read from accelerometer)

app_imu_magnetometer.c/h (read from magnetometer)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Per file:

* lib_pin.c/hPublic:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)Private:lib_can.c/hPublic:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)app_CAN_txTask()app_CAN_rxTask()Private:lib_ethernet.c/hPublic:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)Private:lib_nrf.c/hPublic:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)Private:lib_sd.c/hPublic:Private:dev_imu_config.c/hPublic:Private:dev_motor_config.c/hPublic:Private:dev_tritium_config.c/hPublic:dev_tritium_initState()dev_tritium_send() --> call some function in app_send_data.cdev_tritium_getDeviceID()Private:average()dev_tritium_CANTask()dev_tritium_motorDriveCommand()dev_tritium_reset()dev_tritium_parseMcMsg()dev_tritium_assert()dev_drive_config.c/hPublic:dev_drive_config_LEDinit()dev_drive_config_initMic()dev_drive_config_CANsetup()Private:
* lib_pin.c/hPublic:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)Private:
* Public:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)
* lib_pin_setHigh(pin)
* lib_pin_setLow(pin)
* lib_pin_pinConfig(args...)
* lib_pin_toggle(pin)
* lin_pin_read(pin)
* Private:
* lib_can.c/hPublic:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)app_CAN_txTask()app_CAN_rxTask()Private:
* Public:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)
* lib_can_send(message)
* lib_can_receive(message)
* lib_can_messageConfig(args...)
* app_CAN_txTask()
* app_CAN_rxTask()
* Private:
* lib_ethernet.c/hPublic:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)Private:
* Public:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)
* lib_ethernet_send(message)
* lib_ethernet_receive(message)
* lib_ethernet_messageConfig(args...)
* Private:
* lib_nrf.c/hPublic:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)Private:
* Public:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)
* lib_nrf_send(message)
* lib_nrf_receive(message)
* lib_nrf_messageConfig(args...)
* Private:
* lib_sd.c/hPublic:Private:
* Public:
* Private:
* dev_imu_config.c/hPublic:Private:
* Public:
* Private:
* dev_motor_config.c/hPublic:Private:
* Public:
* Private:
* dev_tritium_config.c/hPublic:dev_tritium_initState()dev_tritium_send() --> call some function in app_send_data.cdev_tritium_getDeviceID()Private:average()dev_tritium_CANTask()dev_tritium_motorDriveCommand()dev_tritium_reset()dev_tritium_parseMcMsg()dev_tritium_assert()
* Public:
* dev_tritium_initState()
* dev_tritium_send() --> call some function in app_send_data.c
* dev_tritium_getDeviceID()
* Private:
* average()
* dev_tritium_CANTask()
* dev_tritium_motorDriveCommand()
* dev_tritium_reset()
* dev_tritium_parseMcMsg()
* dev_tritium_assert()
* dev_drive_config.c/hPublic:dev_drive_config_LEDinit()dev_drive_config_initMic()dev_drive_config_CANsetup()Private:
* Public:
* dev_drive_config_LEDinit()
* dev_drive_config_initMic()
* dev_drive_config_CANsetup()
* Private:

* lib_pin.c/hPublic:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)Private:
* Public:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)
* lib_pin_setHigh(pin)
* lib_pin_setLow(pin)
* lib_pin_pinConfig(args...)
* lib_pin_toggle(pin)
* lin_pin_read(pin)
* Private:
* lib_can.c/hPublic:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)app_CAN_txTask()app_CAN_rxTask()Private:
* Public:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)
* lib_can_send(message)
* lib_can_receive(message)
* lib_can_messageConfig(args...)
* app_CAN_txTask()
* app_CAN_rxTask()
* Private:
* lib_ethernet.c/hPublic:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)Private:
* Public:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)
* lib_ethernet_send(message)
* lib_ethernet_receive(message)
* lib_ethernet_messageConfig(args...)
* Private:
* lib_nrf.c/hPublic:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)Private:
* Public:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)
* lib_nrf_send(message)
* lib_nrf_receive(message)
* lib_nrf_messageConfig(args...)
* Private:
* lib_sd.c/hPublic:Private:
* Public:
* Private:
* dev_imu_config.c/hPublic:Private:
* Public:
* Private:
* dev_motor_config.c/hPublic:Private:
* Public:
* Private:
* dev_tritium_config.c/hPublic:dev_tritium_initState()dev_tritium_send() --> call some function in app_send_data.cdev_tritium_getDeviceID()Private:average()dev_tritium_CANTask()dev_tritium_motorDriveCommand()dev_tritium_reset()dev_tritium_parseMcMsg()dev_tritium_assert()
* Public:
* dev_tritium_initState()
* dev_tritium_send() --> call some function in app_send_data.c
* dev_tritium_getDeviceID()
* Private:
* average()
* dev_tritium_CANTask()
* dev_tritium_motorDriveCommand()
* dev_tritium_reset()
* dev_tritium_parseMcMsg()
* dev_tritium_assert()
* dev_drive_config.c/hPublic:dev_drive_config_LEDinit()dev_drive_config_initMic()dev_drive_config_CANsetup()Private:
* Public:
* dev_drive_config_LEDinit()
* dev_drive_config_initMic()
* dev_drive_config_CANsetup()
* Private:

lib_pin.c/h

* Public:lib_pin_setHigh(pin)lib_pin_setLow(pin)lib_pin_pinConfig(args...)lib_pin_toggle(pin)lin_pin_read(pin)
* lib_pin_setHigh(pin)
* lib_pin_setLow(pin)
* lib_pin_pinConfig(args...)
* lib_pin_toggle(pin)
* lin_pin_read(pin)
* Private:

Public:

* lib_pin_setHigh(pin)
* lib_pin_setLow(pin)
* lib_pin_pinConfig(args...)
* lib_pin_toggle(pin)
* lin_pin_read(pin)

lib_pin_setHigh(pin)

lib_pin_setLow(pin)

lib_pin_pinConfig(args...)

lib_pin_toggle(pin)

lin_pin_read(pin)

Private:

lib_can.c/h

* Public:lib_can_send(message)lib_can_receive(message)lib_can_messageConfig(args...)
* lib_can_send(message)
* lib_can_receive(message)
* lib_can_messageConfig(args...)
* app_CAN_txTask()
* app_CAN_rxTask()
* Private:

Public:

* lib_can_send(message)
* lib_can_receive(message)
* lib_can_messageConfig(args...)

lib_can_send(message)

lib_can_receive(message)

lib_can_messageConfig(args...)

app_CAN_txTask()

app_CAN_rxTask()

Private:

lib_ethernet.c/h

* Public:lib_ethernet_send(message)lib_ethernet_receive(message)lib_ethernet_messageConfig(args...)
* lib_ethernet_send(message)
* lib_ethernet_receive(message)
* lib_ethernet_messageConfig(args...)
* Private:

Public:

* lib_ethernet_send(message)
* lib_ethernet_receive(message)
* lib_ethernet_messageConfig(args...)

lib_ethernet_send(message)

lib_ethernet_receive(message)

lib_ethernet_messageConfig(args...)

Private:

lib_nrf.c/h

* Public:lib_nrf_send(message)lib_nrf_receive(message)lib_nrf_messageConfig(args...)
* lib_nrf_send(message)
* lib_nrf_receive(message)
* lib_nrf_messageConfig(args...)
* Private:

Public:

* lib_nrf_send(message)
* lib_nrf_receive(message)
* lib_nrf_messageConfig(args...)

lib_nrf_send(message)

lib_nrf_receive(message)

lib_nrf_messageConfig(args...)

Private:

lib_sd.c/h

* Public:
* Private:

Public:

Private:

dev_imu_config.c/h

* Public:
* Private:

Public:

Private:

dev_motor_config.c/h

* Public:
* Private:

Public:

Private:

dev_tritium_config.c/h

* Public:
* dev_tritium_initState()
* dev_tritium_send() --> call some function in app_send_data.c
* dev_tritium_getDeviceID()
* Private:
* average()
* dev_tritium_CANTask()
* dev_tritium_motorDriveCommand()
* dev_tritium_reset()
* dev_tritium_parseMcMsg()
* dev_tritium_assert()

Public:

dev_tritium_initState()

dev_tritium_send() --> call some function in app_send_data.c

dev_tritium_getDeviceID()

Private:

average()

dev_tritium_CANTask()

dev_tritium_motorDriveCommand()

dev_tritium_reset()

dev_tritium_parseMcMsg()

dev_tritium_assert()

dev_drive_config.c/h

* Public:
* dev_drive_config_LEDinit()
* dev_drive_config_initMic()
* dev_drive_config_CANsetup()
* Private:

Public:

dev_drive_config_LEDinit()

dev_drive_config_initMic()

dev_drive_config_CANsetup()

Private:

* dev_adc.c/hPublic:dev_adc_getChannel()dev_adc_Poll()dev_adc_initVal()Private:dev_adc_setup()dev_adc_filterVoltage()dev_adc_filterVoltageFast()app_send_data.c/hPublic:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()Private:app_cruise_control.c/hPublic:app_cruise_control_cruise()Private:app_cruise_control_updateTime()app_pedals.c/hPublic:app_pedals_driveTask()Private:app_pedals_configurePedals()app_pedals_applyDeadzone()app_pedals_throttleCheck()app_pedals_brakeCheck()app_pedals_brakeResponse()app_pedals_throttleResponse()app_pedals_brakeValueUnplugged()app_pedals_throttleValueExceedMax()app_imu_gyroscope.c/hPublic:app_imu_gyroscope_read()Private:app_imu_accelerometer.c/hPublic:app_imu_accelerometer_read()Private:app_imu_magnetometer.c/hPublic:app_imu_magnetometer_read()Private:
* Public:dev_adc_getChannel()dev_adc_Poll()dev_adc_initVal()
* dev_adc_getChannel()
* dev_adc_Poll()
* dev_adc_initVal()
* Private:dev_adc_setup()dev_adc_filterVoltage()dev_adc_filterVoltageFast()
* dev_adc_setup()
* dev_adc_filterVoltage()
* dev_adc_filterVoltageFast()
* app_send_data.c/hPublic:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()Private:
* Public:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()
* app_send_data_telemetry()
* app_send_data_buttonBoard()
* app_send_data_lightsCommands()
* app_send_data_BMS()
* Private:
* app_cruise_control.c/hPublic:app_cruise_control_cruise()Private:app_cruise_control_updateTime()
* Public:
* app_cruise_control_cruise()
* Private:
* app_cruise_control_updateTime()
* app_pedals.c/hPublic:app_pedals_driveTask()Private:app_pedals_configurePedals()app_pedals_applyDeadzone()app_pedals_throttleCheck()app_pedals_brakeCheck()app_pedals_brakeResponse()app_pedals_throttleResponse()app_pedals_brakeValueUnplugged()app_pedals_throttleValueExceedMax()
* Public:
* app_pedals_driveTask()
* Private:
* app_pedals_configurePedals()
* app_pedals_applyDeadzone()
* app_pedals_throttleCheck()
* app_pedals_brakeCheck()
* app_pedals_brakeResponse()
* app_pedals_throttleResponse()
* app_pedals_brakeValueUnplugged()
* app_pedals_throttleValueExceedMax()
* app_imu_gyroscope.c/hPublic:app_imu_gyroscope_read()Private:
* Public:app_imu_gyroscope_read()
* app_imu_gyroscope_read()
* Private:
* app_imu_accelerometer.c/hPublic:app_imu_accelerometer_read()Private:
* Public:app_imu_accelerometer_read()
* app_imu_accelerometer_read()
* Private:
* app_imu_magnetometer.c/hPublic:app_imu_magnetometer_read()Private:
* Public:app_imu_magnetometer_read()
* app_imu_magnetometer_read()
* Private:

dev_adc.c/h

* Public:dev_adc_getChannel()dev_adc_Poll()dev_adc_initVal()
* dev_adc_getChannel()
* dev_adc_Poll()
* dev_adc_initVal()
* Private:dev_adc_setup()dev_adc_filterVoltage()dev_adc_filterVoltageFast()
* dev_adc_setup()
* dev_adc_filterVoltage()
* dev_adc_filterVoltageFast()
* app_send_data.c/hPublic:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()Private:
* Public:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()
* app_send_data_telemetry()
* app_send_data_buttonBoard()
* app_send_data_lightsCommands()
* app_send_data_BMS()
* Private:
* app_cruise_control.c/hPublic:app_cruise_control_cruise()Private:app_cruise_control_updateTime()
* Public:
* app_cruise_control_cruise()
* Private:
* app_cruise_control_updateTime()
* app_pedals.c/hPublic:app_pedals_driveTask()Private:app_pedals_configurePedals()app_pedals_applyDeadzone()app_pedals_throttleCheck()app_pedals_brakeCheck()app_pedals_brakeResponse()app_pedals_throttleResponse()app_pedals_brakeValueUnplugged()app_pedals_throttleValueExceedMax()
* Public:
* app_pedals_driveTask()
* Private:
* app_pedals_configurePedals()
* app_pedals_applyDeadzone()
* app_pedals_throttleCheck()
* app_pedals_brakeCheck()
* app_pedals_brakeResponse()
* app_pedals_throttleResponse()
* app_pedals_brakeValueUnplugged()
* app_pedals_throttleValueExceedMax()
* app_imu_gyroscope.c/hPublic:app_imu_gyroscope_read()Private:
* Public:app_imu_gyroscope_read()
* app_imu_gyroscope_read()
* Private:
* app_imu_accelerometer.c/hPublic:app_imu_accelerometer_read()Private:
* Public:app_imu_accelerometer_read()
* app_imu_accelerometer_read()
* Private:
* app_imu_magnetometer.c/hPublic:app_imu_magnetometer_read()Private:
* Public:app_imu_magnetometer_read()
* app_imu_magnetometer_read()
* Private:

Public:

* dev_adc_getChannel()
* dev_adc_Poll()
* dev_adc_initVal()

dev_adc_getChannel()

dev_adc_Poll()

dev_adc_initVal()

Private:

* dev_adc_setup()
* dev_adc_filterVoltage()
* dev_adc_filterVoltageFast()

dev_adc_setup()

dev_adc_filterVoltage()

dev_adc_filterVoltageFast()

app_send_data.c/h

* Public:app_send_data_telemetry()app_send_data_buttonBoard()app_send_data_lightsCommands()app_send_data_BMS()
* app_send_data_telemetry()
* app_send_data_buttonBoard()
* app_send_data_lightsCommands()
* app_send_data_BMS()
* Private:

Public:

* app_send_data_telemetry()
* app_send_data_buttonBoard()
* app_send_data_lightsCommands()
* app_send_data_BMS()

app_send_data_telemetry()

app_send_data_buttonBoard()

app_send_data_lightsCommands()

app_send_data_BMS()

Private:

app_cruise_control.c/h

* Public:
* app_cruise_control_cruise()
* Private:
* app_cruise_control_updateTime()

Public:

app_cruise_control_cruise()

Private:

app_cruise_control_updateTime()

app_pedals.c/h

* Public:
* app_pedals_driveTask()
* Private:
* app_pedals_configurePedals()
* app_pedals_applyDeadzone()
* app_pedals_throttleCheck()
* app_pedals_brakeCheck()
* app_pedals_brakeResponse()
* app_pedals_throttleResponse()
* app_pedals_brakeValueUnplugged()
* app_pedals_throttleValueExceedMax()

Public:

app_pedals_driveTask()

Private:

app_pedals_configurePedals()

app_pedals_applyDeadzone()

app_pedals_throttleCheck()

app_pedals_brakeCheck()

app_pedals_brakeResponse()

app_pedals_throttleResponse()

app_pedals_brakeValueUnplugged()

app_pedals_throttleValueExceedMax()

app_imu_gyroscope.c/h

* Public:app_imu_gyroscope_read()
* app_imu_gyroscope_read()
* Private:

Public:

* app_imu_gyroscope_read()

app_imu_gyroscope_read()

Private:

app_imu_accelerometer.c/h

* Public:app_imu_accelerometer_read()
* app_imu_accelerometer_read()
* Private:

Public:

* app_imu_accelerometer_read()

app_imu_accelerometer_read()

Private:

app_imu_magnetometer.c/h

* Public:app_imu_magnetometer_read()
* app_imu_magnetometer_read()
* Private:

Public:

* app_imu_magnetometer_read()

app_imu_magnetometer_read()

Private:

