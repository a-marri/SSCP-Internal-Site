# protobufs

## SSCP - Protobufs

## Protobufs

We are using nanopb (https://github.com/nanopb/nanopb) for data serialization through ethernet.

[https://github.com/nanopb/nanopb](https://github.com/nanopb/nanopb)

Code structure:

* libdrivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.scriptscompile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* libdrivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.
* drivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.
* &#x20;pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic.
* \*/pb.h: Macros. May or may not be useful.
* \*.pb.h, \*.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.
* scriptscompile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* compile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* libdrivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.
* drivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.
* &#x20;pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic.
* \*/pb.h: Macros. May or may not be useful.
* \*.pb.h, \*.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.
* scriptscompile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* compile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

lib

* drivers pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic._/pb.h: Macros. May or may not be useful._.pb.h, \*.pb.c: Automatically generated protobuf files.
* &#x20;pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic.
* \*/pb.h: Macros. May or may not be useful.
* \*.pb.h, \*.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.

drivers

* &#x20;pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic.
* \*/pb.h: Macros. May or may not be useful.
* \*.pb.h, \*.pb.c: Automatically generated protobuf files.

&#x20;pb\_common(.h, .c), pb\_encode(.h, .c), pb\_decode(.h, .c): Provides protobuf encoding/decoding logic.

\*/pb.h: Macros. May or may not be useful.

\*.pb.h, \*.pb.c: Automatically generated protobuf files.

protobufs

* Put .proto files here.

Put .proto files here.

scripts

* compile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

compile\_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

Protobuf Structure:

message CarStateMessage {

&#x20;   required uint32 datetime = 1;

&#x20;   required uint32 board\_id = 2;

&#x20;  &#x20;

&#x20;   // Vehicle computer

&#x20;   // BMS

&#x20;   // Pedal variables

&#x20;   // Steering wheel

}
