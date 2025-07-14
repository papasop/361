# Structured Pi Approximation Module
# Copyright (c) 2025 Y.Y.N. Li. MIT License.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp

mp.dps = 50  # High precision

# --- Modal correction φ (Machin-like) ---
def compute_phi():
    a_k = [4, -1]
    b_k = [1, 1]
    c_k = [5, 239]
    return sum(mp.mpf(a) * mp.atan(mp.mpf(b)/mp.mpf(c)) for a, b, c in zip(a_k, b_k, c_k))

# --- Leibniz sum ---
def leibniz_sum(n):
    return mp.fsum([mp.mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# --- Structured π approximation ---
def pi_structured(n):
    return leibniz_sum(n) + compute_phi()

# --- Main test ---
n_vals = np.arange(100, 100001, 500)  # from 100 to 100000
residuals = [abs(mp.pi - pi_structured(n)) for n in n_vals]
C_vals = [residual * n for residual, n in zip(residuals, n_vals)]
C_est = max(C_vals)

print(f"Estimated C ≈ {C_est}")

# --- Plot log-log residual and C/n ---
plt.figure(figsize=(10, 6))
plt.loglog(n_vals, residuals, label='|δ(n)|')
plt.loglog(n_vals, [C_est / n for n in n_vals], '--', label='C/n upper bound')
plt.xlabel("n (terms)")
plt.ylabel("Residual |δ(n)|")
plt.title("Structured π Approximation Residual Decay")
plt.grid(True, which='both', ls='--')
plt.legend()
plt.show()
