from unittest import TestCase
import utils


class TestUtils(TestCase):
    def test_read_ip_addresses_file_read_one_record(self):
        expected = {(0, 1): '0.0.0.1'}

        result = utils.read_ip_addresses_file('test_one_record.txt')

        self.assertEqual(expected, result)

    def test_read_ip_addresses_file_reading_nonexistent(self):
        self.assertRaises(FileNotFoundError, utils.read_ip_addresses_file, 'nonexistent.txt')

    def test_read_ip_addresses_file_read_many_records(self):
        expected = {(0, 1): '0.0.0.1',
                    (2, 1): '0.0.3.2'}

        result = utils.read_ip_addresses_file('test_many_records.txt')

        self.assertEqual(expected, result)

    def test_read_ip_addresses_file_with_non_unique_ip_address(self):
        self.assertRaisesRegex(ValueError,
                               'Non unique ip address',
                               utils.read_ip_addresses_file,
                               'test_records_with_non_unique_ip_address.txt')

    def test_read_ip_addresses_file_with_non_unique_key(self):
        self.assertRaisesRegex(ValueError,
                               'Non unique key',
                               utils.read_ip_addresses_file,
                               'test_records_with_non_unique_key.txt')

    def test_read_ip_addresses_file_with_syntax_error(self):
        self.assertRaisesRegex(SyntaxError,
                               'Syntax error in file with ip addresses',
                               utils.read_ip_addresses_file,
                               'test_records_with_syntax_error1.txt')
        self.assertRaisesRegex(SyntaxError,
                               'Syntax error in file with ip addresses',
                               utils.read_ip_addresses_file,
                               'test_records_with_syntax_error2.txt')
