# SSCP - Test Harness

# Test Harness

We utilise the Unity Test Harness for all our embedded systems this cycle

[ Unity Test Harness](https://github.com/ThrowTheSwitch/Unity)

## Testing with Unity

[](#h.p9eaz9gll3u1)

Unity supplies a wide range of macros for basic unit testing. Most are quite straightforward, but still eliminate reinventing the wheel. The list can be found in unity.h, and include examples such as

 

* Simple Boolean - TEST_ASSERT_TRUE, TEST_ASSERT_FALSE
* Standard integer - TEST_ASSERT_EQUAL, TEST_ASSERT_NOT_EQUALSize specific – TEST_ASSERT_EQUAL_INT8, _INT16, _INT32Sign specific – TEST_ASSERT_EQUAL_UINT8, _UINT16, …Base specific – TEST_ASSERT_EQUAL_HEX8, _HEX16, …Bit masks - TEST_ASSERT_BITS, TEST_ASSERT_BITS_HIGH, TEST_ASSERT_BIT_LOWRanges – TEST_ASSERT_INT_WITHINArrays – TEST_ASSERT_EQUAL_INT_ARRAYStrings and structures – TEST_ASSERT_EQUAL_PTR, _STRING, _MEMORYFloating point (if enabled) – TEST_ASSERT_FLOAT_WITHIN
* Size specific – TEST_ASSERT_EQUAL_INT8, _INT16, _INT32
* Sign specific – TEST_ASSERT_EQUAL_UINT8, _UINT16, …
* Base specific – TEST_ASSERT_EQUAL_HEX8, _HEX16, …
* Bit masks - TEST_ASSERT_BITS, TEST_ASSERT_BITS_HIGH, TEST_ASSERT_BIT_LOW
* Ranges – TEST_ASSERT_INT_WITHIN
* Arrays – TEST_ASSERT_EQUAL_INT_ARRAY
* Strings and structures – TEST_ASSERT_EQUAL_PTR, _STRING, _MEMORY
* Floating point (if enabled) – TEST_ASSERT_FLOAT_WITHIN

Simple Boolean - TEST_ASSERT_TRUE, TEST_ASSERT_FALSE

Standard integer - TEST_ASSERT_EQUAL, TEST_ASSERT_NOT_EQUAL

* Size specific – TEST_ASSERT_EQUAL_INT8, _INT16, _INT32
* Sign specific – TEST_ASSERT_EQUAL_UINT8, _UINT16, …
* Base specific – TEST_ASSERT_EQUAL_HEX8, _HEX16, …
* Bit masks - TEST_ASSERT_BITS, TEST_ASSERT_BITS_HIGH, TEST_ASSERT_BIT_LOW
* Ranges – TEST_ASSERT_INT_WITHIN
* Arrays – TEST_ASSERT_EQUAL_INT_ARRAY
* Strings and structures – TEST_ASSERT_EQUAL_PTR, _STRING, _MEMORY
* Floating point (if enabled) – TEST_ASSERT_FLOAT_WITHIN

Size specific – TEST_ASSERT_EQUAL_INT8, _INT16, _INT32

Sign specific – TEST_ASSERT_EQUAL_UINT8, _UINT16, …

Base specific – TEST_ASSERT_EQUAL_HEX8, _HEX16, …

Bit masks - TEST_ASSERT_BITS, TEST_ASSERT_BITS_HIGH, TEST_ASSERT_BIT_LOW

Ranges – TEST_ASSERT_INT_WITHIN

Arrays – TEST_ASSERT_EQUAL_INT_ARRAY

Strings and structures – TEST_ASSERT_EQUAL_PTR, _STRING, _MEMORY

Floating point (if enabled) – TEST_ASSERT_FLOAT_WITHIN

