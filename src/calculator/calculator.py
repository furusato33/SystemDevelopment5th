"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""



    def add(self, a, b):
        self.validate_input(a, b)
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        return a + b

    def subtract(self, a, b):
        self.validate_input(a, b)
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        return a - b

    def multiply(self, a, b):
        self.validate_input(a, b)
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        return a * b

    def divide(self, a, b):
        self.validate_input(a, b)
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def validate_input(self, a, b):
        """Validate that the input is within the acceptable range.

        Args:
            value: The number to validate
        Raises:
            InvalidInputException: If value is outside the range -1000 to 1000
        """

        if a >=100000 or a <= -100000:
            raise InvalidInputException()
        if b >=100000 or b <= -100000:
            raise InvalidInputException()

