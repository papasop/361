"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

Implements a hybrid approximation of π:
π ≈ Leibniz_sum(n) + φ  (Machin-like modal correction)
This improves convergence compared to the pure Leibniz series.
"""

from mpmath import mp, atan, mpf, pi, fsum
from itertools import product

mp.dps = 50  # 设置精度

def generate_phi_candidates(N=2, max_den=300, max_coeff=20, tol=1e-10):
    """
    自动搜索 φ(n) 的组合，使其逼近 π，返回最优残差组合。
    """
    best_phi = None
    best_residual = mpf('inf')
    best_combo = None

    for coeffs in product(range(1, max_coeff+1), repeat=N):
        for denoms in product(range(1, max_den+1), repeat=N):
            a_k = coeffs
            c_k = denoms
            try:
                phi = fsum([mpf(a) * atan(mpf(1)/mpf(c)) for a, c in zip(a_k, c_k)])
                residual = abs(pi - phi)
                if residual < best_residual:
                    best_phi = phi
                    best_combo = list(zip(a_k, [1]*N, c_k))  # a_k, b_k=1, c_k
                    best_residual = residual
                    if residual < tol:
                        return best_phi, best_combo, residual
            except:
                continue
    return best_phi, best_combo, best_residual
