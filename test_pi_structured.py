# Test for Structured Pi Approximation
# Author: Y.Y.N. Li

from pi_structured import pi_structured
from mpmath import mp

mp.dps = 50  # Set precision

# Sweep through multiple steps
for n in [10, 100, 500, 1000, 5000, 10000]:
    approx_pi = pi_structured(n)
    residual = abs(approx_pi - mp.pi)
    print(f"n = {n:<6} | Structured π ≈ {approx_pi}")
    print(f"         | Residual     = {residual}")
    print("-" * 65)
