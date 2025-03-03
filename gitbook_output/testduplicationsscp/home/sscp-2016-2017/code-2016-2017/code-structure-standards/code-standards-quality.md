# SSCP - Code Standards & Quality

# Code Standards & Quality

This document outlines SSCP's coding style and practices.

Everything explicitly written on this page should be followed to the letter, unless there is a compelling reason not to. Style consistency across files will make it SO much easier for future members to understand what the code is doing, so please follow these guidelines. For all guidelines not explicitly specified here, default to the Google Style Guide for C/C++ for the formatting of your code.

[ Google Style Guide](https://google.github.io/styleguide/cppguide.html)

Naming:

* File names should be of the form layer_file_name.h/ceg.  app_driver_controls.c   or    dev_adc.hFunction names should be UpperCamelCaseVariable names should be lower_case_with_underscores
* File names should be of the form layer_file_name.h/ceg.  app_driver_controls.c   or    dev_adc.h
* eg.  app_driver_controls.c   or    dev_adc.h
* Function names should be UpperCamelCase
* Variable names should be lower_case_with_underscores

* File names should be of the form layer_file_name.h/ceg.  app_driver_controls.c   or    dev_adc.h
* eg.  app_driver_controls.c   or    dev_adc.h
* Function names should be UpperCamelCase
* Variable names should be lower_case_with_underscores

File names should be of the form layer_file_name.h/c

* eg.  app_driver_controls.c   or    dev_adc.h

eg.  app_driver_controls.c   or    dev_adc.h

Function names should be UpperCamelCase

Variable names should be lower_case_with_underscores

* Variable and function names should be non-ambiguous. Prefer longer names over ambiguous abbreviations.As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.
* As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.
* As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.

Variable and function names should be non-ambiguous. Prefer longer names over ambiguous abbreviations.

* As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.
* As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.

* As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.

As an example, the variable name min could mean any of the following: minute, minimum, motor identification number, or Minnesota.

* The variable name curr could mean electrical current, current time, or black currant jam.So make sure it's clear.
* The variable name curr could mean electrical current, current time, or black currant jam.
* So make sure it's clear.

* The variable name curr could mean electrical current, current time, or black currant jam.
* So make sure it's clear.

The variable name curr could mean electrical current, current time, or black currant jam.

So make sure it's clear.

Code Structure:

* Always include an else after any if statement that has an else if, even if the else is empty (this shows that the programmer thought about the else case and intentionally left it empty).
* Use if (constant == variable) instead of if (variable == constant) so the consequences will be less severe if you forget or accidentally delete one of the = signs.
* Put brackets on a new line so they can be more easily matched up
* Don't have any public data -- if you need it in another module, use getter and setter functions.
* Have only one file ever modifying a variable -- all others only access it
* Go heavy on the ENUMs and structs to make things more organized and easier to trace (better than solo variables and a bunch of #DEFINEs)

Always include an else after any if statement that has an else if, even if the else is empty (this shows that the programmer thought about the else case and intentionally left it empty).

Use if (constant == variable) instead of if (variable == constant) so the consequences will be less severe if you forget or accidentally delete one of the = signs.

Put brackets on a new line so they can be more easily matched up

Don't have any public data -- if you need it in another module, use getter and setter functions.

Have only one file ever modifying a variable -- all others only access it

Go heavy on the ENUMs and structs to make things more organized and easier to trace (better than solo variables and a bunch of #DEFINEs)

Variables, Constants, etc.:

* NEVER have magic numbers. At the very least create a #define with a descriptive name and use that. CS classes will probably have taught you this already, but I want to reiterate it again - there will be many other people reading, rewriting, and generally trying to maintain your code. They can't read your mind. Save them some time and don't just plop numbers down, even if you think they're obvious in the moment.
* We always use the size-specific version of variables:NO char | YES uint8_tNO int   | YES int32_tNO uint | YES uint32_t Obviously we still use floats and doubles. The only exception to all of this is if you actually have an array of letter characters. Then you can use a char array.In order to use these variables in a file, you need to include the following line at the top of the file:  #define <stdint.h>
* NO char | YES uint8_t
* NO int   | YES int32_t
* NO uint | YES uint32_t 
* Obviously we still use floats and doubles. The only exception to all of this is if you actually have an array of letter characters. Then you can use a char array.
* In order to use these variables in a file, you need to include the following line at the top of the file:  #define <stdint.h>

NEVER have magic numbers. At the very least create a #define with a descriptive name and use that. CS classes will probably have taught you this already, but I want to reiterate it again - there will be many other people reading, rewriting, and generally trying to maintain your code. They can't read your mind. Save them some time and don't just plop numbers down, even if you think they're obvious in the moment.

[magic numbers](https://en.wikipedia.org/wiki/Magic_number_%28programming%29#Unnamed_numerical_constants)

We always use the size-specific version of variables:

* NO char | YES uint8_t
* NO int   | YES int32_t
* NO uint | YES uint32_t 
* Obviously we still use floats and doubles. The only exception to all of this is if you actually have an array of letter characters. Then you can use a char array.
* In order to use these variables in a file, you need to include the following line at the top of the file:  #define <stdint.h>

NO char | YES uint8_t

NO int   | YES int32_t

NO uint | YES uint32_t 

Obviously we still use floats and doubles. The only exception to all of this is if you actually have an array of letter characters. Then you can use a char array.

In order to use these variables in a file, you need to include the following line at the top of the file:  #define <stdint.h>

Maintenance:

* Add  #pragma once  to the top of all of your .h files (to prevent multiple includes)Comment every function. Without exception. Do this in the .h file if there is a function declaration. Commenting when you write the function is much easier than doing it days, weeks, or months later.Comments should read like a sentence. Capitalize the first letter and end with a period.
* Add  #pragma once  to the top of all of your .h files (to prevent multiple includes)
* Comment every function. Without exception. Do this in the .h file if there is a function declaration. Commenting when you write the function is much easier than doing it days, weeks, or months later.
* Comments should read like a sentence. Capitalize the first letter and end with a period.

* Add  #pragma once  to the top of all of your .h files (to prevent multiple includes)
* Comment every function. Without exception. Do this in the .h file if there is a function declaration. Commenting when you write the function is much easier than doing it days, weeks, or months later.
* Comments should read like a sentence. Capitalize the first letter and end with a period.

Add  #pragma once  to the top of all of your .h files (to prevent multiple includes)

Comment every function. Without exception. Do this in the .h file if there is a function declaration. Commenting when you write the function is much easier than doing it days, weeks, or months later.

Comments should read like a sentence. Capitalize the first letter and end with a period.

* Don't leave commented out code in the final version -- if it's not used, remove it.
* Create todos in the form TODO(name of person responsible): commenteg.   TODO(brandon): Verify this value with GPS speed.
* eg.   TODO(brandon): Verify this value with GPS speed.

Don't leave commented out code in the final version -- if it's not used, remove it.

Create todos in the form TODO(name of person responsible): comment

* eg.   TODO(brandon): Verify this value with GPS speed.

eg.   TODO(brandon): Verify this value with GPS speed.

Other great resources for good coding practices:

* How To - C Language

How To - C Language

[How To - C Language](https://matt.sh/howto-c)

And fun resources:

* How To Write Unmaintainable Code (but seriously, don't follow anything this guide says)

How To Write Unmaintainable Code (but seriously, don't follow anything this guide says)

[How To Write Unmaintainable Code](https://www.se.rit.edu/~tabeec/RIT_441/Resources_files/How%20To%20Write%20Unmaintainable%20Code.pdf)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linters:

Static Analysis:

IAR C-Spy static analysis

Facebook infer: https://github.com/facebook/infer

[https://github.com/facebook/infer](https://github.com/facebook/infer)

Unit Tests:

Should we still do this???:

    Name files and variables so they match

        If file name is app_driverControls.c variables would all be app_driverControls_myVariableName

        Generally, structs are named like app_driverControls_driveData_S app_driverControls_driveData

Interesting things from Tesla's style guide:

* Name files and variables so they matchIf file name is app_driverControls.c variables would all be app_driverControls_myVariableNameGenerally, structs are named like app_driverControls_driveData_S app_driverControls_driveData
* If file name is app_driverControls.c variables would all be app_driverControls_myVariableName
* Generally, structs are named like app_driverControls_driveData_S app_driverControls_driveData

Name files and variables so they match

* If file name is app_driverControls.c variables would all be app_driverControls_myVariableName
* Generally, structs are named like app_driverControls_driveData_S app_driverControls_driveData

If file name is app_driverControls.c variables would all be app_driverControls_myVariableName

Generally, structs are named like app_driverControls_driveData_S app_driverControls_driveData

