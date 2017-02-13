def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False

    r = int(n**0.5)
    f = 5

    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6

    return True 


def legendre_symbol(a, p):
    """
    RETURNS: 

    1  : a is a QR(mod p)
    -1 : a is a QNR(mod p)
    0  : a = 0(mod p)
    """
    legendre_symbol = pow(a, int((p - 1)/2), p)
    return -1 if legendre_symbol == p - 1 else legendre_symbol
