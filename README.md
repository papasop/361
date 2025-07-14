# Structured Pi Approximation (ρ(n))

This project proposes a new approximation to π using a hybrid structure:
- A finite Leibniz series: \( L_n = 4 \sum_{k=0}^{n-1} \frac{(-1)^k}{2k+1} \)
- A fixed arctangent correction term \( \phi \)

Together, this gives a structured approximation:
\[
ρ(n) = L_n + \phi
\]

### Files
- `pi_structured.py` — defines the function `pi_structured()`
- `test_pi_structured.py` — tests precision with `mpmath`

### Run the test
```python
# test_pi_structured.py
from pi_structured import pi_structured
from mpmath import mp

mp.dps = 50
print("Structured π:", pi_structured())
print("True π:", mp.pi)
print("Residual:", abs(mp.pi - pi_structured()))





!git clone https://github.com/papasop/361.git
%cd 361
!python3 test_pi_structured.py






MIT License

Copyright (c) 2025 Y.Y.N. Li

Permission is hereby granted, free of charge, to any person obtaining a copy
...
