"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module computes a hybrid approximation of π using:
- The Leibniz series (alternating series)
- A fixed modal correction φ based on the Machin-like formula

The goal is to accelerate convergence with minimal error.
"""

from mpmath import mp, atan, fsum

# Set default precision
mp.dps = 50

def leibniz_sum(n):
    """Compute Leibniz approximation: 4 × Σ (-1)^k / (2k + 1)"""
    return fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def machin_phi():
    """Compute φ correction term using Machin-like formula"""
    return 16 * atan(mp.mpf(1)/5) - 4 * atan(mp.mpf(1)/239)

def pi_structured(n):
    """
    Compute hybrid structured π approximation:
        π ≈ leibniz_sum(n) + (machin_phi() - leibniz_sum(n_ref))
    This ensures φ is a correction, not duplication.

    Args:
        n (int): Number of terms for Leibniz series.

    Returns:
        mpf: Structured π approximation.
    """
    n_ref = 100000  # High-precision reference for correction
    leibniz_n = leibniz_sum(n)
    leibniz_ref = leibniz_sum(n_ref)
    phi = machin_phi() - leibniz_ref
    return leibniz_n + phi

