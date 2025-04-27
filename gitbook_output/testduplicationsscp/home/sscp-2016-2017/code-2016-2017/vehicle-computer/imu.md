# imu

## SSCP - IMU

## IMU

IMU shuttle board pin mapping (attached)

Looking at this example project:

Arduino on the MEGA 2560 uses pins 50-53 for SPI (at least if you're using the standard SPI library).

The github above uses 3 pins called the CSB1,2,3.

Looking at the datasheet suggests that this is the way we can select which data we want.&#x20;

[datasheet](http://www.mouser.com/ds/2/783/BST-BMX055-DS000-02-786507.pdf)

CSB1: SPI Chip select Accel

CSB2: SPI Chip select Gyro

CSB3: SPI Chip select magnet sensor

Current problem: data doesn't make sense. There might be overflow.

Examples:

https://github.com/rsegecin/ArduinoBMX055/blob/master/IMUReader.ino#L27

[https://github.com/rsegecin/ArduinoBMX055/blob/master/IMUReader.ino#L27](https://github.com/rsegecin/ArduinoBMX055/blob/master/IMUReader.ino#L27)

https://github.com/ControlEverythingCommunity/BMX055/blob/master/Arduino/BMX055.ino

[https://github.com/ControlEverythingCommunity/BMX055/blob/master/Arduino/BMX055.ino](https://github.com/ControlEverythingCommunity/BMX055/blob/master/Arduino/BMX055.ino)

https://github.com/kriswiner/BMX-055/blob/master/BMX055\_MS5637\_BasicAHRS\_t3.ino

[https://github.com/kriswiner/BMX-055/blob/master/BMX055\_MS5637\_BasicAHRS\_t3.ino](https://github.com/kriswiner/BMX-055/blob/master/BMX055_MS5637_BasicAHRS_t3.ino)

Moving it to STM32:

Unsure if 3V is enough, It might need 3.3V

THERE IS A DRIVER FROM BOSCH:

https://github.com/BoschSensortec/BMA2x2\_driver

#### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=1yYyqSjiYOhgD5X_-HgZkQjzCj8JCQArx#list)
