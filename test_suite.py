import unittest
from src.tests.test_insert_user import InsertUser


suite1 = unittest.TestLoader().loadTestsFromTestCase(InsertUser)
suite_set = unittest.TestSuite(tests=[suite1, ])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_set)
