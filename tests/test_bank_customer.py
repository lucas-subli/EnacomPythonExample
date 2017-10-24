import unittest
import sys
from source import bank_customer as bank


# Example of tests, you do need to comment this ones as well
class TestBankCustomer(unittest.TestCase):
    """
    Tests Bank Customer class
    """

    def setUp(self):
        """
        Tests the SetUp of the class
        setUp is not written set_up for historical reasons

        """
        self.account = bank.BankCustomer(name="Jonathan", balance=100)
        self.assertEqual(self.account.balance, 100)
        self.assertEqual(self.account.name, "Jonathan")

        account2 = bank.BankCustomer(name="James")
        self.assertEqual(account2.balance, 0)
        self.assertEqual(account2.name, "James")

    def test_withdraw_money(self):
        """
        Tests the withdraw money function
        """
        self.account.withdraw_money(50)
        self.assertEqual(self.account.balance, 50)

        # The code should not allow to withdraw more money than the balance
        try:
            self.account.withdraw_money(200)
        except RuntimeError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_deposit_money(self):
        """
        Tests the deposit money function
        """
        self.account.deposit_money(50)
        self.assertEqual(self.account.balance, 150)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        """
        Demonstrates skipping tests
        """
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.platform.startswith("win"), "does not run in Windows")
    def test_format(self):
        """
        Demonstrates Tests that won't work on windows.
        """
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        """
        Demonstrates Tests that will only work on windows.
        """
        pass
