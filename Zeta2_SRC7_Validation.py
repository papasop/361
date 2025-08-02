from mpmath import mp, zeta, fsum, mpf, log10
import pandas as pd
import matplotlib.pyplot as plt

# 设置高精度
mp.dps = 50

# 构造 ζ(2) 的部分和
def zeta_partial_sum(s, n):
    return fsum([1 / mpf(k)**s for k in range(1, n + 1)])

# 修正的 SRC-5 补偿器（基于Euler-Maclaurin公式，up to n^{-5}项）
def src5_zeta2(n):
    return mpf(1)/n - mpf(1)/(2*n**2) + mpf(1)/(6*n**3) - mpf(1)/(30*n**5)

# 真正值 ζ(2)
zeta2 = zeta(2)

# 测试点（扩展以观察渐进行为）
n_vals = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]

rows = []
for n in n_vals:
    approx = zeta_partial_sum(2, n) + src5_zeta2(n)
    delta = abs(zeta2 - approx)
    delta_scaled5 = delta * n**5
    delta_scaled6 = delta * n**6
    rows.append({
        "n": n,
        "δ(n)": delta,
        "δ(n)·n⁵": delta_scaled5,
        "δ(n)·n⁶": delta_scaled6,
        "log₁₀(n)": log10(n),
        "-log₁₀(δ(n))": -log10(delta)
    })

df = pd.DataFrame(rows)
print(df)  # 输出表格到控制台（实际运行时可见）

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(df["log₁₀(n)"], df["-log₁₀(δ(n))"], marker='o', label='Log-Log Plot')
plt.title("Log-Log Plot of $-\\log_{10}(\\delta(n))$ vs $\\log_{10}(n)$ (ζ(2) SRC-5)")
plt.xlabel("$\\log_{10}(n)$")
plt.ylabel("$-\\log_{10}(\\delta(n))$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()