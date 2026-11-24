# Refactoring safely

Refactoring is a behavior-preserving change to the internal structure of software. A feature change alters behavior; a refactoring should not.

## A safe sequence

1. Identify the behavior that must remain unchanged.
2. Add or improve a test that captures that behavior.
3. Make one small structural change.
4. Run the focused test, then the full suite.
5. Review the diff for accidental behavior changes.
6. Repeat only while each step remains easy to understand.

## Common refactorings

### Rename for clarity

Change a vague name to one that communicates the domain meaning. Let the IDE or language-aware tooling update references.

### Extract a function

Move a coherent block into a named function when the name clarifies intent or allows independent testing.

### Replace conditional variation with a policy

When several algorithms vary independently and the variation is expected to grow, move each algorithm behind a small common contract. Do not do this for every two-branch conditional.

### Introduce a parameter object

Group parameters that represent one cohesive concept and are repeatedly passed together. Avoid data classes that merely collect unrelated values.

### Separate side effects

Keep calculations deterministic and move network, file, database, or messaging operations to explicit boundaries.

## Warning signs

- A broad rewrite mixes formatting, behavior, and architecture changes.
- A test asserts private method calls rather than observable results.
- A new abstraction has only one trivial implementation and no plausible variation.
- A refactor changes public behavior without a test or migration plan.

Small steps make failures easier to locate and code review easier to perform.
