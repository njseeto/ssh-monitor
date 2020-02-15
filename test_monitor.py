import unittest
from monitor import find_ip
from test_cases import possible_break_in, invalid_user, no_threat, lower_case_invalid, london_office


class TestFindIp(unittest.TestCase):
    def test_ips_are_malicious(self):
        self.assertEqual(find_ip(possible_break_in), '101.50.00.222')
        self.assertEqual(find_ip(invalid_user), '101.50.00.111')

    def test_ips_are_not_malicious(self):
        self.assertEqual(find_ip(no_threat), None)
        self.assertEqual(find_ip(lower_case_invalid), None)

    def test_ips_are_not_malicious_if_london_office(self):
        self.assertEqual(None, find_ip(london_office))

if __name__ == '__main__':
    unittest.main()
