from mpmath import mp, fsum, quad, mpf, log10
import pandas as pd
import matplotlib.pyplot as plt

# 设置高精度
mp.dps = 50

# 正确的 φ₇(n)，基于渐近展开
def phi_approx_7(n):
    terms = [
        mpf(1) / n,
        -mpf(1) / (4 * n**3),
        mpf(5) / (16 * n**5),
        -mpf(61) / (64 * n**7)
    ]
    return fsum(terms)

# 更精确地计算 Rₙ（尾项）
def Rn_integral(n):
    return 4 * quad(lambda t: t**(2 * n) / (1 + t**2), [0, 1])

# 测试点
n_vals = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]

rows = []
for n in n_vals:
    rn = Rn_integral(n)
    phi = phi_approx_7(n)
    delta = abs(rn - phi)
    delta_scaled = delta * n**7
    rows.append({
        "n": n,
        "δ(n)": delta,
        "δ(n)·n⁷": delta_scaled,
        "log₁₀(n)": log10(n),
        "-log₁₀(δ(n))": -log10(delta)
    })

# 创建 DataFrame
df = pd.DataFrame(rows)
display(df)

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(df["log₁₀(n)"], df["-log₁₀(δ(n))"], marker='o', label='Log-Log Plot')
plt.title("Log-Log Plot of $-\\log_{10}(\\delta(n))$ vs $\\log_{10}(n)$ (Corrected SRC-7)")
plt.xlabel("$\\log_{10}(n)$")
plt.ylabel("$-\\log_{10}(\\delta(n))$")
plt.grid(True, which='both', ls='--')
plt.legend()
plt.tight_layout()
plt.show()