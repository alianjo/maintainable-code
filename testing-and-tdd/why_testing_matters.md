# Why Testing is Important

## Explanation  
**Testing** ensures that our code is **reliable, maintainable, and bug-free**. Without testing, we risk introducing **unexpected failures** and making changes that could break existing functionality.

---

## Example – Unit Test:
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
Why is this useful?
✔ It prevents unexpected failures by catching bugs early.
✔ It makes refactoring safer, allowing us to change code with confidence.
✔ It helps in automating the verification of functionality.