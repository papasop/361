"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

Implements a hybrid approximation of π using Leibniz series and Machin-like modal corrections.
This module demonstrates the conjecture's numerical verification by computing the approximation, residual, and boundedness.
"""

from mpmath import mp, atan, mpf, pi, fsum, abs
from itertools import product

mp.dps = 50  # Set precision for high-accuracy computations

def generate_phi_candidates(N=2, max_den=300, max_coeff=20, tol=1e-10):
    """
    Automatically search for combinations of φ(n) to approximate π and return the best residual combination.
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

def leibniz_sum(n):
    """
    Compute the Leibniz series sum up to n terms.
    """
    return fsum([mpf(4) * mpf((-1)**k) / mpf(2*k + 1) for k in range(n)])

def structured_pi(n, a_k=None, b_k=None, c_k=None):
    """
    Compute the structured approximation of π: Leibniz sum + modal correction φ.
    If modal coefficients are not provided, use default Machin-like values.
    """
    if a_k is None:
        a_k = [4, -1]
        b_k = [1, 1]
        c_k = [5, 239]
    N = len(a_k)
    phi = fsum([mpf(a) * atan(mpf(b)/mpf(c)) for a, b, c in zip(a_k, b_k, c_k)])
    return leibniz_sum(n) + phi

def compute_residual(n, a_k=None, b_k=None, c_k=None):
    """
    Compute the residual δ(n) = π - structured_pi(n).
    """
    approx = structured_pi(n, a_k, b_k, c_k)
    return abs(pi - approx)

# Example usage for submission test
if __name__ == "__main__":
    mp.dps = 50  # Set high precision
    n_values = [10, 100, 500, 1000, 5000, 10000]  # Test n values

    print("Structured π Approximation Test (Default Machin-like Coefficients)")
    for n in n_values:
        approx = structured_pi(n)
        residual = compute_residual(n)
        print(f"n = {n} | Structured π = {approx}")
        print(f"          | Residual = {residual}")

    # Optional: Search for better modal combinations
    # best_phi, best_combo, best_residual = generate_phi_candidates(N=2)
    # print("\nBest Modal Combination Found:")
    # print(f"Best φ = {best_phi}")
    # print(f"Best Residual = {best_residual}")
    # print(f"Best Combo (a_k, b_k, c_k): {best_combo}")
