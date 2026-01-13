import math

def normal_square(w,h):
    return w * h - (w + h - math.gcd(w, h))




print(normal_square(8, 12)) # result = 80