"""
Structured Pi Approximation Module
Author: Y.Y.N. Li
Date: 2025-07-14

This module implements a hybrid approximation of π:
    ρ(n) = Leibniz_sum(n) + φ(n)

- The Leibniz sum converges slowly: O(1/n)
- φ(n) is a fixed modal correction (Machin-like), improving convergence

Residual: δ(n) = |ρ(n) - π| is bounded by O(1/n^α), potentially with ε > 0
"""

from mpmath import mp, mpf, atan, fsum
import numpy as np

# Set high precision
mp.dps = 50

# === φ(n) Modal Residual Generator ===

def generate_phi_modal(n, mode='harmonic', alpha=1.0):
    """
    Generate a structural correction φ(n) based on n.

    Parameters:
        n (int): Number of main series terms.
        mode (str): Type of modal correction ('harmonic', 'inverse-square', 'trainable').
        alpha (float): Scaling factor or decay rate.

    Returns:
        mpf: The structural correction φ(n).
    """
    phi = mpf(0)
    if mode == 'harmonic':
        # φ(n) = Σ (1 / (2k + 1)) / n^α
        phi = fsum([mpf(1)/(2*k+1) for k in range(1, 6)]) / (n ** alpha)
    elif mode == 'inverse-square':
        # φ(n) = Σ (1 / (2k+1)^2) / n^α
        phi = fsum([mpf(1)/(2*k+1)**2 for k in range(1, 6)]) / (n ** alpha)
    elif mode == 'trainable':
        # Placeholder for learning model
        weights = [mpf(0.8), -0.3, 0.15, -0.08, 0.04]
        phi = fsum([weights[k] * atan(mpf(1)/(5+2*k)) for k in range(len(weights))])
        phi /= (n ** alpha)
    else:
        raise ValueError("Unsupported mode.")
    return phi


# === Main Series (Leibniz) + Residual φ(n) ===

def structured_pi(n, mode='harmonic', alpha=1.0):
    leibniz = fsum([mpf(4)*(-1)**k / (2*k + 1) for k in range(n)])
    phi = generate_phi_modal(n, mode=mode, alpha=alpha)
    return leibniz + phi


# === Output Table for Various Modes ===

results = []
n_values = [10, 100, 500, 1000, 5000, 10000]

for mode in ['harmonic', 'inverse-square', 'trainable']:
    for n in n_values:
        approx = structured_pi(n, mode=mode, alpha=1.0)
        residual = abs(approx - mp.pi)
        results.append({
            'n': n,
            'mode': mode,
            'structured_pi': approx,
            'residual': residual
        })

import pandas as pd
from ace_tools import display_dataframe_to_user

df = pd.DataFrame(results)
display_dataframe_to_user("Structured π Approximation with φ(n)", df)

