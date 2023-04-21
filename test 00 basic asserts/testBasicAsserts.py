import unittest
import warnings


class MyTests(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(2 + 2, 4) # Check for equality

    def test_assert_not_equal(self):
        self.assertNotEqual(2 + 2, 5) # Check for inequality

    def test_assert_true(self):
        self.assertTrue(2 + 2 == 4) # Truth check

    def test_assert_false(self):
        self.assertFalse(2 + 2 == 5) # False check

    def test_assert_is(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b) # Check for identity of objects

    def test_assert_is_not(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b) # Check for non-identity of objects

    def test_assert_in(self):
        a = [1, 2, 3]
        self.assertIn(2, a) # Check for the presence of an element in the sequence

    def test_assert_not_in(self):
        a = [1, 2, 3]
        self.assertNotIn(4, a) # Check for the absence of an element in the sequence

    def test_assert_is_none(self):
        a = None
        self.assertIsNone(a) # Check for equality with None

    def test_assert_is_not_none(self):
        a = 42
        self.assertIsNotNone(a) # Test for inequality with None

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, delta=0.00001) # Check for approximate equality of numbers with a given delta

    def test_assert_not_almost_equal(self):
        self.assertNotAlmostEqual(0.1 + 0.2, 0.3, places=20) # delta=0.00001 or places=20 Check for non-approximate equality of numbers with a given delta

    def test_assert_raises(self):
        with self.assertRaises(ValueError): # Check for a specific exception
            int("abc")

    def test_assert_warns(self):
        with self.assertWarns(DeprecationWarning):
            warnings.warn("This function is deprecated", DeprecationWarning) # Check for a specific warning

    def test_assert_regex(self):
        self.assertRegex("hello world", r'hello') # Check for regular expression match
    
    def test_assert_not_regex(self):
        self.assertNotRegex("hello world", r'goodbye') # Check for non-matching regular expression


if __name__ == '__main__':
    unittest.main()