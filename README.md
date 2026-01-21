# saucedemo-framework

## Project overview

This repository contains an automated UI test framework for the Sauce Demo application (https://www.saucedemo.com). The framework is organized to make it easy to write, run and extend end-to-end tests against the demo site using a Page Object Model and pytest-based test runners.

Key points:
- Purpose: provide reusable page objects, fixtures and tests for validating common flows on Sauce Demo.
- Designed for local development and CI execution.
- Targets browser-based functional tests using Selenium WebDriver.

## Tech stack

- Python (recommended 3.8+)
- pytest for test execution
- Selenium WebDriver for browser automation
- webdriver-manager or a configured driver binary for browser drivers
- Optional: pytest-html / Allure for reporting (if configured in requirements)

## Prerequisites

1. Python 3.8+ installed
2. Git
3. A browser supported by Selenium (Chrome/Firefox) and corresponding driver (or use webdriver-manager)

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

If requirements.txt is not present, install the typical dependencies:

```bash
python -m pip install pytest selenium webdriver-manager pytest-html
```

## Running tests

From the repository root, example commands:

- Run all tests:
```bash
pytest -q
```

- Run a specific test file:
```bash
pytest tests/test_example.py -q
```

- Run tests with a specific marker (e.g., smoke):
```bash
pytest -m smoke -q
```

- Generate an HTML report (if pytest-html is installed):
```bash
pytest --html=report.html -q
```

If the project includes custom CLI flags or environment variables (browser selection, headless mode), use those as shown in the project's conftest.py or run scripts. Example conventions:
- BROWSER=chrome pytest -q
- HEADLESS=true pytest -q

Check conftest.py and any runner scripts for the exact flags used by this framework.

## Project structure (typical)

- src/ or package/ - shared framework code (utilities, page objects)
- pages/ - Page Object Model classes for application pages
- tests/ - pytest test modules
- resources/ - test data, configuration, fixture data
- drivers/ - optional pre-bundled browser drivers
- conftest.py - pytest fixtures and session configuration
- requirements.txt - Python dependencies
- README.md - this file

Adjust the above to match the exact directories in this repo; the pattern follows common Sauce Demo frameworks.

## Writing tests

- Use page objects to interact with UI elements.
- Keep assertions in tests, interactions inside page objects.
- Use fixtures (login, browser setup/teardown) from conftest.py to reduce duplication.
- Tag tests with pytest markers (smoke, regression) when appropriate.

## CI and reporting

- Integrate pytest commands into your CI pipeline (GitHub Actions, Azure Pipelines, etc.).
- Produce HTML or Allure reports in CI for visibility.
- Ensure browsers/drivers are available on CI runners or use a Selenium grid / cloud provider.

## Contributing

- Run tests locally before submitting PRs.
- Follow existing code style and add tests for new features.
- Keep changes small and focused.

## Further notes

Refer to the repository's conftest.py, tests and page objects to discover actual flags, markers and configuration used by this project — update this README if the repo uses custom conventions.
