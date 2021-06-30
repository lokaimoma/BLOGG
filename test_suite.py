import unittest
from src.tests.insert_tests.test_insert_user import InsertUser
from src.tests.insert_tests.test_insert_blog import InsertBlog
from src.tests.insert_tests.test_insert_engagement import InsertEngament


suite1 = unittest.TestLoader().loadTestsFromTestCase(InsertUser)
suite2 = unittest.TestLoader().loadTestsFromTestCase(InsertBlog)
suite3 = unittest.TestLoader().loadTestsFromTestCase(InsertEngament)
suite_set = unittest.TestSuite(tests=[suite1, suite2, suite3, ])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_set)
