# SSCP - Software Considerations

# Software Considerations

When designing software, there are several overall considerations to bear in mind before starting the project.

1. Portability. This is one of the most important criteria for software projects that are going to get used on the race. S*** breaks in Australia and we may need to swap out laptops at short notice. Every critical software package should be designed such that on a freshly installed OS, the steps to getting your package to run are as minimal as possible; ideally the flow should be something similar to checking out the repo, running './configure' and 'make' (if relevant) and executing the resultant executable. This means careful library choices, lots of testing on different systems, and meticulous logging of dependencies.

