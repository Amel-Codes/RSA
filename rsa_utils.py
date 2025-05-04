import random
import sympy
import math

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generer_premier(nb_bits):
    min_val = 2
    max_val = 2**nb_bits - 1
    while True:
        num = random.randint(min_val, max_val)
        if sympy.isprime(num):
            return num

def inverse_modulaire(a, b):
    r, rr = a, b
    u, uu = 1, 0
    v, vv = 0, 1
    while rr:
        q = r // rr
        r, rr = rr, r - q * rr
        u, uu = uu, u - q * uu
        v, vv = vv, v - q * vv
    return v + a if v < 0 else v

def montgomery_multiplication(a, b, n):
    result = 0
    a %= n
    while b > 0:
        if b % 2 == 1:
            result = (result + a) % n
        a = (a * 2) % n
        b //= 2
    return result

def montgomery_exponentiation(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = montgomery_multiplication(result, base, mod)
        base = montgomery_multiplication(base, base, mod)
        exp //= 2
    return result

def factoriser(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def generer_cles_rsa(nb_bits):
    p = generer_premier(nb_bits // 2)
    q = generer_premier(nb_bits // 2)
    while p == q:
        q = generer_premier(nb_bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generer_premier(nb_bits)
    while pgcd(e, phi) != 1:
        e = generer_premier(nb_bits)
    d = inverse_modulaire(phi, e)
    return (e, n), (d, n)
