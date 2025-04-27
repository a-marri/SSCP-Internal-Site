# SSCP - Code 2020-2021

# Code 2020-2021

Welcome to the Code Team Sub-page! 

Here you'll find information about current projects and the tools we use to fulfill them. You'll also find some FAQs, teaching tools, and information regarding safety.

Questions? Feel free to reach out!

 Sub-team Leadership

 Ethan Li (Former Code Lead)

 Maisam Pyarali (Engineering Director)

 Contact

ethansli@stanford.edu

maisam@stanford.edu

## Design Philosophy

[](#h.7ur8b4ghrfd)

In old fashion software development routine, we tend to write a part of code, then start testing and finding the bugs. That would not be pleasant experience especially when the bugs shown up and we were shaking our heads about where to start digging from.

In TDD, on the other hand, test cases are driving your software development. When developing a function (unit of a code), you start by writing a small test to fail, then you write a simplest code to pass the test, then you will refactor the code. Next, you do the loop again, write another test, write the code to pass the test, refactor, Test, Code, Refactor. You will do the loop until you finished developing a particular function.

![](../../../assets/image_fb4c6baabb.png)

Source: TDD for Embedded C by James W. Grenning

A good place to start is to refer to the below documentation:

1. The bible of STM32F4 Micro controllers. It's greatly detailed

[ The bible of STM32F4 Micro controllers.](https://www.st.com/resource/en/user_manual/dm00105879-description-of-stm32f4-hal-and-ll-drivers-stmicroelectronics.pdf)

2. Everything FreeRTOS and why we use it

[ Everything FreeRTOS and why we use it](https://www.freertos.org/wp-content/uploads/2018/07/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf)

3. FreeRTOS Reference Manual

[ FreeRTOS Reference Manual](https://www.freertos.org/wp-content/uploads/2018/07/FreeRTOS_Reference_Manual_V10.0.0.pdf)

