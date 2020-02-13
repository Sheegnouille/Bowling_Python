import unittest
import Bowling

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, False)

    def test_compute_score(self):
        self.assertEqual(Bowling.compute_score("--------------------"), 0)
        self.assertEqual(Bowling.compute_score("1-------------------"), 1)
        self.assertEqual(Bowling.compute_score("-------------------1"), 1)
        self.assertEqual(Bowling.compute_score("--------1-----------"), 1)
        self.assertEqual(Bowling.compute_score("1-1-1-1-1-1-1-1-1-1-"), 1)
        self.assertEqual(Bowling.compute_score("2-------------------"), 2)
        self.assertEqual(Bowling.compute_score("9-9-9-9-9-9-9-9-9-9-"), 9)

if __name__ == '__main__':
    unittest.main()
