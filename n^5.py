# 安装依赖（如尚未安装）
!pip install mpmath tabulate matplotlib pandas

# 导入库
from mpmath import mp, mpf, fsum, log
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import math
from IPython.display import display

# 设置精度
mp.dps = 50

# 定义函数
def alpha_fifth_order(n):
    return mpf(n) / (4 * n**2 + 1)

def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

def rho(n):
    return leibniz_sum(n) + 4 * (-1)**n * alpha_fifth_order(n)

def count_matching_digits(approx, true_pi):
    approx_str = mp.nstr(approx, mp.dps)[2:]  # 小数部分
    pi_str = mp.nstr(true_pi, mp.dps)[2:]
    matching = 0
    for a, p in zip(approx_str, pi_str):
        if a != p:
            break
        matching += 1
    return matching

def structure_density(n):
    α = alpha_fifth_order(n)
    return α**2

def entropy_density(n):
    α = alpha_fifth_order(n)
    return log(1 + α)

def K_ratio(n):
    Φ = structure_density(n)
    H = entropy_density(n)
    return Φ / H

def K_over_alpha(n):
    α = alpha_fifth_order(n)
    return K_ratio(n) / α

# 主运行逻辑
ns = [10, 50, 100, 300, 1000, 3000, 10000]
true_pi = mp.pi
rows = []
log_data = []

for n in ns:
    approx = rho(n)
    δ = abs(true_pi - approx)
    α = alpha_fifth_order(n)
    K = K_ratio(n)
    kn_over_an = K / α
    matching = count_matching_digits(approx, true_pi)
    delta_n5 = δ * n**5
    rows.append([
        n,
        mp.nstr(approx, 20),  # 20 位
        mp.nstr(δ, 5, strip_zeros=False),
        matching,
        mp.nstr(kn_over_an, 8),
        mp.nstr(delta_n5, 5)
    ])
    log_data.append({
        'x': math.log10(n),
        'y': -math.log10(float(δ))
    })

# 输出为 DataFrame
df = pd.DataFrame(rows, columns=["n", "ρ(n)", "δ(n)", "匹配位数", "K/α(n)", "δ(n)·n⁵"])
display(df)

# 保存为 CSV（可选）
df.to_csv("pi_structure_table.csv", index=False)

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter([d['x'] for d in log_data], [d['y'] for d in log_data],
            color='#1f77b4', label='log(δ(n)) vs log(n)', s=60)
plt.plot([1, 4], [5, -10], color='#ff7f0e', linestyle='--', label='Slope -5')
plt.xlabel('log(n)')
plt.ylabel('-log(δ(n))')
plt.title('Log-Log Plot for Fifth-Order Convergence')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('loglog_plot.png', dpi=300, bbox_inches='tight')
plt.show()

