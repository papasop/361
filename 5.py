from mpmath import mp, mpf, fsum, pi

mp.dps = 50

def leibniz_sum(n):
    return fsum([mpf(4) * (-1)**k / (2*k + 1) for k in range(n)])

def madhava_f2(n):
    return mpf(n) / (4 * n**2 + 1)

def rho(n):
    return leibniz_sum(n) + 4 * (-1)**n * madhava_f2(n)

def count_matching_digits(approx, true_pi):
    approx_str = mp.nstr(approx, mp.dps)[2:]  # 小数部分
    pi_str = mp.nstr(true_pi, mp.dps)[2:]     # π 小数部分
    matching = 0
    for a, p in zip(approx_str, pi_str):
        if a != p:
            break
        matching += 1
    return matching

ns = [100, 1000, 10000]
true_pi = mp.pi

for n in ns:
    approx = rho(n)
    δ = abs(true_pi - approx)
    matching = count_matching_digits(approx, true_pi)
    print(f"n = {n:<6} | ρ(n) ≈ {mp.nstr(approx, 30)}")
    print(f"         | δ(n)  = {mp.nstr(δ, 5)}")
    print(f"         | δ(n)·n^3 = {mp.nstr(δ * n**3, 5)}")
    print(f"         | δ(n)·n^4 = {mp.nstr(δ * n**4, 5)}")
    print(f"         | δ(n)·n^5 = {mp.nstr(δ * n**5, 5)}")
    print(f"         | 匹配位数 = {matching}")
    print("-" * 90)