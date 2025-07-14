# Test for Structured Pi Approximation
# Author: Y.Y.N. Li

from pi_structured import pi_structured
from mpmath import mp

mp.dps = 50  # Set precision

n = 1000
approx_pi = pi_structured(n)

print("Structured π ≈", approx_pi)
print("True π       =", mp.pi)
print("Residual     =", abs(approx_pi - mp.pi))
