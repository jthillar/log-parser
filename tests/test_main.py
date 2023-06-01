import unittest
import main


class TestArgument(unittest.TestCase):

    def test_check_file_as_argument_missing_arg(self):
        with self.assertRaises(RuntimeError) as context:
            main.check_one_file_as_argument(['main.py'])
        self.assertTrue('Missing file path' in str(context.exception))

    def test_check_file_as_argument_more_than_2_args(self):
        with self.assertRaises(RuntimeError) as context:
            main.check_one_file_as_argument(['one', 'two', 'three'])
        self.assertTrue('Must be only one file to read' in str(context.exception))

    def test_check_file_as_argument_wrong_file_type(self):
        with self.assertRaises(RuntimeError) as context:
            main.check_one_file_as_argument(['main.py', 'hello.world'])
        self.assertTrue('You must use a .log file' in str(context.exception))

    def test_check_file_as_argument_file_error(self):
        with self.assertRaises(RuntimeError) as context:
            main.check_one_file_as_argument(['main.py', 'hello.log'])
        self.assertTrue('File doesn\'t exist' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
