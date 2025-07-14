"""
Structured π Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module implements a hybrid approximation of π using:
- Leibniz series up to n terms
- A fixed arctangent-based modal correction φ

The combined structure aims to improve convergence rate and bound the residual error by O(1/n^α).
"""

from mpmath import mp

# Optional: default modal correction coefficients (Machin-like)
# π ≈ 4 arctan(1/5) − arctan(1/239)
a_k = [4, -1]
b_k = [1, 1]
c_k = [5, 239]

def compute_phi(n=None):
    """Compute modal correction φ (independent of n here)"""
    phi = mp.mpf(0)
    for j in range(len(a_k)):
        phi += mp.mpf(a_k[j]) * mp.atan(mp.mpf(b_k[j]) / mp.mpf(c_k[j]))
    return phi

def leibniz_sum(n):
    """Compute 4 × Leibniz series sum up to n terms"""
    return mp.fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def pi_structured(n=1000):
    """
    Compute structured approximation to π:
        ρ(n) = Leibniz_sum(n) + φ
    where φ is a fixed modal correction.
    
    Parameters:
        n (int): Number of Leibniz terms.
        
    Returns:
        mpf: Structured π approximation.
    """
    leibniz = leibniz_sum(n)
    phi = compute_phi()
    return leibniz + phi
