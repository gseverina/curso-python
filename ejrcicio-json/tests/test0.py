import unittest
import src

class TestPerson(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_person(self):
        p = src.Person.Person('Juan','Perez','1990-08-23')
        self.assertEqual(p.name,'Juan','Person name not equal.')
        self.assertEqual(p.last_name,'Perez','Person last_name not equal')
        self.assertEqual(p.birth,'1990-08-23','Person birth date not equel')

if __name__ == '__main__':
        unittest.main()

