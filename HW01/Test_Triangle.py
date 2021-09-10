import math
import random
import unittest
import TriangleClass


class TestTriangle(unittest.TestCase):

    def test_TriangleClass0(self):
        self.assertEqual(TriangleClass.classify_triangle(9, 9, 9), "equilateral")

    def test_TriangleClass1(self):
        self.assertEqual(TriangleClass.classify_triangle(9, 8, 9), "isosceles")

    def test_TriangleClass2(self):
        self.assertEqual(TriangleClass.classify_triangle(7, 8, 7), "isosceles")

    def test_TriangleClass3(self):
        self.assertEqual(TriangleClass.classify_triangle(6, 8, 6), "isosceles")

    def test_TriangleClass4(self):
        self.assertEqual(TriangleClass.classify_triangle(7, 7, 8), "isosceles")

    def test_TriangleClass5(self):
        self.assertEqual(TriangleClass.classify_triangle(8, 8, 4), "isosceles")

    def test_TriangleClass6(self):
        self.assertEqual(TriangleClass.classify_triangle(2, 3, 3), "isosceles")

    def test_TriangleClass7(self):
        self.assertEqual(TriangleClass.classify_triangle(4, 5, 5), "isosceles")

    def test_TriangleClass8(self):
        self.assertEqual(TriangleClass.classify_triangle(6, 2, 2), "isosceles")

    def test_TriangleClass9(self):
        self.assertEqual(TriangleClass.classify_triangle(9, 1, 9), "isosceles")

    def test_TriangleClass10(self):
        self.assertEqual(TriangleClass.classify_triangle(6, 6, 2), "isosceles")

    def test_TriangleClass11(self):
        self.assertEqual(TriangleClass.classify_triangle(3, 4, 5), "right")

    def test_TriangleClass12(self):
        self.assertEqual(TriangleClass.classify_triangle(5, 12, 13), "right")

    def test_TriangleClass13(self):
        self.assertEqual(TriangleClass.classify_triangle(8, 15, 17), "right")

    def test_TriangleClass14(self):
        self.assertEqual(TriangleClass.classify_triangle(7, 24, 25), "right")

    def test_TriangleClass15(self):
        self.assertEqual(TriangleClass.classify_triangle(9, 40, 41), "right")

    def test_TriangleClass16(self):
        self.assertEqual(TriangleClass.classify_triangle(1,1,1), "equilateral")

    def test_TriangleClass17(self):
        self.assertEqual(TriangleClass.classify_triangle(5,5,5), "equilateral")

    def test_TriangleClass18(self):
        self.assertEqual(TriangleClass.classify_triangle(18,18,18), "equilateral")

    def test_TriangleClass19(self):
        self.assertEqual(TriangleClass.classify_triangle(234,234,234), "equilateral")

    def test_TriangleClass20(self):
        self.assertEqual(TriangleClass.classify_triangle(293,293,293), "equilateral")

    def test_TriangleClass21(self):
        self.assertEqual(TriangleClass.classify_triangle(8,8,8), "equilateral")

    def test_TriangleClass22(self):
        self.assertEqual(TriangleClass.classify_triangle(6,3,8), "scalene")

    def test_TriangleClass23(self):
        self.assertEqual(TriangleClass.classify_triangle(9,1,4), "scalene")

    def test_TriangleClass24(self):
        self.assertEqual(TriangleClass.classify_triangle(8,7,2), "scalene")

    def test_TriangleClass25(self):
        self.assertEqual(TriangleClass.classify_triangle(7,5,9), "scalene")

    def test_TriangleClass26(self):
        self.assertEqual(TriangleClass.classify_triangle(3,8,7), "scalene")

    def test_TriangleClass27(self):
        self.assertEqual(TriangleClass.classify_triangle(0,0,0), "none")

    def test_TriangleClass28(self):
        a = random.randrange(100)
        b = random.randrange(100)
        c = math.sqrt(a*a+b*b)
        self.assertEqual(TriangleClass.classify_triangle_withError(a,b,c,0.001), "right")

    def test_TriangleClass29(self):
        a = random.randrange(100)
        b = random.randrange(100)
        c = math.sqrt(a*a+b*b)
        self.assertEqual(TriangleClass.classify_triangle_withError(a,b,c,0.001), "right")

    def test_TriangleClass30(self):
        a = random.randrange(100)
        b = random.randrange(100)
        c = math.sqrt(a*a+b*b)
        self.assertEqual(TriangleClass.classify_triangle_withError(a,b,c,0.001), "right")

    def test_TriangleClass31(self):
        a = random.randrange(100)
        b = random.randrange(100)
        c = math.sqrt(a*a+b*b)
        self.assertEqual(TriangleClass.classify_triangle_withError(a,b,c,0.001), "right")

    def test_TriangleClass32(self):
        a = random.randrange(100)
        b = random.randrange(100)
        c = math.sqrt(a*a+b*b)
        self.assertEqual(TriangleClass.classify_triangle_withError(a,b,c,0.001), "right")








if __name__ == '__main__':
    unittest.main()
