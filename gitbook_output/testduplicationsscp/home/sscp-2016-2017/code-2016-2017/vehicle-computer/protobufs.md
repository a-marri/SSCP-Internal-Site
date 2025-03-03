# SSCP - Protobufs

# Protobufs

We are using nanopb (https://github.com/nanopb/nanopb) for data serialization through ethernet.

[https://github.com/nanopb/nanopb](https://github.com/nanopb/nanopb)

Code structure:

* libdrivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.scriptscompile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* libdrivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.
* drivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.
*  pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.
* */pb.h: Macros. May or may not be useful.
* *.pb.h, *.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.
* scriptscompile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* compile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

* libdrivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.protobufsPut .proto files here.
* drivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.
*  pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.
* */pb.h: Macros. May or may not be useful.
* *.pb.h, *.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.
* scriptscompile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.
* compile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

lib

* drivers pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.*/pb.h: Macros. May or may not be useful.*.pb.h, *.pb.c: Automatically generated protobuf files.
*  pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.
* */pb.h: Macros. May or may not be useful.
* *.pb.h, *.pb.c: Automatically generated protobuf files.
* protobufsPut .proto files here.
* Put .proto files here.

drivers

*  pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.
* */pb.h: Macros. May or may not be useful.
* *.pb.h, *.pb.c: Automatically generated protobuf files.

 pb_common(.h, .c), pb_encode(.h, .c), pb_decode(.h, .c): Provides protobuf encoding/decoding logic.

*/pb.h: Macros. May or may not be useful.

*.pb.h, *.pb.c: Automatically generated protobuf files.

protobufs

* Put .proto files here.

Put .proto files here.

scripts

* compile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

compile_pb.sh: Run this script in this directory to generate protobuf files for the .proto files.

Protobuf Structure:

message CarStateMessage {

    required uint32 datetime = 1;

    required uint32 board_id = 2;

    

    // Vehicle computer

    // BMS

    // Pedal variables

    // Steering wheel

}

