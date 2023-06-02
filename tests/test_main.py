import io
import unittest
from unittest import mock

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

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_parser_printer(self, mock_stdout):
        main.parser_printer('data/data.log')
        expected_result = """0 : Multiple de 5
            1 : {"player": {"first_name": "Sergio", "last_name": "Ramos", "Age": 34}, "team": "Real Madrid", "pair": false}
            2 : {"player": {"first_name": "Kylian", "last_name": "Mbappé", "Age": 22}, "team": "PSG", "pair": true}
            3 : Rien à afficher
            4 : Rien à afficher
            5 : Multiple de 5
            6 : {"player": {"first_name": "Luis", "last_name": "Suárez", "Age": 34}, "team": "Atlético Madrid"}.
            7 : Rien à afficher
            8 : Process_9000_suc$esfully_run
            9 : Rien à afficher
            10 : Multiple de 5
            11 : Rien à afficher
            12 : Match_95687_has_fin$shed
            13 : {"player": {"first_name": "Jamie", "last_name": "Vardy", "Age": 34}, "team": "Leicester", "pair": false}
            14 : Rien à afficher
            15 : Multiple de 5
            16 : Process 498758 succesfully run.
        """
        self.assertEqual(mock_stdout.getvalue(), expected_result.replace('    ', ''))


if __name__ == '__main__':
    unittest.main()
