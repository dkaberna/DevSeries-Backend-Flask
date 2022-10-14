"""
test_app.py
--------
Provides unit test functionality via UnitTest

"""

import sys
sys.path.append('.')
sys.path.append('..')


import unittest
import app
class FlaskTest(unittest.TestCase):

    # check response 200
 #   def test_index(self):
 #       tester = app.app.test_client(self)
 #       response = tester.get("/getSomeData")
 #       statuscode = response.status_code
 #       self.assertEqual(statuscode, 200)

    # Confirms correct employee was returned
    def test_employee(self):
        tester = app.app.test_client(self)
        response = tester.get('/api/employee/0', follow_redirects=True)
        #json returned should be {"id":1,"name":"Cranston, Bryan","title":"Mission Lead"}
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        html = response.get_data(as_text=True)

        # for debugging purposes
        print("Test output->", html)

        # make sure html returned employee name (as one of the checks, others can also be added)
        assert 'Cranston, Bryan' in html


if __name__ == "__main__":
    unittest.main()