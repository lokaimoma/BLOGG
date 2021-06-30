import unittest
from src.tests.insert_tests.test_insert_user import InsertUser
from src.tests.insert_tests.test_insert_blog import InsertBlog
from src.tests.insert_tests.test_insert_engagement import InsertEngament
from src.tests.update_tests.test_update_blog import UpdateBlogTestCase
from src.tests.update_tests.test_update_engagement import UpdateEngagementTestCase

suite1 = unittest.TestLoader().loadTestsFromTestCase(InsertUser)
suite2 = unittest.TestLoader().loadTestsFromTestCase(InsertBlog)
suite3 = unittest.TestLoader().loadTestsFromTestCase(InsertEngament)
suite4 = unittest.TestLoader().loadTestsFromTestCase(UpdateBlogTestCase)
suite5 = unittest.TestLoader().loadTestsFromTestCase(UpdateEngagementTestCase)
suite_set = unittest.TestSuite(tests=[suite1, suite2, suite3, suite4, suite5])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_set)
