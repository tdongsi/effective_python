
from unittest import TestCase


class ExampleTest(TestCase):

    def setUp(self):
        print('Setup')

    def tearDown(self):
        print('Teardown')

    def test_a(self):
        print('a')

    def test_b(self):
        print('b')
