# Learning path

The goal is not to memorize rules. The goal is to recognize the cost of a design choice and select a proportionate response.

## Suggested sequence

1. **Readability first:** work through [Clean Code](principles/clean-code.md). Practice naming and simplifying one function at a time.
2. **Design boundaries:** read [SOLID](principles/solid.md). Focus on reasons to change and dependency direction, not class counts.
3. **Understand the sample:** inspect `src/maintainable_shop/domain` before the application and infrastructure packages. Read [Layered Architecture](architecture/layered-architecture.md) alongside it.
4. **Test behavior:** follow [Testing and TDD](testing/tdd-and-pytest.md), then run the unit and integration tests.
5. **Improve safely:** use [Refactoring](techniques/refactoring.md) to change structure while keeping behavior stable.
6. **Explore Python tools:** read [Type Hints and Protocols](python/type-hints-and-protocols.md) and [Design Patterns](patterns/design-patterns.md).
7. **Review your own work:** use the [Code Review Checklist](code-review-checklist.md) and complete the [exercises](exercises.md).

## How to study each topic

- Read the explanation once without trying to memorize it.
- Look at the code and identify what would become difficult to change.
- Run the tests and inspect what each test protects.
- Change one behavior, write a test for it, and refactor only after the test passes.
- Write down the trade-off you made. A good design is contextual, not universal.

## Expected outcome

After working through the repository, you should be able to explain why a boundary exists, choose a useful test level, identify common maintainability risks, and improve a small codebase without introducing unnecessary complexity.
