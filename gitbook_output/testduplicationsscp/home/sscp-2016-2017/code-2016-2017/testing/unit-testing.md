# SSCP - Unit Testing

# Unit Testing

We're using CppUTest (https://github.com/cpputest/cpputest) for unit testing, since we can directly run unit tests for our projects within IAR.

[https://github.com/cpputest/cpputest](https://github.com/cpputest/cpputest)

Documentation: http://cpputest.github.io/manual.html

[http://cpputest.github.io/manual.html](http://cpputest.github.io/manual.html)

More detailed documentation for IAR projects specifically: https://cpputest.github.io/stories.html (Note that a number of things that they recommend are not necessary, such as removing warnings or making specific changes to library files.)

[https://cpputest.github.io/stories.html](https://cpputest.github.io/stories.html)

How to create unit tests for a project (note: this assumes that you are writing a unit test for an actual IAR project.)

* Open the original workspace for the project to be tested.While you are in this workspace, go to project -> Create New Project...In the "Create New Project" popup, choose the C++ project with an empty main.cpp file.Make the following changes to the project's options by navigating to Project -> Options:General Options -> Processor Variant -> Device -> Set to STM32F407VGC/C++ Compiler -> Language 1 -> Language = AutoC/C++ Compiler -> Language 1 -> C++ Dialect = C++C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)In the project directory you created, create a tests directory. Add a file AllTests.cpp in this tests directory with the following code:
* Open the original workspace for the project to be tested.
* While you are in this workspace, go to project -> Create New Project...
* In the "Create New Project" popup, choose the C++ project with an empty main.cpp file.
* Make the following changes to the project's options by navigating to Project -> Options:General Options -> Processor Variant -> Device -> Set to STM32F407VGC/C++ Compiler -> Language 1 -> Language = AutoC/C++ Compiler -> Language 1 -> C++ Dialect = C++C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)
* General Options -> Processor Variant -> Device -> Set to STM32F407VG
* C/C++ Compiler -> Language 1 -> Language = Auto
* C/C++ Compiler -> Language 1 -> C++ Dialect = C++
* C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)
* In the project directory you created, create a tests directory. Add a file AllTests.cpp in this tests directory with the following code:

1. Open the original workspace for the project to be tested.
2. While you are in this workspace, go to project -> Create New Project...
3. In the "Create New Project" popup, choose the C++ project with an empty main.cpp file.
4. Make the following changes to the project's options by navigating to Project -> Options:General Options -> Processor Variant -> Device -> Set to STM32F407VGC/C++ Compiler -> Language 1 -> Language = AutoC/C++ Compiler -> Language 1 -> C++ Dialect = C++C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)
5. General Options -> Processor Variant -> Device -> Set to STM32F407VG
6. C/C++ Compiler -> Language 1 -> Language = Auto
7. C/C++ Compiler -> Language 1 -> C++ Dialect = C++
8. C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)
9. In the project directory you created, create a tests directory. Add a file AllTests.cpp in this tests directory with the following code:

Open the original workspace for the project to be tested.

While you are in this workspace, go to project -> Create New Project...

In the "Create New Project" popup, choose the C++ project with an empty main.cpp file.

Make the following changes to the project's options by navigating to Project -> Options:

1. General Options -> Processor Variant -> Device -> Set to STM32F407VG
2. C/C++ Compiler -> Language 1 -> Language = Auto
3. C/C++ Compiler -> Language 1 -> C++ Dialect = C++
4. C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)

General Options -> Processor Variant -> Device -> Set to STM32F407VG

C/C++ Compiler -> Language 1 -> Language = Auto

C/C++ Compiler -> Language 1 -> C++ Dialect = C++

C/C++ Compiler -> Preprocessor -> Additional include directories -> Add $PROJ_DIR$/../lib/cpputest. Add any additional directories for which you need files for testing. (Often, you can just copy the include directories from the desired project to be tested.)

In the project directory you created, create a tests directory. Add a file AllTests.cpp in this tests directory with the following code:

* #include "CppUTest/CommandLineTestRunner.h"int main(int ac, char** av){  const char * av_override[] = { "exe", "-v" }; //turn on verbose mode  //return CommandLineTestRunner::RunAllTests(ac, av);  return CommandLineTestRunner::RunAllTests(2, av_override);}
* #include "CppUTest/CommandLineTestRunner.h"int main(int ac, char** av){  const char * av_override[] = { "exe", "-v" }; //turn on verbose mode  //return CommandLineTestRunner::RunAllTests(ac, av);  return CommandLineTestRunner::RunAllTests(2, av_override);}
* #include "CppUTest/CommandLineTestRunner.h"
* int main(int ac, char** av)
* {
*   const char * av_override[] = { "exe", "-v" }; //turn on verbose mode
*   //return CommandLineTestRunner::RunAllTests(ac, av);
*   return CommandLineTestRunner::RunAllTests(2, av_override);
* }

* #include "CppUTest/CommandLineTestRunner.h"int main(int ac, char** av){  const char * av_override[] = { "exe", "-v" }; //turn on verbose mode  //return CommandLineTestRunner::RunAllTests(ac, av);  return CommandLineTestRunner::RunAllTests(2, av_override);}
* #include "CppUTest/CommandLineTestRunner.h"
* int main(int ac, char** av)
* {
*   const char * av_override[] = { "exe", "-v" }; //turn on verbose mode
*   //return CommandLineTestRunner::RunAllTests(ac, av);
*   return CommandLineTestRunner::RunAllTests(2, av_override);
* }

* #include "CppUTest/CommandLineTestRunner.h"
* int main(int ac, char** av)
* {
*   const char * av_override[] = { "exe", "-v" }; //turn on verbose mode
*   //return CommandLineTestRunner::RunAllTests(ac, av);
*   return CommandLineTestRunner::RunAllTests(2, av_override);
* }

#include "CppUTest/CommandLineTestRunner.h"

int main(int ac, char** av)

{

  const char * av_override[] = { "exe", "-v" }; //turn on verbose mode

  //return CommandLineTestRunner::RunAllTests(ac, av);

  return CommandLineTestRunner::RunAllTests(2, av_override);

}

* In the tests directory, add cpp files describing each of your tests, using the following format:
* In the tests directory, add cpp files describing each of your tests, using the following format:

1. In the tests directory, add cpp files describing each of your tests, using the following format:

In the tests directory, add cpp files describing each of your tests, using the following format:

* extern "C"{  // Include c files from your project in this block!  // If you don't do this, you will get a mysterious error.}#include "CppUTest/TestHarness.h"TEST_GROUP(FirstTestGroup){  void setup() {    // Put setup code here. The setup code is run before each test,    // and each test runs independently of each other.  }  void teardown() {    // Put teardown code here. The teardown code is run after each test,    // and each test runs independently of each other.  }};TEST(FirstTestGroup, FirstTest){  FAIL("Fail me!");  // Should fail}TEST(FirstTestGroup, SecondTest){  STRCMP_EQUAL("hello", "world");  // Should also fail}
* extern "C"
* {
*   // Include c files from your project in this block!
*   // If you don't do this, you will get a mysterious error.
* }
* #include "CppUTest/TestHarness.h"
* TEST_GROUP(FirstTestGroup)
* {
*   void setup() {
*     // Put setup code here. The setup code is run before each test,
*     // and each test runs independently of each other.
*   }
*   void teardown() {
*     // Put teardown code here. The teardown code is run after each test,
*     // and each test runs independently of each other.
*   }
* };
* TEST(FirstTestGroup, FirstTest)
* {
*   FAIL("Fail me!");  // Should fail
* }
* TEST(FirstTestGroup, SecondTest)
* {
*   STRCMP_EQUAL("hello", "world");  // Should also fail
* }

* extern "C"
* {
*   // Include c files from your project in this block!
*   // If you don't do this, you will get a mysterious error.
* }
* #include "CppUTest/TestHarness.h"
* TEST_GROUP(FirstTestGroup)
* {
*   void setup() {
*     // Put setup code here. The setup code is run before each test,
*     // and each test runs independently of each other.
*   }
*   void teardown() {
*     // Put teardown code here. The teardown code is run after each test,
*     // and each test runs independently of each other.
*   }
* };
* TEST(FirstTestGroup, FirstTest)
* {
*   FAIL("Fail me!");  // Should fail
* }
* TEST(FirstTestGroup, SecondTest)
* {
*   STRCMP_EQUAL("hello", "world");  // Should also fail
* }

extern "C"

{

  // Include c files from your project in this block!

  // If you don't do this, you will get a mysterious error.

}

#include "CppUTest/TestHarness.h"

TEST_GROUP(FirstTestGroup)

{

  void setup() {

    // Put setup code here. The setup code is run before each test,

    // and each test runs independently of each other.

  }

  void teardown() {

    // Put teardown code here. The teardown code is run after each test,

    // and each test runs independently of each other.

  }

};

TEST(FirstTestGroup, FirstTest)

{

  FAIL("Fail me!");  // Should fail

}

TEST(FirstTestGroup, SecondTest)

{

  STRCMP_EQUAL("hello", "world");  // Should also fail

}

* Add these test files created above to the project within IAR.Add the file lib/cpputest/cpputest.a to the project.Add any other solar car library files that are needed to run.Remove main.cpp from the project and delete it from the project directory.Run your unit tests as you would a normal IAR project. 
* Add these test files created above to the project within IAR.
* Add the file lib/cpputest/cpputest.a to the project.
* Add any other solar car library files that are needed to run.
* Remove main.cpp from the project and delete it from the project directory.
* Run your unit tests as you would a normal IAR project. 

1. Add these test files created above to the project within IAR.
2. Add the file lib/cpputest/cpputest.a to the project.
3. Add any other solar car library files that are needed to run.
4. Remove main.cpp from the project and delete it from the project directory.
5. Run your unit tests as you would a normal IAR project. 

Add these test files created above to the project within IAR.

Add the file lib/cpputest/cpputest.a to the project.

Add any other solar car library files that are needed to run.

Remove main.cpp from the project and delete it from the project directory.

Run your unit tests as you would a normal IAR project. 

