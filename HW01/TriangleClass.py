import math


def classify_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "none"
    if a == b and b == c and c == a:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2) or math.pow(b, 2) + math.pow(c, 2) == math.pow(a,2) \
            or math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2):
        return "right"
    else:
        return "scalene"


def classify_triangle_withError(a, b, c, e):
    if a == 0 or b == 0 or c == 0:
        return "none"
    if a == b and b == c and c == a:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    if c > 0 and abs(1 - (a * a + b * b) / (c * c)) < e or a > 0 and abs(1 - (b * b + c * c) / (a * a)) < e or b > 0 and abs(1 - (c * c + a * a) / (b * b)) < e:
        return "right"
    else:
        return "scalene"

