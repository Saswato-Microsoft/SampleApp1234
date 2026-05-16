"""Module demonstrating race conditions, deadlocks, and threading exceptions."""

import threading
import time


class BankAccount:
    """Bank account with no thread safety."""

    def __init__(self, balance=1000):
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw without locking - race condition bug."""
        if self.balance >= amount:
            time.sleep(0.01)  # Simulates processing delay; exposes race condition
            self.balance -= amount
            return True
        return False

    def transfer(self, other, amount):
        """Transfer money between accounts - potential deadlock."""
        self.lock = threading.Lock()
        other.lock = threading.Lock()
        # Bug: Deadlock when two threads transfer in opposite directions
        with self.lock:
            time.sleep(0.01)
            with other.lock:
                if self.balance >= amount:
                    self.balance -= amount
                    other.balance += amount


class SharedCounter:
    """Counter with lost-update bug."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment is not atomic - lost update bug."""
        current = self.count
        time.sleep(0.001)
        self.count = current + 1  # Bug: race condition, lost updates


def run_race_condition():
    account = BankAccount(balance=100)
    threads = []
    for _ in range(20):
        t = threading.Thread(target=account.withdraw, args=(10,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # Bug: balance can go negative due to race condition
    print(f"Final balance: {account.balance}")


if __name__ == "__main__":
    run_race_condition()
