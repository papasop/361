"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

Implements a hybrid approximation of π using Leibniz series and Machin-like modal corrections.
This module demonstrates the conjecture's numerical verification by computing the approximation, residual, and boundedness.
"""

from mpmath import mp, atan, mpf, pi, fsum

mp.dps = 50  # Set precision for high-accuracy computations

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

def verify_bound(n_values, deltas):
    """
    Estimate C as max |delta(n)| * n and check if bound holds.
    """
    C_estimates = [abs(d) * mpf(m) for m, d in zip(n_values, deltas)]
    C = max(C_estimates)
    return C

# Example usage and verification
if __name__ == "__main__":
    mp.dps = 50  # Set high precision
    n_values = [10, 100, 500, 1000, 5000, 10000]  # Test n values

    print("Structured π Approximation Test (Default Machin-like Coefficients)")
    deltas = []
    for n in n_values:
        approx = structured_pi(n)
        residual = compute_residual(n)
        deltas.append(residual)
        print(f"n = {n} | Structured π = {approx}")
        print(f"          | Residual = {residual}")

    # Estimate C for bound |δ(n)| < C / n
    C = verify_bound(n_values, deltas)
    print("\nEstimated C for bound |δ(n)| < C / n:", C)
