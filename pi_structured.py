"""
Structured Pi Approximation Module 
Author: Y.Y.N. Li
Date: 2025-07-14

This module approximates π using a structured formula:
    π ≈ Leibniz(n) + α(n) * φ
where:
    - Leibniz(n): partial sum of the Leibniz series
    - φ: constant Machin-like correction term
    - α(n): decay factor, e.g. α(n) = 1/n^p (p ∈ (0.5, 2.0))

This improves convergence without overcorrecting.
"""

from mpmath import mp, mpf, fsum, atan

# Set default decimal precision
mp.dps = 50

# --- Constant Machin-like correction φ ---
def compute_phi():
    return 4 * atan(mpf(1) / 5) - atan(mpf(1) / 239)

# --- Leibniz partial sum ---
def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# --- Structured π approximation with α(n) decay ---
def pi_structured(n=1000, p=1.0):
    """
    Approximates π using structured series:
        π ≈ Leibniz(n) + α(n) * φ

    Parameters:
        n (int): Number of Leibniz terms
        p (float): Decay exponent for α(n) = 1 / n^p

    Returns:
        mpf: Approximate value of π
    """
    alpha = mpf(1) / n**p
    return leibniz_sum(n) + alpha * compute_phi()

n_values = [10, 100, 500, 1000, 5000, 10000]
deltas = [compute_residual(n) for n in n_values]
C = max(abs(d) * mpf(m) for m, d in zip(n_values, deltas))
print("\nEstimated C:", C)
