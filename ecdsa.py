"""
Full name: Lai Ngoc Tan
MSSV: 18020049
"""


import core 
import elliptic
from random import randint
import hashlib


g = elliptic.P
n = elliptic.order

d = 1
Q = elliptic.multi(g,d)


def create_key():
    try:
        d = int(input('Enter private key in [1,' + str(n-1) +']: '))
        Q = elliptic.multi(g,d)
        print_public_key_sign(Q)
    except:
        print('Invalid number')


def sign_ecdsa(d):
    msg = input('- Enter your signature: ')
    x = str.encode(msg)

    k = randint(1, n-1)
    r = 0
    s = 0
    while s == 0:
        k = randint(1, n-1)

        tmp = elliptic.multi(g,k)
        r = tmp[0] % n
        if r == 0:
            continue
        h = int(hashlib.sha512(x).hexdigest(),16)

        if core.have_inverse_number(k,n):
            s = (h + d*r)*core.inverse_number(k,n) % n

    if r != 0 and s != 0:
        print('\n- Sign successfully: (r,s) = (' + str(r) + ',' + str(s) +')')


def ver_ecdsa(g,Q):
    try:
        r = int(input('- Enter code r = '))
        s = int(input('- Enter code s = '))

        msg = input('- Enter signature need to verify: ')
        x = str.encode(msg)
        h = int(hashlib.sha512(x).hexdigest(),16)
        
        if 1 <= r <= n-1 and 1 <= s <= n-1:
            if core.have_inverse_number(s,n):
                w = core.inverse_number(s,n)
                u1 = h*w % n
                u2 = r*w % n

                u1g = elliptic.multi(g,u1)
                u2Q = elliptic.multi(Q,u2)
                tmp = elliptic.add(u1g,u2Q)
                v = tmp[0] % n
                
                if v == r:
                    print('- Verify successfully.')
                else:
                    print('- Verify fail.')

            else:
                print('gcd(s,n) is not 1')
        else:
            print('- Invalid code')
        
    except:
        print('- Invalid code') 


def print_public_key_sign(Q):
    print('- Using public key: \n' + \
            '(E): y^2 = x^3 + ' + str(elliptic.a) + 'x + ' + str(elliptic.b) + '\n' + \
            'Generator point g = ' + str(g) + '\n' + \
            'Order of g: n = ' + str(n) + '\n' + \
            'Q = ' + str(Q))


if __name__ == '__main__':
    req = input('Sign EC Elgamal (1) or Verify signature EC Elgamal (2) or Create signature public key (3) - 1 or 2 or 3: ')
    
    try:
        if req == '1':
            d = int(input('- Enter private key: d = '))
            sign_ecdsa(d)

        elif req == '2':
            g_x = int(input('- Enter g.x = '))
            g_y = int(input('- Enter g.y = '))
            Q_x = int(input('- Enter Q.x = '))
            Q_y = int(input('- Enter Q.y = '))

            ver_ecdsa([g_x,g_y],[Q_x,Q_y])

        elif req == '3':
            create_key()

        else:
            print('- Please enter "1" or "2" or "3"')

    except:
        print('- Invalid number')