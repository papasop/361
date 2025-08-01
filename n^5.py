# 安装依赖（Colab 可能已预装 mpmath，但确保 tabulate 可用）
!pip install mpmath tabulate

# 导入库
from mpmath import mp, mpf, fsum, log, atan
import pandas as pd
from tabulate import tabulate

# 设置高精度
mp.dps = 50

# 五阶结构项 α(n) = n / (4n² + 1)
def alpha_fifth_order(n):
    return mpf(n) / (4 * n**2 + 1)

# Leibniz 主和项
def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

# 完整 π 近似式
def rho(n):
    return leibniz_sum(n) + 4 * (-1)**n * alpha_fifth_order(n)

# 匹配位数计算（修正为连续匹配位数，从小数点后开始逐位比较直到第一个不匹配）
def count_matching_digits(approx, true_pi):
    approx_str = mp.nstr(approx, mp.dps)[2:]  # 小数部分
    pi_str = mp.nstr(true_pi, mp.dps)[2:]     # π 小数部分
    matching = 0
    for a, p in zip(approx_str, pi_str):
        if a != p:
            break
        matching += 1
    return matching

# 结构密度 Φ(n) = α²(n)
def structure_density(n):
    α = alpha_fifth_order(n)
    return α**2

# 熵密度 H(n) = log(1 + α(n))
def entropy_density(n):
    α = alpha_fifth_order(n)
    return log(1 + α)

# 比值 K = Φ / H
def K_ratio(n):
    Φ = structure_density(n)
    H = entropy_density(n)
    return Φ / H

# K(n)/α(n)
def K_over_alpha(n):
    α = alpha_fifth_order(n)
    return K_ratio(n) / α

# 主运行逻辑
ns = [100, 300, 1000, 3000, 10000]
true_pi = mp.pi
rows = []

for n in ns:
    approx = rho(n)
    δ = abs(true_pi - approx)
    α = alpha_fifth_order(n)
    K = K_ratio(n)
    kn_over_an = K / α
    matching = count_matching_digits(approx, true_pi)
    delta_n5 = δ * n**5  # 添加 δ(n) · n^5 以验证五阶收敛
    rows.append([
        n,
        mp.nstr(approx, 20),  # 显示更多位数（20 位）
        mp.nstr(δ, 5, strip_zeros=False),
        matching,
        mp.nstr(kn_over_an, 25),
        mp.nstr(delta_n5, 5)  # δ(n) · n^5
    ])

# 表头与美感输出
headers = ["n", "ρ(n)", "δ(n)", "匹配位数", "K/α(n)", "δ(n)·n^5"]
print(tabulate(rows, headers=headers, tablefmt="grid", colalign=("right",)))
