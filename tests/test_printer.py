import io
import unittest
from unittest import mock

from src import printer


class PrinterTest(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_multiple_of_five(self, mock_stdout):
        printer.print_multiple_of_five(1)
        self.assertEqual(mock_stdout.getvalue(), '1 : Multiple de 5\n')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_space_as_underscore(self, mock_stdout):
        printer.print_space_as_underscore(2, 'Hello World')
        self.assertEqual(mock_stdout.getvalue(), '2 : Hello_World\n')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_line(self, mock_stdout):
        printer.print_data(1, 'This is the line')
        self.assertEqual(mock_stdout.getvalue(), '1 : This is the line\n')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dict_with_pair_info_as_pair(self, mock_stdout):
        json_test = '{"Hello": "World"}'
        json_res_pair = '{"Hello": "World", "pair": true}'
        printer.print_dict_with_pair_info(2, json_test)
        self.assertEqual(mock_stdout.getvalue(), f'2 : {json_res_pair}\n')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dict_with_pair_info_as_impair(self, mock_stdout):
        json_test = '{"Hello": "World"}'
        json_res_impair = '{"Hello": "World", "pair": false}'
        printer.print_dict_with_pair_info(1, json_test)
        self.assertEqual(mock_stdout.getvalue(), f'1 : {json_res_impair}\n')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_new_data(self, mock_stdout):
        printer.print_new_data(1, 'Hello World')
        self.assertEqual(mock_stdout.getvalue(), f'1 : Hello World\n')


if __name__ == '__main__':
    unittest.main()
