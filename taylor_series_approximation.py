import numpy as np
import matplotlib.pyplot as plt

# The function to approximate
f = lambda x: 1/(1+x**2)

# The first n terms in the Taylor (Maclaurin) Series for f(x)
def taylor_approximation(x, n):
    approx = 0
    for k in range(1, n+1):
        approx += (-1)**(k+1)*(1/x**(2*k))
    return approx

# Plot the function and the Taylor Series at several orders
x = np.linspace(1, 5, 1000)
plt.plot(x, f(x), color='b', label='$f(x)$')

for n in range(2, 11, 2):
    plt.plot(x, taylor_approximation(x, n), color=(1-.083*n, 0, 0.083*n), label=
             'Order-{} Taylor Polynomial'.format(n))
    
plt.legend()
plt.grid()
plt.show()
