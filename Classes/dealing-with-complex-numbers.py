# Classes: Dealing with Complex Numbers

class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self+0)
