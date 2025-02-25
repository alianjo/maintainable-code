# Organizing Code Properly

## Explanation:
Code should be structured logically to enhance readability. Proper organization of code helps in maintaining and scaling projects, making them easier to understand for other developers or even future you.

### Bad Example:

```python
class Order:
    def __init__(self, items):
        self.items = items
    
    def total_price(self):
        return sum(self.items)
    
    def print_invoice(self):
        print("Order details...")

Problem: The class mixes business logic and presentation logic.

Good Example:

class Order:
    def __init__(self, items):
        self.items = items
    
    def total_price(self):
        return sum(self.items)

class InvoicePrinter:
    def print(self, order: Order):
        print(f"Order total: {order.total_price()}")
Why is this better?

Separation of Concerns:

The Order class only handles order-related logic, such as calculating the total price.

The InvoicePrinter class is responsible for printing the invoice details.

Modularity:

Each class has a single responsibility, making the code modular and easier to maintain. Changes in one part of the code will have minimal impact on others.

Reusability:

The InvoicePrinter class can be reused with different order classes or even extended for different types of outputs (e.g., PDF, HTML).

Testability:

Each class can be tested independently. For instance, you can test the Order class without worrying about how the invoice is printed.

Detailed Explanation:
Separation of Concerns: This principle ensures that different aspects of the program are separated, making it easier to manage and reduce the risk of introducing bugs when making changes.

Modularity: Modular code is easier to read, understand, and modify. Each part of the codebase has a clear purpose and can be developed and maintained independently.

Reusability: When code is organized into reusable modules, it reduces redundancy and makes it easier to use the same code in different parts of the project or even in other projects.

Testability: Well-organized code is easier to test. When functions and classes have clearly defined responsibilities, writing unit tests becomes straightforward.

By following these principles, you ensure that your code is easier to understand, maintain, and scale.