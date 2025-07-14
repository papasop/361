"""
Test script for Structured Pi Approximation
Author: Y.Y.N. Li
Date: 2025-07-14
"""

from pi_structured import pi_structured
from mpmath import mp, mpf, pi
import matplotlib.pyplot as plt

# Set precision
mp.dps = 50

# Config
p = 1.0  # decay exponent for alpha(n) = 1/n^p
n_values = [10, 100, 500, 1000, 5000, 10000]
residuals = []

# Run test for each n
print(f"Testing Structured π Approximation with decay p = {p}")
print("=" * 65)

for n in n_values:
    approx = pi_structured(n, p=p)
    resid = abs(approx - pi)
    residuals.append(resid)

    print(f"n = {n:<6} | Structured π ≈ {approx}")
    print(f"         | Residual     = {resid}")
    print("-" * 65)

# Estimate constant C in bound: |δ(n)| < C / n^p
C_estimates = [res * (n**p) for res, n in zip(residuals, n_values)]
C_max = max(C_estimates)
print(f"Estimated C ≈ {C_max}")

# Optional: Plot log-log residuals
plt.figure(figsize=(8, 5))
plt.loglog(n_values, residuals, marker='o', label='Residual |π - ρ(n)|')
plt.xlabel('n (Leibniz terms)')
plt.ylabel('Residual (log scale)')
plt.title(f'Residual Decay with α(n) = 1/n^{p}')
plt.grid(True, which='both', ls='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
