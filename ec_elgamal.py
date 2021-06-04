"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


from elgamal import decode_elgamal, encode_elgamal
import core 
import elliptic
from random import randint


P = elliptic.P
prime_number = elliptic.p 
s = 1
B = elliptic.multi(P,s)


def encode_ecc():
    msg = input('- Enter message: ')
    x = core.encode_msg(msg)

    M = elliptic.multi(P,x)
    print('M =', M)

    k = randint(0, prime_number-1)

    print('- To create key, use random number k =', k)

    M1 = elliptic.multi(P,k)
    M2 = elliptic.add(M,elliptic.multi(B,k))

    print('\n- Encode successfully, encode: ' + '\nM1 = ' + str(M1) + '\nM2 = ' + str(M2))


def decode_ecc():
    try:
        M1_x = int(input('- Enter code M1.x = '))
        M1_y = int(input('- Enter code M1.y = '))
        M2_x = int(input('- Enter code M2.x = '))
        M2_y = int(input('- Enter code M2.y = '))
        
        M1 = [M1_x,M1_y]
        M2 = [M2_x,M2_y]

        tmp = elliptic.multi(M1,s)

        M = elliptic.add(M2,[tmp[0],prime_number-tmp[1]])

        print('\n- Decode successfully: ' + '\nM = ' + str(M))

    except:
        print('- Invalid code') 


def print_public_key():
    print('- Using public key: \n' + \
            '(E): y^2 = x^3' + str(elliptic.a) + 'x + ' + str(elliptic.b) + '\n' + \
            'p = ' + str(prime_number) + '\n' + \
            'Generator point P = ' + str(P) + '\n' + \
            'B = ' + str(B))


if __name__ == '__main__':
    req = input('- Encode EC Elgamal (1) or Decode EC Elgamal (2) or Create new public key (3) - 1 or 2 or 3: ')
    
    try:
        if req == '1':
            x = int(input('- Enter B.x = '))
            y = int(input('- Enter B.y = '))
            B = [x,y]
            print_public_key()
            encode_ecc()

        elif req == '2':
            s = int(input('- Enter private key s = '))
            print_public_key()
            decode_ecc()

        elif req == '3':
            s = int(input('- Enter private key s = '))
            B = elliptic.multi(P,s)
            print_public_key()

        else:
            print('- Please enter "1" or "2" or "3"')

    except:
        print('- Invalid number')