import math
class Complex:
    def __init__(self, a, b):
        self.real = round(a, 2)
        self.imaginary = round(b,2)
    def __str__(self):
        if self.real != 0:
            str = '%0.2f' % self.real
        elif self.imaginary != 0:
            str = '0.00'
        else :
            str = '0.00+0.00i'
        if self.imaginary > 0 :
            str += '+%0.2fi' % self.imaginary
        elif self.imaginary < 0:
            str += '-%0.2fi' % abs(self.imaginary)
        else :
            str += '+0.00i'
        return str
    def __add__(self, Number):
        real = self.real + Number.real
        imaginary = self.imaginary + Number.imaginary
        return Complex(real, imaginary)
    def __sub__(self, Number):
        real = self.real - Number.real
        imaginary = self.imaginary - Number.imaginary
        return Complex(real, imaginary)
    def __mul__(self, Number):
        real = self.real * Number.real - self.imaginary * Number.imaginary
        imaginary = self.real * Number.imaginary + self.imaginary * Number.real
        return Complex(real, imaginary)
    def __truediv__(self, Number):
        x = float(Number.real ** 2 + Number.imaginary ** 2)
        y = self * Complex(Number.real, - Number.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)
    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

if __name__ == '__main__':
    print('Enter the real & imaginary value of first complex number')
    c = map(float, input().split())
    print('Enter the real & imaginary value of first complex number')
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
