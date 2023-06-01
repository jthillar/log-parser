import unittest
import check


class TestLineCheck(unittest.TestCase):

    # Tests of row_number_is_multiple_of_five
    def test_row_number_is_multiple_of_five_true(self):
        self.assertTrue(check.row_number_is_multiple_of_five(5))

    def test_row_number_is_multiple_of_five_false(self):
        self.assertFalse(check.row_number_is_multiple_of_five(3))

    def test_row_number_is_multiple_of_five_false_0(self):
        self.assertTrue(check.row_number_is_multiple_of_five(0))

    # Tests of row_with_dollar_sign
    def test_row_with_dollar_sign_true(self):
        self.assertTrue(check.row_with_dollar_sign("Hello$World"))

    def test_row_with_dollar_sign_false(self):
        self.assertFalse(check.row_with_dollar_sign("Hello World"))

    # Tests of row_end_swith_comma
    def test_row_endswith_comma_true(self):
        self.assertTrue(check.row_ends_with_comma("Hello$World."))

    def test_row_endswith_comma_false(self):
        self.assertFalse(check.row_ends_with_comma("Hello World"))

    # Tests of row_starts_with_curly_bracket
    def test_row_starts_with_curly_bracket_true(self):
        self.assertTrue(check.row_ends_with_comma("{Hello$World."))

    def test_row_starts_with_curly_bracket_false(self):
        self.assertFalse(check.row_ends_with_comma("H{ello World}"))


if __name__ == '__main__':
    unittest.main()
