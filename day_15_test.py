def add(a, b):
    return a + b
 
 
import unittest
 
#  Task 1 :add unit testcase for negative numbers
# Task 2 :add unit testcase for decimal numbers
class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
    def test_add_for_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
    def test_add_decimal_numbers(self):
        self.assertEqual(add(1.2, 2.3), 3.5)
 
def adds_interest(self):
    pass
 
class TestInterestModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        print("Setup Ran...")
        self.accounts = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "johndoe@example.com",
                "isActive": True,
                "balance": 150.75,
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "janesmith@example.com",
                "isActive": True,
                "balance": 500.50,
            },
            {
                "id": 3,
                "name": "Emily Jones",
                "email": "emilyjones@example.com",
                "isActive": True,
                "balance": 0.00,
            },
        ]
 
    def tearDown(self):
        print("TearDown : Clear cursor")
 
    def test_interest_rate_for_active_user(self):
        # Act
        # output = adds_interest(self.accounts, 0.1)
        print("Test 1")
        # Assert
        self.assertEqual(add(1.2, 3.2), 4.4)
 
    def test_interest_rate_for_non_active_user(self):
        # output = adds_interest(self.accounts, 0.1)
        print("Test 2")
        # self.assertEqual(output[1]["balance"], 500.5)
 
 
 
if __name__ == "__main__":
    unittest.main()