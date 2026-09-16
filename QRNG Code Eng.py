from math import *
import numpy as np
import scipy.stats as sc
from numpy.random import chisquare
from scipy.special import exp1
import mpmath

# input data

bits = str( input ("input 'true random num' for bits pls :) "))
ln = len(bits)
rp = ln//100
'''
print("                                           ", rp)
k = int( input("input the number of bits to split (best is ^^^^^) "))
'''
k = rp
# ones and zeros counter

def ones_zeroes_counter(bits):
    ones = 0
    zeroes = 0
    for letter in bits:
        if letter == '1':
            ones += 1
        else:
            zeroes += 1
    return zeroes, ones

# main nist test

def NIST_test(bits):

# frequency bitwise test
    length = len(bits)
    ones , zeros = ones_zeroes_counter(bits)
    pr = ones / length

    #P-value of the 1st test
    p_value_1 = erfc(abs(ones - zeros)/sqrt(length))
    print(" ")
    print(" proportion (ones' part): ", pr)
    print(" test's P_value: ", p_value_1)
    if p_value_1 <= 0.01 and (pr > 0.65 or pr < 0.35):
        return False, p_value_1
# frequency block test

    a = list(bits)
    n = k
    chunks = [a[i:i + n] for i in range(0, len(a), n)]
    chi_sqr = 0
    for i in range(length // k):
        one_one = chunks[i].count('1')
        wwv = one_one / k
        p = (wwv - 0.5) ** 2
        chi_sqr = chi_sqr + p
    chi_sqr = chi_sqr * 4 * k
    p_value = mpmath.gammainc((length / (2*k)), (chi_sqr / 2))
    if p_value <= 0.01:
        return False, p_value
    print(" res of blok test: ", p_value)

# special condition

    condition = 2.0 / sqrt(length)
    print(" condition: ", condition)
    if abs(pr - 0.5) > condition:
        return False, 0.0

# test for identical consecutive bits

    alt_bits = 0.0
    for i in range(length - 1):
        if bits[i] != bits[i + 1]:
            alt_bits += 1.0
    print(" total number of alternating bits: ", alt_bits)

    #P-value of the final test
    p = erfc(abs(alt_bits - (2.0 * length * pr * (1.0 - pr))) / (2.0 * sqrt(2.0 * length) * pr * (1 - pr)))
    success = (p >= 0.01) #True/False
    return success, p

# all stats

print(" result:", *NIST_test(bits))
print(" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")