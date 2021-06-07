"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


import core


p = 1461501637330902918203684832716283019651637554291
a = 1461501637330902918203684832716283019651637554288
b = 1032640608390511495214075079957864673410201913530

#root point
P = [473058756663038503608844550604547710019657059949, 1454008495369951658060798698479395908327453245230]
order = 1461501637330902918203685083571792140653176136043

def ecc_lambda(p1,p2):
    if (p1[0] == p2[0] and p1[1] == p2[1]):
        tmp = core.inverse_number(2*p1[1],p)
        return (3*(p1[0]**2)+a)*tmp % p

    elif (p1[0] != p2[0]):
        tmp = core.inverse_number(p2[0]-p1[0],p)
        return (p2[1]-p1[1])*tmp % p


def add(p1,p2):
    try:
        l = ecc_lambda(p1,p2)

        x = (l**2 - p1[0] - p2[0]) % p
        y = (l*(p1[0] - x) - p1[1]) % p

        p3 = [x,y]
        return p3

    except:
        return [0,0]


def multi(a,times):
    if (times >= 0):
        bit = core.decimal_to_binary(times)

        number_bit = len(bit)
        tmp = []
        tmp.append(a)
        
        for i in range(1,number_bit):
            r = add(tmp[i-1],tmp[i-1])
            tmp.append(r)
        tmp = tmp[::-1]

        res = a
        first_bit_1 = True
        for i in range(0,number_bit):
            if bit[i] == '1':
                if first_bit_1:
                    res = tmp[i]
                    first_bit_1 = False
                else:
                    res = add(res,tmp[i])
        return res
    else:
        return -1


