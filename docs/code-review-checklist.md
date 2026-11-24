# Code review checklist

Use this as a prompt, not a rigid gate. Not every question applies to every change.

## Correctness

- [ ] Does the change solve the stated problem?
- [ ] Are edge cases and failure paths handled intentionally?
- [ ] Are inputs validated at the right boundary?
- [ ] Are errors explicit and useful to callers?

## Design and maintainability

- [ ] Are names and function signatures clear?
- [ ] Does each module have a cohesive responsibility?
- [ ] Are business rules separated from infrastructure details?
- [ ] Are dependencies explicit and directed toward stable contracts?
- [ ] Is the abstraction proportionate to the problem?

## Tests

- [ ] Do tests verify observable behavior?
- [ ] Are important success and failure paths covered?
- [ ] Are test doubles simpler than the behavior they replace?
- [ ] Does the full test suite pass?

## Python and operations

- [ ] Are public boundaries type-annotated?
- [ ] Are secrets and environment-specific values kept out of source control?
- [ ] Are logs useful without exposing sensitive data?
- [ ] Are dependencies justified and pinned appropriately for the project?
- [ ] Do lint and formatting checks pass?

## Documentation

- [ ] Are setup or usage instructions still correct?
- [ ] Are examples runnable?
- [ ] Are meaningful trade-offs and limitations explained?
