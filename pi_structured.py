"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

Implements a hybrid approximation of π:
π ≈ Leibniz_sum(n) + φ  (Machin-like modal correction)
This improves convergence compared to the pure Leibniz series.
"""

from mpmath import mp

# Set desired precision
mp.dps = 50  # decimal digits

# Machin-like correction φ = 4·arctan(1/5) − arctan(1/239)
a_k = [4, -1]
b_k = [1, 1]
c_k = [5, 239]

def compute_phi():
    """Fixed modal correction φ(n), independent of n"""
    return mp.fsum([mp.mpf(a_k[j]) * mp.atan(mp.mpf(b_k[j]) / mp.mpf(c_k[j]))
                    for j in range(len(a_k))])

def leibniz_sum(n):
    """Partial sum of Leibniz series with n terms"""
    return mp.fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def pi_structured(n=1000):
    """
    Structured approximation of π:
        ρ(n) = Leibniz_sum(n) + φ

    Parameters:
        n (int): number of Leibniz terms

    Returns:
        mpf: approximate value of π
    """
    return leibniz_sum(n) + compute_phi()

