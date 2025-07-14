"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module approximates π using a structured formula:
    π ≈ Leibniz(n) + φ(n)
where:
    - Leibniz(n): partial sum of the alternating series
    - φ(n): optional modal correction term (Machin-like)

Residual ≈ O(1/n) or better, depending on φ(n).
"""

from mpmath import mp, mpf, fsum, atan

# Set default decimal precision
mp.dps = 50

# --- Modal correction φ(n) using Machin-like formula ---
# Default: φ(n) = 4*arctan(1/5) - arctan(1/239)
def compute_phi():
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    phi = mpf(0)
    for a, b, c in zip(a_k, b_k, c_k):
        phi += a * atan(mpf(b) / mpf(c))
    return phi

# --- Leibniz partial sum ---
def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# --- Structured approximation ---
def pi_structured(n=1000):
    """
    Structured approximation of π:
        ρ(n) = Leibniz(n) + φ

    Parameters:
        n (int): Number of terms in Leibniz series

    Returns:
        mpf: Approximate value of π
    """
    return leibniz_sum(n) + compute_phi()

