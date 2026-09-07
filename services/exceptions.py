
class DomainException(Exception):
    """Base exception for all domain business errors."""
    pass

class UserNotFoundException(DomainException):
    """Raised when a user cannot be found."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} was not found.")

class InsufficientBalanceException(DomainException):
    """Raised when a wallet balance is too low."""
    def __init__(self, balance: float, required: float):
        self.balance = balance
        self.required = required
        super().__init__(f"Insufficient funds: Balance is ${balance:.2f}, but required ${required:.2f}.")
