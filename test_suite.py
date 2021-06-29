import unittest
from src.tests.test_insert_user import InsertUser
from src.tests.test_insert_blog import InsertBlog


suite1 = unittest.TestLoader().loadTestsFromTestCase(InsertUser)
suite2 = unittest.TestLoader().loadTestsFromTestCase(InsertBlog)
suite_set = unittest.TestSuite(tests=[suite1, suite2, ])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_set)
