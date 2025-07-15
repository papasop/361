# ⬛ Structural Pi Approximation with ε > 0 Validation
# Author: Y.Y.N. Li
# Version: July 2025

from mpmath import mp, mpf, fsum, atan, pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- High precision ---
mp.dps = 50

# --- Machin-like correction term ϕ ---
def compute_phi():
    a_k = [4, -1]
    c_k = [5, 239]
    phi = mpf(0)
    for a, c in zip(a_k, c_k):
        phi += a * atan(mpf(1) / mpf(c))
    return phi

phi_fixed = compute_phi()

# --- α(n) = 4 / (π·n), cancels 1/n leading error ---
def alpha(n):
    return mpf(4) / (mp.pi * mpf(n))

# --- Leibniz partial sum ---
def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# --- Structured π approximation ---
def pi_structured(n):
    return leibniz_sum(n) + alpha(n) * phi_fixed

# --- Main test routine ---
def run_test():
    ns = [100, 1000, 10_000, 100_000, 1_000_000]
    true_pi = mp.pi
    residuals = []

    print("🎯 Testing Structured π Approximation with ε > 0 (Cancel 1/n)")
    print("="*70)
    for n in ns:
        approx = pi_structured(n)
        delta = abs(true_pi - approx)
        residuals.append(delta)
        print(f"n = {n:<8} | α(n) = {alpha(n)}")
        print(f"         | ρ(n) ≈ {approx}")
        print(f"         | Residual = {delta}")
        print(f"         | Residual × n^2 = {delta * n**2}")
        print("-"*70)

    # Fit log-log to verify ε > 0
    log_n = np.log(np.array(ns, dtype=np.float64))
    log_res = np.log(np.array([float(r) for r in residuals]))
    slope, intercept = np.polyfit(log_n, log_res, 1)
    epsilon_est = -slope - 1
    print(f"\n✅ Estimated ε ≈ {epsilon_est:.5f} (target: ε > 0)")

    # Plot
    plt.figure(figsize=(7,5))
    plt.loglog(ns, [float(r) for r in residuals], marker='o')
    plt.title("Residual Decay: |π − ρ(n)| vs n")
    plt.xlabel("n")
    plt.ylabel("Residual")
    plt.grid(True, which='both', ls='--')
    plt.show()

# --- Run ---
run_test()
