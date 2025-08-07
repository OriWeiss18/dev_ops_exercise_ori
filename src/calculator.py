class Calculator:
    # This is a test comment to trigger the pipeline
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        print("Feature branch addition")
        print("Main branch update")
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    @staticmethod
    def power(a: float, b: float) -> float:
        """Raise a to the power of b."""
        return a ** b
