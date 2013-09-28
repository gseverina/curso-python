import unittest
import src


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p = src.Person.Person('Juan', 'Perez', '1990-08-23')

    def test_init_person(self):
        self.assertEqual(self.p.name, 'Juan')
        self.assertEqual(self.p.last_name, 'Perez')
        self.assertEqual(self.p.birth, '1990-08-23')

    def test_to_dict(self):
        assert isinstance(self.p.to_dict(), dict)

if __name__ == '__main__':
        unittest.main()
