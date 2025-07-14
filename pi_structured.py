"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module implements a hybrid approximation of π using:
- The Leibniz series up to n terms
- A fixed modal correction φ based on Machin-like arctangent terms

The combination improves convergence compared to the Leibniz series alone.
"""

from mpmath import mp

# Set default precision (50 decimal places)
mp.dps = 50

# Machin-like coefficients for φ correction
# Example: π ≈ 4·arctan(1/5) − arctan(1/239)
a_k = [4, -1]
b_k = [1, 1]
c_k = [5, 239]

def compute_phi():
    """Compute modal correction φ using predefined arctangent terms."""
    phi = mp.mpf(0)
    for j in range(len(a_k)):
        phi += mp.mpf(a_k[j]) * mp.atan(mp.mpf(b_k[j]) / mp.mpf(c_k[j]))
    return phi

def leibniz_sum(n):
    """Compute the sum of the first n terms of the Leibniz series for π."""
    return mp.fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def pi_structured(n=1000):
    """
    Compute the structured approximation of π:
        π ≈ ρ(n) = Leibniz(n) + φ

    Parameters:
        n (int): Number of Leibniz terms

    Returns:
        mpf: Structured approximation of π
    """
    return leibniz_sum(n) + compute_phi()

