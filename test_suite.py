import unittest

from src.tests.DeleteBlogTestCase import DeleteBlogTestCase
from src.tests.getters_test.test_get_all_blogs import GeAllBlogsTestCase
from src.tests.getters_test.test_get_blog_detail import GetBlogDetailTestCase
from src.tests.getters_test.test_get_blogs_user_id import GetBlogsByUserIdTestCase
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
suite6 = unittest.TestLoader().loadTestsFromTestCase(GetBlogsByUserIdTestCase)
suite7 = unittest.TestLoader().loadTestsFromTestCase(GetBlogDetailTestCase)
suite8 = unittest.TestLoader().loadTestsFromTestCase(GeAllBlogsTestCase)
suite9 = unittest.TestLoader().loadTestsFromTestCase(DeleteBlogTestCase)
suite_set = unittest.TestSuite(tests=[suite1, suite2, suite3, suite4,
                                      suite5, suite6, suite7, suite8,
                                      suite9])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_set)
