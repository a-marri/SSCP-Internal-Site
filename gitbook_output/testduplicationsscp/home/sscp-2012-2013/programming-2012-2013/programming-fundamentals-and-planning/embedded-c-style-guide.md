# SSCP - Embedded C Style Guide

# Embedded C Style Guide

As a general reference, we're using the Google style guide: http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml.  Obviously this is for C++, so we're modifying it for our purposes here.

[http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Function_Parameter_Ordering)

More relevant (especially if you know good C style already) is to be sure to read:

http://www.netrino.com/Embedded-Systems/How-To/Bug-Killing-Standards-for-Embedded-C

[http://www.netrino.com/Embedded-Systems/How-To/Bug-Killing-Standards-for-Embedded-C](http://www.netrino.com/Embedded-Systems/How-To/Bug-Killing-Standards-for-Embedded-C)

http://www.netrino.com/Embedded-Systems/How-To/More-Bug-Killing-Standards-for-Embedded-C

[http://www.netrino.com/Embedded-Systems/How-To/More-Bug-Killing-Standards-for-Embedded-C](http://www.netrino.com/Embedded-Systems/How-To/More-Bug-Killing-Standards-for-Embedded-C)

And as a reference, here are the JPL standards for code, including the code on Curiosity:

http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf 

[http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf ](http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf)

File format:

* Tabs are 4 spaces (and not the 'tab' character)Unix or Windows Format is OK (Ride7 doesn't care)
* Tabs are 4 spaces (and not the 'tab' character)
* Unix or Windows Format is OK (Ride7 doesn't care)

* Tabs are 4 spaces (and not the 'tab' character)
* Unix or Windows Format is OK (Ride7 doesn't care)

Tabs are 4 spaces (and not the 'tab' character)

Unix or Windows Format is OK (Ride7 doesn't care)

Indentation / Bracketing scheme:

NOTE - ALWAYS SURROUND BLOCKS OF CODE WITH { and }.  NOT DOING THIS CAN LEAD TO BUGS WHEN YOU ADD FUNCTIONALITY LATER.  DON'T BE LAZY.

int main()

{

    if(a == b)

    {

        foo();

    }

}

Data Types:

When possible, use (u)int8_t, (u)int16_t, etc, etc instead of char/short/int/long.  This adds clarity to how much data you plan to store as the traditional data types are loosely defined.

Naming scheme:

Global Variables:

Prepend globals with g_.  This puts them in their own namespace and helps make it easier to avoid naming collisions.

Static Global Variables:

Prepend static local variables with _.  Same idea, but to avoid collisions with local variables/arguments in module functions.

Function Arguments / Local Variables:

camelCase, with the first letter lower case.

Struct Members:

camelCase, with the first letter lower case.

Function naming:

CamelCase, but with the first letter capitalized.

File naming:

name_stuff_like_this.c

Struct Design:

There are two separate cases where you will use structs in embedded code:

* Bit-packed structs for data transmissionNot necessarily bit-packed structs for state storage
* Bit-packed structs for data transmission
* Not necessarily bit-packed structs for state storage

1. Bit-packed structs for data transmission
2. Not necessarily bit-packed structs for state storage

Bit-packed structs for data transmission

Not necessarily bit-packed structs for state storage

Module design:

* Use static global variables for module-specific global stateImplement interfaces in .h files, module-specific code in .c filesIn general, pass a pointer to the object you are manipulating in the module as the first argument of any module-specific functions (the context for that function)
* Use static global variables for module-specific global state
* Implement interfaces in .h files, module-specific code in .c files
* In general, pass a pointer to the object you are manipulating in the module as the first argument of any module-specific functions (the context for that function)

* Use static global variables for module-specific global state
* Implement interfaces in .h files, module-specific code in .c files
* In general, pass a pointer to the object you are manipulating in the module as the first argument of any module-specific functions (the context for that function)

Use static global variables for module-specific global state

Implement interfaces in .h files, module-specific code in .c files

In general, pass a pointer to the object you are manipulating in the module as the first argument of any module-specific functions (the context for that function)

Memory Management:

* Don't use malloc unless absolutely necessary - stick to static allocation (probably as a static global in your main module or a local variable in your main function), and then pass a pointer to that to your various helper functions.If you're using free, you're probably doing something wrong.Be aware of the memory limits of the device and the worst case for memory usage.  These sorts of issues are extremely hard to debug.
* Don't use malloc unless absolutely necessary - stick to static allocation (probably as a static global in your main module or a local variable in your main function), and then pass a pointer to that to your various helper functions.
* If you're using free, you're probably doing something wrong.
* Be aware of the memory limits of the device and the worst case for memory usage.  These sorts of issues are extremely hard to debug.

* Don't use malloc unless absolutely necessary - stick to static allocation (probably as a static global in your main module or a local variable in your main function), and then pass a pointer to that to your various helper functions.
* If you're using free, you're probably doing something wrong.
* Be aware of the memory limits of the device and the worst case for memory usage.  These sorts of issues are extremely hard to debug.

Don't use malloc unless absolutely necessary - stick to static allocation (probably as a static global in your main module or a local variable in your main function), and then pass a pointer to that to your various helper functions.

If you're using free, you're probably doing something wrong.

Be aware of the memory limits of the device and the worst case for memory usage.  These sorts of issues are extremely hard to debug.

