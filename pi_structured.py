from mpmath import mp

def leibniz_sum(n):
    """Leibniz π 部分"""
    return mp.fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def phi_tail(n):
    """尾部修正结构项 φ(n)"""
    return mp.mpf(4) * (-1)**n / (2 * n + 1)

def pi_structured(n=1000):
    """结构近似：Leibniz + φ(n)"""
    return leibniz_sum(n) + phi_tail(n)

# 示例测试
mp.dps = 50  # 设置高精度
approx_pi = pi_structured(1000)
print("Structured π ≈", approx_pi)
print("True π       =", mp.pi)
print("Residual     =", abs(approx_pi - mp.pi))

