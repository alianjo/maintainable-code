# Dependency Inversion Principle (DIP)

## Explanation  
The **Dependency Inversion Principle (DIP)** states that **high-level modules should not depend on low-level modules**. Instead, both should depend on **abstractions**. This helps decouple the code and makes it more maintainable.

---

## Bad Example – Violating DIP:
```python
class MySQLDatabase:
    def connect(self):
        return "Connected to MySQL"

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on a low-level module

    def get_users(self):
        return f"Fetching users from {self.database.connect()}"
Problem:

UserService is tightly coupled with MySQLDatabase.
If we need to switch databases (e.g., PostgreSQL), we must modify UserService, violating OCP too!
Good Example – Applying DIP:
from abc import ABC, abstractmethod

# Define an abstraction (interface)
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# Implement concrete classes
class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"

# High-level module depends on abstraction
class UserService:
    def __init__(self, database: Database):
        self.database = database  # Dependency Injection

    def get_users(self):
        return f"Fetching users from {self.database.connect()}"
Why is this better?
✔ UserService is independent of any specific database implementation.
✔ We can easily switch to PostgreSQLDatabase without modifying UserService.
✔ The code follows OCP and **D