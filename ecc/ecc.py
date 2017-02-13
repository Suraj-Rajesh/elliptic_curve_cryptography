from ecc.galois_field.galois_field import GaloisField
from ecc.galois_field.generic import legendre_symbol

class EllipticCurve(object):

    """
        Elliptic curve object, y^2 = x^3 + Ax + B
    """

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.gf = GaloisField(p)

    def order_of_curve(self):
        order = 0

        for x in self.gf.elements:
            order = order + legendre_symbol(self.gf.add(self.gf.add((self.gf.x_cubed(x)), self.gf.multiply(self.a, x)), self.b), self.gf.p)
        return (order + self.gf.p + 1)
