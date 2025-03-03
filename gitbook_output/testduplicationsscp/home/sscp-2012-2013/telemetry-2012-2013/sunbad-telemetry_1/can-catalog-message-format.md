# SSCP - CAN Catalog Message Format

# CAN Catalog Message Format

## Introduction

[](#h.mbwwwywa6mig)

From Equinox through Xenith our CAN message format was created in an ad-hoc manner. We would simply create arbitrary message types to suit our needs, resulting in a poorly documented and difficult to use communications systems. Adding new functionality was painful and required updating many layers of software.

The Catalog represents an attempt to fix this through a standardized layer for information interchange based on a list of variables with some metadata about their content. Unlike our previous systems, it uses the CAN 2.0B extended identifier (29 bits) rather than the standard identifier (11 bits). This both provides for the overhead required for catalog access as well as a simple means to coexist with earlier software.

## 29-bit identifier

[](#h.kdzzof5fsz54)

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

## Field descriptions

[](#h.68j2q42v2p5j)

### isCat

[](#h.djplh6c3ocui)

All packets intended to communicate through the catalog system should set this bit. This is a means for future expansion, allowing us to have other functionality using the other half of the identifier space.

### devID

[](#h.mxsk6tsbfpd3)

This is the device identifier and should uniquely identify a role within the vehicle. This field is 8 bits long because CAN supports a maximum of 256 devices. While we do not expect to ever reach such a large number of nodes in our vehicle, out catalog should not preclude the possibility.

### varID

[](#h.ssjiu4v2a9sk)

This is a unique catalog entry identifier. No guarantees are made that this space be densely packed; catalog entries can have any identifier even if it is larger than the total count of entries. Some identifiers will be required in order to facilitate board identification and entry reflection.

### index

[](#h.vxfco9rrgva6)

Many variables are actually arrays. For example, the battery management system might have an array of float to represent the voltages of the cells in the battery pack. An index of 0 would refer to the first element.

Strings are an exception to the rule. As strings are arrays of char it is very wasteful to put only one of them in a CAN message. Further, strings can be very long. When communicating strings, the index field will actually represent a chunk of 8 bytes within the string. For example, if I have an array containing "The quick brown fox jumps over the lazy dog", then index 0 will refer to characters "The quic" and index 1 will refer to "k brown " and so on.

### opID

[](#h.25kang5ag6xf)

Beyond just getting and setting values, the catalog must support reflection in to the structure of its contents. This allows an uninformed system to request information about any board on the car and build up the database needed to communicate with it. There are 16 possible operations:

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

## Types

[](#h.847fr6vyx8xt)

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

## Variable Name

[](#h.y4e9u9g0xh0f)

The variable name is a string.  If the name has units the units should be a human-readable string  with the variable name followed by a # followed by  the units.

## Flags 

[](#h.9refzvx39ffp)

### Embedded Content

Embedded content: [Custom embed]()

<iframe width="100%" height="400" src="" frameborder="0"></iframe>

