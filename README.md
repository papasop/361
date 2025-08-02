# Structured Pi and Zeta Approximation via SRC (ρ(n), ζSRC)

This repository implements **Structural Residual Compensation (SRC)** — a symbolic-numeric method to accelerate the convergence of slowly converging series. We provide high-order approximations for:

- The **Leibniz series** for π using a **ninth-order SRC** compensator.
- The **Riemann zeta function** at s = 2 using a **seventh-order SRC** compensator.

## ✨ Key Features

- ✅ Symbolic derivation of compensators via Euler or Bernoulli expansions
- ✅ Verified **O(n⁻⁹)** convergence for π via the Leibniz series
- ✅ Verified **O(n⁻⁷)** convergence for ζ(2) via harmonic inverse square summation
- ✅ High-precision output using `mpmath` (50+ digits)
- ✅ Log-log slope verification, residual decay validation

---

## 📂 File Structure

| File                        | Description |
|----------------------------|-------------|
| `src3.py`                  | Computes π using the SRC-3 (9th-order) compensator for the Leibniz series |
| `Zeta2_SRC7_Validation.py` | Applies SRC-5 compensator to ζ(2), with observed 7th-order convergence |
| `n^3.py`, `n^5.py`         | Residual scaling and symbolic convergence checks for orders n³, n⁵, etc. |
| `README.md`                | This documentation file |

---

## 📈 Example Output

### π via Leibniz + SRC-3:
| n       | δ(n)                      | δ(n) · n⁹         |
|----------|----------------------------|--------------------|
| 10      | 4.97×10⁻⁹               | ≈ 0.0497         |
| 100     | 5.41×10⁻¹⁸             | ≈ 0.00054        |
| 1000    | 5.41×10⁻²⁷             | ≈ 5.41×10⁻⁶      |

### ζ(2) via harmonic sum + SRC-5:
| n       | δ(n)                      | δ(n) · n⁷         |
|----------|----------------------------|--------------------|
| 10      | 2.35×10⁻⁹               | ≈ 0.0235         |
| 100     | 2.38×10⁻¹⁶             | ≈ 0.0238         |
| 1000    | 2.38×10⁻²³             | ≈ 0.0238         |

---

## 📚 Theory

SRC approximates the residual tail \( R_n \) via symbolic compensators:
\[
\rho_k(n) = 4 \sum_{j=0}^{n-1} \frac{(-1)^j}{2j+1} + (-1)^n \varphi_k(n)
\]
where \(\varphi_k(n)\) cancels dominant terms using Euler or Bernoulli expansions. For ζ(2), similar corrections are derived from the Euler–Maclaurin formula.

---

## 🛠 Dependencies

- Python ≥ 3.8
- `mpmath` (`pip install mpmath`)

---

## 🔬 References



Structural Residual Compensation (SRC): A Framework for
High-Order Acceleration of Slowly Converging Series
https://doi.org/10.5281/zenodo.16715318




MIT License

Copyright (c) 2025 Y.Y.N. Li


Structural Residual Cancellation in π Approximation: A Cubic Convergence via Modal Compensation
https://doi.org/10.5281/zenodo.15897936
