# Contributing

Thanks for helping make this a useful learning resource.

## Before changing something

- Search the existing guides and examples to avoid duplicating a topic.
- Prefer a small, concrete example over a large framework-like abstraction.
- Explain trade-offs. Avoid presenting a principle as an absolute rule.
- Do not add a dependency unless the learning value justifies its maintenance cost.

## Development workflow

1. Create a focused branch: `git switch -c docs/topic-name` or `git switch -c feature/short-description`.
2. Make the smallest coherent change.
3. Add tests for changed behavior.
4. Run `python -m pytest`, `python -m ruff check .`, and `python -m ruff format --check .`.
5. Update documentation and examples together when needed.
6. Open a pull request with the motivation, design notes, and test results.

## Writing guidelines

- Use direct language and define unfamiliar terms.
- Keep code blocks runnable and format them consistently.
- Show a problematic approach before a better one when that helps explain the reason.
- Mention when an example is intentionally simplified or unsuitable for production.
- Prefer links between related guides over repeating large explanations.
