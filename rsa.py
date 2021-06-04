"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


import core 
import math


p = 78669127458061087247706989358483239190815578755986744778269251075444973560609
q = 81334505444646769807876363896883649712728812830289282580438377725505501967723

n = p*q
phi_n = (p-1)*(q-1)

e = 1051 #default e


def encode_rsa():
    msg = input('- Enter message: ')
    x = core.encode_msg(msg)

    print('- Encode successfully: y =', core.cal_power_mod(x,e,n))


def decode_rsa():
    try:
        y = int(input('- Enter code y = '))
        x = core.cal_power_mod(y,d,n)

        core.decode_msg(x)

    except:
        print('- Invalid code') 
    

def is_valid_e(e):
    return math.gcd(e,phi_n) == 1
    

if __name__ == '__main__':
    try:
        e = int(input('- Enter e = '))

        if is_valid_e(e):
            print('\n- Using public key is: \nn = ' + str(n) + '\ne = ' + str(e) + '\n')
            d = core.inverse_number(e,phi_n)

            req = input('- Encode RSA (1) or decode RSA (2) - 1 or 2: ')
            if req == '1':
                encode_rsa()
            elif req == '2':
                decode_rsa()
            else:
                print('- Please enter "1" or "2"')
        else:
            print('- Invalid: gcd(e,phi_n) is not 1, try again.')

    except:
        print('- Invalid number')  