from ecc.galois_field.generic import is_prime

class GaloisField(object):
    
    """
    Galois Field object

    Contains modules for addition, multiplication, inverse, subtraction over Galois Field

    """

    def __init__(self, p):
        assert is_prime(p), "\nPassed value should be a prime !!\n"
        self.p = p
        self.elements = list(range(0, p))

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __repr__(self):
        return "Galois Field, p = {}, Start element = {}, End element = {}".format(self.p, self.elements[0], self.elements[self.p -1])

    # Operations
    
    # Addition
    def add(self, element_1, element_2):
        return (element_1 + element_2) % self.p

    # Subtraction
    def subtract(self, element_1, element_2):
        return (element_1 - element_2)%self.p

    # Multiplication
    def multiply(self, element_1, element_2):
        return (element_1 * element_2)%self.p

    # Division
    def division(self, element_1, element_2):
        return (element_1 * self.inverse(element_2))%self.p

    # Inverse ( b = a-1(mod p); b is the inverse of a, a-1 = b)
    # By Fermat's Theorem
    def inverse(self, a):
        return a**(self.p - 2)%self.p

    # x^3
    def x_cubed(self, x):
        return self.multiply(self.multiply(x, x), x)
