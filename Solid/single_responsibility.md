# Single Responsibility Principle (SRP)

## Explanation  
The **Single Responsibility Principle (SRP)** states that a class should have **only one reason to change**.  
This means that a class should have **one responsibility** and should not mix multiple concerns.

##  Bad Example – Violating SRP:
```python
class Report:
    def generate(self):
        return "Generating report content..."
    
    def save_to_file(self):
        with open("report.txt", "w") as file:
            file.write(self.generate())
Problem: The Report class has two responsibilities:

Generating the report content
Saving the report to a file
Good Example – Applying SRP:
class Report:
    def generate(self):
        return "Generating report content..."

class ReportSaver:
    def save_to_file(self, report: Report):
        with open("report.txt", "w") as file:
            file.write(report.generate())
Why is this better?
✔ Report is responsible only for generating content.
✔ ReportSaver is responsible only for saving the file.