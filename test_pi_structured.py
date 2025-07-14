from mpmath import mp
from pi_structured import pi_structured

mp.dps = 50  # 精度设置

approx_pi = pi_structured(n=1000)
true_pi = mp.pi
residual = abs(true_pi - approx_pi)

print("Structured π:", approx_pi)
print("True π:", true_pi)
print("Residual:", residual)
