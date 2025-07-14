# test_structured_pi.py
# Test for Structured Pi Approximation
# Author: Y.Y.N. Li

from pi_structured import pi_structured
from mpmath import mp, mpf

mp.dps = 50  # Set precision

def run_tests():
    steps = [10, 100, 500, 1000, 5000, 10000]
    for n in steps:
        approx_pi = pi_structured(n)
        true_pi = mp.pi
        residual = abs(approx_pi - true_pi)
        print(f"n = {n:<6} | Structured π ≈ {approx_pi}")
        print(f"         | Residual     = {residual}")
        print("-" * 65)

        # Optional: Assertion (basic threshold check)
        if n >= 1000:
            assert residual < mpf('0.001'), f"Residual too large for n = {n}"

if __name__ == "__main__":
    run_tests()
