# SSCP - FreeRTOS

# FreeRTOS

### Introduction

[](#h.gyl4hjinp86o)

FreeRTOS is a simple preemptive kernel for microcontrollers. There's a working port for the STM32 series of processors. A daemon runs out of the systick interrupt service routine and handles thread execution.

### Benefits

[](#h.771lpdcfjoln)

In traditional microcontroller programs, all code executes sequentially with linear branching, jumps, and returns. There are many opportunities to hang a program with a busy-wait. It also puts the onus on the programmer to ensure the timings of multiple software routines and the handling of asynchronous data transfer between hardware peripherals and software.

FreeRTOS allows the programmer to write more modular code. Each routine can be represented as an independent infinite loop. Sleep timers and resource locks make it easy to only execute on a certain interval or when some data becomes available. Well-tested locks allow safe interchange of information between interrupt service routes and higher level software. The kernel is preemptive, so it effectively allows from multi-threading. Priority management can ensure that no thread can hog CPU time and hang the program.

### Disadvantages

[](#h.9lguxvvhuo74)

Unfortunately, the initial setup of FreeRTOS is nontrivial. Templates and help from those experienced with it can get around this. More unfortunately, it's possible to have stack overruns and break your code in subtle ways. Mostly these failure modes are detectable, but if you don't know what you're looking for it can make for some nasty debugging. For anything more than the simplest task, the advantages tend to outweigh the disadvantages.

### Example use cases

[](#h.y9k2alw1rx4l)

Imagine that you're writing the firmware for the driver interface. One thread could monitor the buttons and put actions in a queue or update state variables. Another thread could run PID loops for cruise control. Yet another could handle loading and unloading CAN messages from the peripherals. Thread-safe queues provide an efficient means of moving data between the threads. Using such a scheme can dramatically simplify and clarify the code.

Similarly, BMS can benefit from threads. One thread can handle the math surrounding Coulomb counting. A second can run Kalman filters to estimate each module's state of charge. More threads can handle system state machines (precharging, fault, active, etc), CAN transmission and reception, and other housekeeping tasks.

### Documentation

[](#h.gpfq6urs3vv)

Attached is a PDF (do not post on publicly indexed sites or distribute outside SSCP) that has examples of the use of FreeRTOS. API calls are documented on the FreeRTOS website.

[ FreeRTOS website](http://www.freertos.org/modules.html#API_reference)

### Troubleshooting

[](#h.lhj72xqevash)

Thread appears to stop for no apparent reason

The STM32 has 4 bits of priority control. That means when you set an interrupt, you must set its priority from 0-15. Anything lower than 5 means that you can't use any FreeRTOS calls from the interrupt service routine. If you do, you'll derail the task handler and your task may never be executed again. Careful when using example code from around the internet; much of it is designed for processors with many more interrupt priority bits. Many examples will have an ISR configured with a priority of 64 or 128. Doing so will appear to work, but because the lowest bits are all 0 and the STM32 only has 4 usable priority bits, your interrupt will actually be running at priority 0. That means that it can interrupt the kernel.

Thread runs once, never again

Check the value you pass to vTaskDelay.  If it's zero your thread will never run again.  This is only an issue if you are dynamically calculating your delay times.

Wonky behavior - lost data, overruns, etc

Make sure that you've set your linker to provide a reasonable amount of stack and heap space. Default amounts are 512 bytes and 256 bytes respectively. For something as powerful as the STM32F4, the heap size is extremely limiting. For the STM32407VE, a 64KB heap is perfectly reasonable. When instantiating tasks, let FreeRTOS allocate at least 4KB to each task. Using floats in printf or sprintf consumes about 3KB of stack during the function call.

Tips

Queues

There was some fail code in a few places within driver controls. This was the code pattern:

while(1)

{

    if(xQueueReceive(CanRx_tritium_queue, &rxMsg, 0) == pdPASS)

    {

       ...

       vTaskDelay(50);

    }

}

The correct code should be:

while(1)

{

    if(xQueueReceive(CanRx_tritium_queue, &rxMsg, 50) == pdPASS)

    {

       ...

    }

}

Otherwise the loop will only check for values once every 50ms. The Tritium sends us messages far faster than that. The queue fills up and we get noticeable lag and dropped packets.

[](https://drive.google.com/folderview?id=11wfC7HV-lH56BqmCQCU6dRxA0CJYSINy)

### Embedded Google Drive File

Google Drive File: [Embedded Content](https://drive.google.com/embeddedfolderview?id=11wfC7HV-lH56BqmCQCU6dRxA0CJYSINy#list)

<iframe width="100%" height="400" src="https://drive.google.com/embeddedfolderview?id=11wfC7HV-lH56BqmCQCU6dRxA0CJYSINy#list" frameborder="0"></iframe>

