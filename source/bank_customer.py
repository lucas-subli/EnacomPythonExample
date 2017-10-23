

# An example of a class
class BankCustomer(object):
    """
    A customer of ABC Bank with a checking account.

    Attributes:
        name (str): A string representing the customer's name.
        balance (:obj:`int`, optional): A float tracking the current balance of the customer's account.
    """

    # Init should always be the first method
    def __init__(self, name, balance=0.0):
        """
        Return a Customer object whose name is *name* and starting balance is *balance*.

        Args:
            name (str): The account owner complete name
            balance (:obj:`float`, optional): the initial balance, defaults to 0
        """

        self.name = name
        self.balance = balance

    # method names should be lowercase
    def withdraw_money(self, amount):
        """
        Return the balance remaining after withdrawing *amount* dollars.

        Args:
            amount (float): Amount to withdraw in dollars.

        Returns:
            float: The balance after the withdraw.

        Examples:
            >>> john = BankCustomer('John', 30000.0)
            >>> print(john.withdraw_money(500))
            29500.0

        Raises:
            RuntimeError: If `amount` is bigger than the balance.

        """
        # TODO: Not allow negative values

        if amount > self.balance:
            # mid code comments are not only allowed but recommended
            # and treat your exceptions!
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit_money(self, amount):
        """
        Return the balance remaining after depositing *amount* dollars.

        Args:
            amount: Amount to deposit in dollars.

        Returns: The balance after the deposit.

        """

        self.balance += amount
        return self.balance

# Files must End with a newline
