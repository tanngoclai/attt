"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""

import math

def inverse_number(a,n):
    while a < 0:
        a += n 

    tmp = n
    y = 0
    x = 1
 
    if (n == 1):
        return 0
 
    while (a > 1):
        q = a // n
        t = n
        n = a % n
        a = t
        t = y

        y = x - q * y
        x = t
 
    if (x < 0):
        x = x + tmp
 
    return x

def have_inverse_number(a,n):
    return math.gcd(a,n) == 1


def encode_msg(s):
    s = s.upper()

    length = len(s)
    code = 0

    for i in range(0,length):
        code += (27**(length-i-1))*(ord(s[i])-64) # A->1, B->2, ..., Z->26
    
    print('- Convert message ' + '"' + s + '"' + ' to code: x =', code)

    return code


def decode_msg(s):
    x = s
    length = 0
    while 27**length < s:
        length += 1
    
    res = ''
    for i in range(length-1,-1,-1):
        k = s // 27**i
        s = s % 27**i
        res += chr(k+64)
    
    print('\n- Decode successfully: x =', x)
    print('- Message: "' +  res + '"')
    return res


def cal_power_mod(radix,exp,n):
    tmp = []
    tmp.append(radix % n)

    i = 1
    while 2**i < exp:
        k = tmp[i-1]*tmp[i-1] % n
        tmp.append(k)
        i += 1

    bit = len(tmp)
    sum = 0
    res = 1

    for i in range(bit-1,-1,-1):
        k = sum + 2**i
        if k <= exp:
            sum += 2**i
            res = res*tmp[i] % n
            
    return res


def decimal_to_binary(n):
    if n >= 0:
        return bin(n)[2:]
    else:
        return -1

