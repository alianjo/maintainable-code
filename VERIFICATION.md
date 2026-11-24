# Verification report

Last checked: 2026-11-24

| Check | Result | Notes |
|---|---|---|
| Unit and integration tests | PASS | 32 tests passed with pytest 9.0.2 |
| Python bytecode compilation | PASS | `compileall` completed for `src`, `tests`, and `examples` |
| Demo execution | PASS | Checkout completed using the in-memory adapters |
| Internal Markdown links | PASS | 17 Markdown documents checked; no broken local links found |
| Ruff lint and formatting | NOT RUN | Ruff was not installed in the execution environment and package installation was unavailable because network access was disabled |

Run the remaining quality checks locally after installing the development dependencies:

```powershell
python -m pip install -e ".[dev]"
python -m ruff check .
python -m ruff format --check .
```

The GitHub Actions workflow runs lint, formatting, and tests on Python 3.11, 3.12, and 3.13 for pushes to `main` and pull requests.
