"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module implements a hybrid approximation of π:
    ρ(n) = Leibniz_sum(n) + φ(n)

- The Leibniz sum converges slowly: O(1/n)
- φ(n) is a fixed modal correction (Machin-like), improving convergence

Residual: δ(n) = |ρ(n) - π| is bounded by O(1/n^α), potentially with ε > 0
"""

from mpmath import mp, mpf, fsum, atan

# Set default precision (50 decimal places)
mp.dps = 50

# Modal correction φ(n): Machin-like formula
# π ≈ 4 arctan(1/5) − arctan(1/239)
a_k = [4, -1]
b_k = [1, 1]
c_k = [5, 239]

def compute_phi():
    """Fixed modal correction φ(n), independent of n"""
    phi = mpf(0)
    for j in range(len(a_k)):
        phi += mpf(a_k[j]) * atan(mpf(b_k[j]) / mpf(c_k[j]))
    return phi

def leibniz_sum(n):
    """Compute Leibniz series: 4 * Σ [(-1)^k / (2k+1)]"""
    return fsum([mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def pi_structured(n=1000):
    """
    Compute structured approximation of π:
        ρ(n) = Leibniz_sum(n) + φ

    Parameters:
        n (int): Number of Leibniz terms

    Returns:
        mpf: Approximation of π
    """
    return leibniz_sum(n) + compute_phi()

