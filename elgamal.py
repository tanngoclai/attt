"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


import core
from random import randint


p = 63658079635199111956084400808111488530041639455424124782351522677612092790273
alpha = 5


def encode_elgamal():
    msg = input('- Enter message: ')
    x = core.encode_msg(msg)

    k = randint(0, p-1)
    print('- To create key, use random number k =', k)

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


def print_public_key():
    print('\n- Using public key: ' + \
            '\np = ' + str(p) + \
            '\nalpha = ' + str(alpha) + \
            '\nbeta = ' + str(beta) + '\n')


if __name__ == '__main__':

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






