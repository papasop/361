"""
Structured Pi Approximation Module (Adjustable)
Author: Y.Y.N. Li
Date: 2025-07-14

π ≈ Leibniz(n) + α · φ
- Leibniz(n): partial alternating series
- φ: modal correction (Machin-like)
- α: correction weight parameter

Residual ≈ O(1/n), tunable via α
"""

from mpmath import mp, mpf, fsum, atan

mp.dps = 50  # high precision

# --- Modal correction φ (Machin-like) ---
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
    return fsum([mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

# --- Structured approximation with α φ ---
def pi_structured(n=1000, alpha=1.0):
    """
    Structured π approximation:
        π ≈ Leibniz(n) + α · φ

    Parameters:
        n (int): terms in the Leibniz series
        alpha (float): scaling factor for φ

    Returns:
        mpf: approximation of π
    """
    phi = compute_phi()
    return leibniz_sum(n) + mpf(alpha) * phi

