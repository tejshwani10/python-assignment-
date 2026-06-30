import math

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        d = no.real**2 + no.imaginary**2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / d
        imag_part = (self.imaginary * no.real - self.real * no.imaginary) / d
        return Complex(real_part, imag_part)

    def mod(self):
        mod_val = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(mod_val, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            result = "0.00%+.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x.mod())
    print(y.mod())