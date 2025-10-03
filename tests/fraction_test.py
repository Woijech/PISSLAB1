from src.fraction_class import Fraction
import unittest

class TestFraction(unittest.TestCase):
    def test_1(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6))

    def test_2(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 - f2, Fraction(1, 6))

    def test_3(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2))

    def test_4(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 / f2, Fraction(3, 2))

    def test_5(self):
        f1 = Fraction(2, 4)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 == f2)

    def test_6(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1 != f2)

    def test_7(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)
        self.assertTrue(f1 > f2)

    def test_8(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertTrue(f1 < f2)

    def test_9(self):
        f1 = Fraction(5, 3)
        f2 = Fraction(5, 3)
        self.assertTrue(f1 >= f2)

    def test_10(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertTrue(f1 <= f2)

    def test_11(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_12(self):
        f = Fraction(-1, 2)
        self.assertEqual(f.num, -1)

    def test_13(self):
        f = Fraction(1, -2)
        self.assertEqual(f.den, -2)
        self.assertEqual(f.num, 1)

    def test_14(self):
        f = Fraction(7, 3)
        self.assertEqual(f.whole_part, 2)

    def test_15(self):
        f = Fraction(1, 2)
        self.assertEqual(f.float_repr, 0.5)

    def test_16(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-1, 3)
        self.assertEqual(f1 + f2, Fraction(1, 6))

    def test_17(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-1, 3)
        self.assertEqual(f1 - f2, Fraction(5, 6))

    def test_18(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-3, 4)
        self.assertEqual(f1 * f2, Fraction(-3, 8))

    def test_19(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-1, 3)
        self.assertEqual(f1 / f2, Fraction(-3, 2))

    def test_20(self):
        f = Fraction(5, 1)
        self.assertEqual(f.num, 5)
        self.assertEqual(f.den, 1)

    def test_21(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertEqual(f1, f2)

    def test_22(self):
        f = Fraction(4, 8)
        self.assertEqual(f, Fraction(1, 2))

    def test_23(self):
        f = Fraction(1, 2)
        self.assertEqual(repr(f), "Fraction(1, 2)")

    def test_24(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_25(self):
        self.assertEqual(Fraction(0, 5), Fraction(0, 1))

    def test_26(self):
        with self.assertRaises(TypeError):
            Fraction("1", 2)
        with self.assertRaises(TypeError):
            Fraction(1, "2")

    def test_27(self):
        f = Fraction(3, 1)
        self.assertTrue(f == 3)
        self.assertTrue(f >= 3)
        self.assertTrue(f <= 3)

    def test_28(self):
        self.assertEqual(Fraction(-3, -4), Fraction(3, 4))
        self.assertEqual(Fraction(-3, 4), Fraction(-3, 4))

    def test_29(self):
        self.assertEqual(2 + Fraction(1, 3), Fraction(7, 3))

    def test_30(self):
        self.assertEqual(Fraction(1, 3) + 2, Fraction(7, 3))

    def test_31(self):
        self.assertEqual(1 - Fraction(1, 3), Fraction(2, 3))

    def test_32(self):
        self.assertEqual(Fraction(1, 3) - 1, Fraction(-2, 3))

    def test_33(self):
        self.assertEqual(3 * Fraction(1, 4), Fraction(3, 4))

    def test_34(self):
        self.assertEqual(Fraction(1, 4) * 3, Fraction(3, 4))

    def test_35(self):
        self.assertEqual(1 / Fraction(1, 2), Fraction(1, 1))

    def test_36(self):
        self.assertEqual(Fraction(1, 2) / 2, Fraction(1, 4))

    def test_37(self):
        f = Fraction(4, 6)
        f.num = 10
        self.assertEqual(f, Fraction(10, 3))
        f.den = 12
        self.assertEqual(f, Fraction(10, 12))

    def test_38(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f.num = 1.5
        with self.assertRaises(TypeError):
            f.den = "3"
        with self.assertRaises(ValueError):
            f.den = 0

    def test_39(self):
        self.assertTrue(Fraction(5, 2) > 2)
        self.assertTrue(Fraction(3, 2) >= 1)
        self.assertTrue(Fraction(1, 2) < 1)
        self.assertTrue(Fraction(1, 2) <= 1)

    def test_40(self):
        self.assertEqual(Fraction(-3, 2).whole_part, -2)

    def test_41(self):
        self.assertEqual(Fraction(-3, 2).float_repr, -1.5)

    def test_42(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            _ = f + 0.5
        with self.assertRaises(TypeError):
            _ = 0.5 + f
        with self.assertRaises(TypeError):
            _ = f - 0.5
        with self.assertRaises(TypeError):
            _ = 0.5 - f
        with self.assertRaises(TypeError):
            _ = f * 0.5
        with self.assertRaises(TypeError):
            _ = 0.5 * f
        with self.assertRaises(TypeError):
            _ = f / 0.5
        with self.assertRaises(TypeError):
            _ = 0.5 / f

    def test_43(self):
        self.assertEqual(Fraction(1000, 2500), Fraction(2, 5))

if __name__ == "__main__":
    unittest.main()
