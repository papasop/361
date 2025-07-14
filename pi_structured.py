# Structured Pi Approximation Module
# Copyright (c) 2025 Y.Y.N. Li. MIT License.

from mpmath import mp

def leibniz_sum(n):
    """Leibniz π approximation part"""
    return mp.fsum([mp.mpf(4) * (-1)**k / (2 * k + 1) for k in range(n)])

def phi_tail(n):
    """Structured correction φ(n) for tail"""
    return mp.mpf(4) * (-1)**n / (2 * n + 1)

def pi_structured(n=1000):
    """
    Structured approximation to π:
        ρ(n) = Leibniz_sum(n) + φ(n)
    """
    return leibniz_sum(n) + phi_tail(n)
