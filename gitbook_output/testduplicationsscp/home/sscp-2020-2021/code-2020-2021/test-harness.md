# test-harness

## SSCP - Test Harness

## Test Harness

We utilise the Unity Test Harness for all our embedded systems this cycle

[Unity Test Harness](https://github.com/ThrowTheSwitch/Unity)

### Testing with Unity

Unity supplies a wide range of macros for basic unit testing. Most are quite straightforward, but still eliminate reinventing the wheel. The list can be found in unity.h, and include examples such as

&#x20;

* Simple Boolean - TEST\_ASSERT\_TRUE, TEST\_ASSERT\_FALSE
* Standard integer - TEST\_ASSERT\_EQUAL, TEST\_ASSERT\_NOT\_EQUALSize specific – TEST\_ASSERT\_EQUAL\_INT8, \_INT16, \_INT32Sign specific – TEST\_ASSERT\_EQUAL\_UINT8, \_UINT16, …Base specific – TEST\_ASSERT\_EQUAL\_HEX8, \_HEX16, …Bit masks - TEST\_ASSERT\_BITS, TEST\_ASSERT\_BITS\_HIGH, TEST\_ASSERT\_BIT\_LOWRanges – TEST\_ASSERT\_INT\_WITHINArrays – TEST\_ASSERT\_EQUAL\_INT\_ARRAYStrings and structures – TEST\_ASSERT\_EQUAL\_PTR, \_STRING, \_MEMORYFloating point (if enabled) – TEST\_ASSERT\_FLOAT\_WITHIN
* Size specific – TEST\_ASSERT\_EQUAL\_INT8, \_INT16, \_INT32
* Sign specific – TEST\_ASSERT\_EQUAL\_UINT8, \_UINT16, …
* Base specific – TEST\_ASSERT\_EQUAL\_HEX8, \_HEX16, …
* Bit masks - TEST\_ASSERT\_BITS, TEST\_ASSERT\_BITS\_HIGH, TEST\_ASSERT\_BIT\_LOW
* Ranges – TEST\_ASSERT\_INT\_WITHIN
* Arrays – TEST\_ASSERT\_EQUAL\_INT\_ARRAY
* Strings and structures – TEST\_ASSERT\_EQUAL\_PTR, \_STRING, \_MEMORY
* Floating point (if enabled) – TEST\_ASSERT\_FLOAT\_WITHIN

Simple Boolean - TEST\_ASSERT\_TRUE, TEST\_ASSERT\_FALSE

Standard integer - TEST\_ASSERT\_EQUAL, TEST\_ASSERT\_NOT\_EQUAL

* Size specific – TEST\_ASSERT\_EQUAL\_INT8, \_INT16, \_INT32
* Sign specific – TEST\_ASSERT\_EQUAL\_UINT8, \_UINT16, …
* Base specific – TEST\_ASSERT\_EQUAL\_HEX8, \_HEX16, …
* Bit masks - TEST\_ASSERT\_BITS, TEST\_ASSERT\_BITS\_HIGH, TEST\_ASSERT\_BIT\_LOW
* Ranges – TEST\_ASSERT\_INT\_WITHIN
* Arrays – TEST\_ASSERT\_EQUAL\_INT\_ARRAY
* Strings and structures – TEST\_ASSERT\_EQUAL\_PTR, \_STRING, \_MEMORY
* Floating point (if enabled) – TEST\_ASSERT\_FLOAT\_WITHIN

Size specific – TEST\_ASSERT\_EQUAL\_INT8, \_INT16, \_INT32

Sign specific – TEST\_ASSERT\_EQUAL\_UINT8, \_UINT16, …

Base specific – TEST\_ASSERT\_EQUAL\_HEX8, \_HEX16, …

Bit masks - TEST\_ASSERT\_BITS, TEST\_ASSERT\_BITS\_HIGH, TEST\_ASSERT\_BIT\_LOW

Ranges – TEST\_ASSERT\_INT\_WITHIN

Arrays – TEST\_ASSERT\_EQUAL\_INT\_ARRAY

Strings and structures – TEST\_ASSERT\_EQUAL\_PTR, \_STRING, \_MEMORY

Floating point (if enabled) – TEST\_ASSERT\_FLOAT\_WITHIN
