# SSCP - Luminos: Optimization Approach

# Luminos: Optimization Approach

The optimizing solver was run in conjunction with the constant airspeed solver, and both agreed within a few kph during WSC2013

Plans for WSC 2013

I've been looking into possible algorithms to do constrained optimization. I think I now have an idea on how this can be done.

First we need to write an objective function, f(v), which it takes in a velocity vector (dimension 3000) and outputs the total time of the trip. (we are close to being done with this I think)

This has to be subject to a bunch of constraints, such as the battery charge cannot become negative. 

Constraints can be imposed by log barrier functions (choose one from this list).

[barrier functions](http://en.wikipedia.org/wiki/Barrier_function)

[this list](http://www.math.ucsd.edu/~njw/Teaching/Math271C/Lecture_07.pdf)

Then we would need to calculate the gradient of the objective function (which is also a dimension 3000 vector with the approx. gradient of each route segment)

This can be done fairly easily with the method of finite differences.

[method of finite differences](http://en.wikipedia.org/wiki/Finite_difference_method)

Then, we can try a slew of optimizations methods such as the following. In the order of increasing difficulty :P

- Coordinate descent

[Coordinate descent](http://en.wikipedia.org/wiki/Coordinate_descent)

- Gradient descent

[Gradient descent](http://en.wikipedia.org/wiki/Gradient_descent)

- Projected gradient descent (Need to think about how to calculate the projection...)

In the case that we can get our objective to be convex... (I'm not sure if this is even possible, but it might be)

- minFunc (a library with ALL THE OPTIMIZATION) 

[minFunc](http://www.di.ens.fr/~mschmidt/Software/minFunc.html)

- LBFGS 

[LBFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS)

- Stochastic Gradient descent

[Stochastic Gradient descent](http://en.wikipedia.org/wiki/Stochastic_gradient_descent)

The following are numerical methods that don't require the gradient, but they might be less accurate?

- Simulated annealing

[Simulated annealing](http://en.wikipedia.org/wiki/Simulated_annealing)

- Nelder mead

[Nelder mead](http://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method)

There are tons of other optimizations we can use: Mathematical Optimization

[Mathematical Optimization](http://en.wikipedia.org/wiki/Mathematical_optimization)

Oh and we should use constant speed and/or random speed as our baseline.

Sam Patterson from UNSW Sunswift offered to let us use their Weatherzone data for 2013. Email him at sam.paterson@sunswift.unsw.edu.au if we need their data.

