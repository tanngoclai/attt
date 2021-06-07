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
d = core.inverse_number(e,phi_n)


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
    

def sig_rsa(a):
    msg = input('- Enter your signature: ')
    x = core.encode_msg(msg)

    print('- Sign successfully: sig(x) =', core.cal_power_mod(x,a,n))


def ver_rsa(y,b):
    try:
        x = core.cal_power_mod(y,b,n) % n

        core.decode_msg(x)

    except:
        print('- Invalid code') 


def has_inverse_number(e):
    return math.gcd(e,phi_n) == 1


if __name__ == '__main__':
    action = input('Encode/Decode (1) or Sign/Verify (2): 1 or 2: ')

    if action == '1':
        try:
            e = int(input('- Enter e = '))

            if has_inverse_number(e):
                print('\n- Using public key is: (n,e) = ' + str(n) + ',' + str(e) + ')\n')
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
    
    elif action == '2':
        try:
            req = input('- Sign RSA (1) or Verify signature RSA (2) - 1 or 2: ')

            if req == '1':
                a = int(input('- Enter private key a = '))

                if has_inverse_number(a):
                    b = core.inverse_number(a,phi_n)
                    print('\n- Using public key is: (n,b) = ' + str(n) + ',' + str(b) + ')\n')
                    sig_rsa(a)

                else:
                    print('- Invalid: gcd(a,phi_n) is not 1, try again.')

            elif req == '2':
                b = int(input('- Enter b in public key b = '))
                y = int(input('- Enter signature y = '))

                ver_rsa(y, b)
            else:
                print('- Please enter "1" or "2"')

        except:
            print('- Invalid number') 

    else:
        print('- Please enter "1" or "2"')