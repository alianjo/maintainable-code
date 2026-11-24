# Maintainable Code

A practical Python learning repository for writing software that is easier to understand, test, change, and extend.

This repository combines **short engineering guides** with a **runnable example application**. It is intended to be studied incrementally: read a principle, inspect the implementation, run the tests, then try the exercises.

## What is included?

- **Fundamentals:** clean code, naming, small functions, cohesion, coupling, and useful comments.
- **SOLID:** all five principles with Python-oriented examples and trade-offs.
- **Design and architecture:** composition, dependency inversion, ports and adapters, and pragmatic design patterns.
- **Testing:** unit and integration tests, test doubles, behavior-focused assertions, and a practical TDD workflow.
- **Python practices:** type hints, `Protocol`, dataclasses, exceptions, project configuration, and code quality automation.
- **A working example:** a small checkout flow separated into domain, application, and infrastructure layers.
- **Automation:** pytest, Ruff, and a GitHub Actions workflow.

## Learning path

Start with [the learning path](docs/learning-path.md), then follow the guides in order. You do not need to read everything at once.

| Area | Guide | What you will learn |
|---|---|---|
| Fundamentals | [Clean Code](docs/principles/clean-code.md) | Naming, functions, boundaries, comments, and readability |
| Principles | [SOLID](docs/principles/solid.md) | Designing modules that are easier to change |
| Programming styles | [OOP and Functional Programming](docs/principles/oop-and-functional.md) | Modeling state and writing deterministic transformations |
| Architecture | [Layered Architecture](docs/architecture/layered-architecture.md) | Separating business rules from details |
| Testing | [Testing and TDD](docs/testing/tdd-and-pytest.md) | Tests as feedback and executable documentation |
| Maintenance | [Refactoring](docs/techniques/refactoring.md) | Improving structure without changing behavior |
| Python | [Type Hints and Protocols](docs/python/type-hints-and-protocols.md) | Making boundaries explicit with Python typing |
| Reliability | [Error Handling and Logging](docs/python/error-handling-and-logging.md) | Making failures diagnosable and safe to handle |
| Design | [Design Patterns](docs/patterns/design-patterns.md) | Applying patterns only when they solve a real problem |
| Quality | [Review Checklist](docs/code-review-checklist.md) | A repeatable checklist for everyday work |

## Quick start

Python 3.11 or newer is required. The application itself uses only the Python standard library; pytest and Ruff are development tools.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m maintainable_shop.demo
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m maintainable_shop.demo
```

## Project structure

```text
maintainable-code/
├── .github/workflows/ci.yml
├── docs/                         # Conceptual guides and checklists
├── examples/                     # Small focused examples
├── src/maintainable_shop/
│   ├── domain/                    # Business rules and domain objects
│   ├── application/               # Use cases and dependency contracts
│   ├── infrastructure/            # In-memory development adapters
│   └── demo.py                    # Runnable composition example
├── tests/
│   ├── unit/
│   └── integration/
├── pyproject.toml
└── README.md
```

## Example architecture

The checkout example intentionally stays small so the boundaries are visible:

- `domain` contains `Money`, `Order`, and `OrderItem`. It does not import database, network, or framework code.
- `application` contains the checkout use case and `Protocol` contracts for payment, persistence, notifications, and discount policies.
- `infrastructure` contains in-memory adapters suitable for learning and tests—not production payment or database integrations.
- `tests` verify domain behavior and the full checkout flow without network access.

The example demonstrates separation of concerns and dependency inversion. It is **not** a production-ready commerce system: it does not solve distributed transactions, payment idempotency, authentication, tax, inventory, or real payment processing.

## Quality commands

```bash
python -m pytest                 # Run all tests
python -m pytest -q              # Compact test output
python -m ruff check .           # Lint
python -m ruff format --check .  # Verify formatting
python -m ruff format .         # Apply formatting
```

## Contributing

Contributions should improve clarity or correctness, not add abstraction for its own sake. Before opening a pull request:

1. Explain the problem the change solves.
2. Keep examples runnable and focused.
3. Add or update tests when behavior changes.
4. Run the quality commands above.
5. Update the relevant guide when the design lesson changes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and [the review checklist](docs/code-review-checklist.md) before submitting changes.

## Repository history and licensing note

This repository began as a fork of [alianjo/maintainable-code](https://github.com/alianjo/maintainable-code). The current version expands the original topic outline with independently written guides, code, tests, and automation. The upstream repository did not expose a license in its GitHub repository metadata when this revision was prepared; do not assume that the inherited upstream material is relicensed. Review the upstream repository's licensing status before redistributing inherited material.
