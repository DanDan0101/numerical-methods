# Hello World for PSI Numerical Methods 2026
# Hello World from WSL

import numpy as np
from matplotlib import pyplot as plt

def myexp(x, N=10):
    """
    This function computes exp(x) via the Taylor Series using terms up to
    order N.
    """

    t = 1.0  # The value of the current term
    y = 1.0  # The value of exp(x) up to this point

    # We initialize with the 0th order term, so run the loop
    # for the remaining N terms.
    for i in range(1, N+1):
        t *= x/i  # Update the term: tn = x^n / n!
        y += t    # add tn to y

    # We're done!
    return y


if __name__ == "__main__":

    print("Hello, world!")

    print("e^(1.2)={}".format(np.exp(1.2)))

    x = np.linspace(0, 2 * np.pi, 1000)
    fig, ax = plt.subplots(figsize = (8, 6), dpi = 300, layout = "constrained")
    plt.plot(x, np.sin(x), label = r"$\sin(x)$")
    plt.plot(x, np.cos(x), label = r"$\cos(x)$")
    plt.legend()
    plt.savefig("trig.png")

    # print("e(1) with  5 terms is", myexp(1.0, 5))
    # print("e(1) with 10 terms is", myexp(1.0, 10))
    # print("e(1) with 20 terms is", myexp(1.0, 20))
    # print("e(1) with 40 terms is", myexp(1.0, 40))
