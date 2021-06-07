"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


import core
from random import randint
import math


p = 63658079635199111956084400808111488530041639455424124782351522677612092790273
alpha = 5
a = 1 #default private key
beta = core.cal_power_mod(alpha,a,p)


def encode_elgamal():
    msg = input('- Enter message: ')
    x = core.encode_msg(msg)

    k = randint(0, p-1)
    print('- Created key, use random number k =', k)

    y1 = core.cal_power_mod(alpha,k,p)
    y2 = x*core.cal_power_mod(beta,k,p) % p

    print('\n- Encode successfully, encode: ' + '\n(y1,y2) = (' + str(y1) + ', ' + str(y2) + ')')


def decode_elgamal():
    try:
        y1 = int(input('- Enter code y1 = '))
        y2 = int(input('- Enter code y2 = '))
        
        pow_y_a = core.cal_power_mod(y1,a,p)
        inverse_y_a = core.inverse_number(pow_y_a,p)

        x = y2*inverse_y_a % p

        core.decode_msg(x)

    except:
        print('- Invalid code') 


def sig_elgamal(a):
    msg = input('- Enter your signature: ')
    x = core.encode_msg(msg)

    
    k = randint(0, p-1)

    while not core.have_inverse_number(k,p-1):
        k = randint(0, p-1)
    
    print('- Created key, use random number k =', k)

    gamma_elgamal = core.cal_power_mod(alpha,k,p)
    sigma_elgamal = (x-a*gamma_elgamal)*core.inverse_number(k,p-1) % (p-1)

    print('\n- Sign successfully, sig(x,k) =: ' + '\n(gamma,sigma) = (' + str(gamma_elgamal) + ', ' + str(sigma_elgamal) + ')')


def ver_elgamal(msg,gamma_elgamal,sigma_elgamal):
    x = core.encode_msg(msg)
    res = core.cal_power_mod(beta,gamma_elgamal,p)*core.cal_power_mod(gamma_elgamal,sigma_elgamal,p) - core.cal_power_mod(alpha,x,p)

    if res % p == 0:
        core.decode_msg(x)
        print('Verify successfully.')
    else:
        print('Verify fail.')


def print_public_key():
    print('\n- Using public key: ' + \
            '\np = ' + str(p) + \
            '\nalpha = ' + str(alpha) + \
            '\nbeta = ' + str(beta) + '\n')


if __name__ == '__main__':
    action = input('Encode/Decode (1) or Sign/Verify (2): 1 or 2: ')

    if action == '1':
        req = input('- Encode Elgamal (1) or Decode Elgamal (2) or Create new public key (3) - 1 or 2 or 3: ')
    
        try:
            if req == '1':
                beta = int(input('- Enter beta = '))
                print_public_key()
                encode_elgamal()       

            elif req == '2':
                a = int(input('- Enter private key a = '))
                beta = core.cal_power_mod(alpha,a,p)
                print_public_key()
                decode_elgamal()
    
            elif req == '3':
                a = int(input('- Enter private key a = '))
                beta = core.cal_power_mod(alpha,a,p)
                print_public_key()  

        except:
            print('- Invalid key') 

    elif action == '2':
        req = input('- Sign Elgamal (1) or Verify signature Elgamal (2) or Create new public key (3) - 1 or 2 or 3: ')
    
        try:
            if req == '1':
                a = int(input('- Enter private key a = '))
                beta = core.cal_power_mod(alpha,a,p)
                print_public_key()
                sig_elgamal(a)

            elif req == '2':
                x = input('- Enter signature text x = ')
                beta = int(input('- Enter beta in puclic key: beta = '))
                gamma_sign = int(input('- Enter signature gamma = '))
                sigma_sign = int(input('- Enter signature sigma = '))
                print_public_key()
                ver_elgamal(x,gamma_sign,sigma_sign)
               
            elif req == '3':
                a = int(input('- Enter private key a = '))
                beta = core.cal_power_mod(alpha,a,p)
                print_public_key() 

               
        except:
            print('- Invalid key') 

    else:
        print('- Please enter "1" or "2"')

    






