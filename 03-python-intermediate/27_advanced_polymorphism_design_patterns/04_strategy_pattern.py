"""
Lesson 27.5 - Strategy Pattern

This lesson demonstrates the Strategy Design Pattern.

Topics:
- Strategy Pattern
- Separation of Concerns
- Composition
- Polymorphism
- Runtime strategy selection

Key idea:

The Strategy Pattern allows us to define different
ways of performing an operation and select the
appropriate strategy at runtime.

Example:

Payment
   |
   +-- CreditCardPayment
   +-- PayPalPayment
   +-- BankTransferPayment
"""


# ============================================================
# 1. Strategy Classes
# ============================================================

class CreditCardPayment:
    """Define a payment strategy using a credit card."""

    def pay(self, amount: float) -> str:
        """Process payment using a credit card."""
        return f"Paid ${amount:.2f} using Credit Card"


class PayPalPayment:
    """Define a payment strategy using PayPal."""

    def pay(self, amount: float) -> str:
        """Process payment using PayPal."""
        return f"Paid ${amount:.2f} using PayPal"


class BankTransferPayment:
    """Define a payment strategy using bank transfer."""

    def pay(self, amount: float) -> str:
        """Process payment using a bank transfer."""
        return f"Paid ${amount:.2f} using Bank Transfer"


# ============================================================
# 2. Context Class
# ============================================================

class PaymentProcessor:
    """
    Context class that uses a payment strategy.

    The PaymentProcessor does not need to know
    how the payment is processed.

    It delegates the payment operation to
    the selected strategy.
    """

    def __init__(self, strategy) -> None:
        """Initialize the payment processor with a strategy."""
        self.strategy = strategy

    def process_payment(self, amount: float) -> str:
        """Process the payment using the selected strategy."""
        return self.strategy.pay(amount)


# ============================================================
# 3. Main
# ============================================================

def main() -> None:
    """Demonstrate the Strategy Pattern."""

    # Create different payment strategies.
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()

    # Create the context using the Credit Card strategy.
    processor = PaymentProcessor(credit_card)

    print(processor.process_payment(100.00))

    # Change the strategy at runtime.
    processor.strategy = paypal

    print(processor.process_payment(250.00))

    # Change the strategy again.
    processor.strategy = bank_transfer

    print(processor.process_payment(500.00))


if __name__ == "__main__":
    main()
