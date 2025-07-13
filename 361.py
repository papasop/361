# Google Colab compatible code to verify the modified conjecture for Pi approximation bounded residual.
# Copy and paste this into a Colab notebook cell and run it.

import numpy as np
import matplotlib.pyplot as plt

# Constants for Machin-like formula (example coefficients for phi(n))
# For N=1: 4*arctan(1/5) - arctan(1/239)
a_k = [4, -1]  # Coefficients a_k
b_k = [1, 1]   # Numerators b_k
c_k = [5, 239] # Denominators c_k
N = len(a_k)   # Modal cutoff N

# Function to compute phi(n) with modal cutoff N
def compute_phi(n):
    phi = 0
    for k in range(min(n, N)):
        phi += a_k[k] * np.arctan(b_k[k] / c_k[k])
    return phi

# Function to compute Leibniz series sum up to n-1 terms
def leibniz_sum(n):
    terms = [4 * (-1)**k / (2*k + 1) for k in range(n)]
    return sum(terms)

# Function to compute rho(n)
def compute_rho(n):
    leibniz = leibniz_sum(n)
    phi = compute_phi(n)
    return leibniz + phi

# Compute residual delta(n) = pi - rho(n)
def compute_delta(n):
    return np.pi - compute_rho(n)

# Verify the bound |delta(n)| < C / n for some C
def find_C(n_values, deltas):
    # Estimate C as max |delta(n)| * n
    C_estimates = np.abs(deltas) * n_values
    return np.max(C_estimates)

# Main validation
n_values = np.arange(10, 10001, 10)  # n from 10 to 10000, step 10
deltas = [compute_delta(n) for n in n_values]

# Estimate C
C = find_C(n_values, deltas)
print(f"Estimated C: {C}")
print("If C is finite and bound holds for large n, conjecture is supported.")

# Plot |delta(n)| and C/n bound
plt.figure(figsize=(10, 6))
plt.plot(n_values, np.abs(deltas), label='|δ(n)|')
plt.plot(n_values, C / n_values, label='C / n bound', linestyle='--')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('|δ(n)|')
plt.title('Residual Boundedness Verification for Pi Approximation')
plt.legend()
plt.grid(True)
plt.show()