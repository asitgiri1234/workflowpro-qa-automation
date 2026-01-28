# WorkFlow Pro – QA Automation Case Study

This repository contains a QA automation case study for "WorkFlow Pro", a multi-tenant B2B SaaS project management platform. The purpose of this project is to demonstrate test automation design, framework structure, and testing strategy across UI, API, and mobile platforms.

The repository focuses on testing mindset, scalability, and real-world automation challenges rather than fully executable test coverage.

---

## Assignment Coverage Mapping

This repository addresses all parts of the QA automation case study as follows:

- Part 1: Debugging Flaky Tests  
  Implemented and documented in `docs/flaky-test-analysis.md`, including root cause analysis and improved Playwright test examples.

- Part 2: Test Framework Design  
  Covered in `docs/framework-design.md` and `docs/assumptions.md`, along with the implemented project structure.

- Part 3: API + UI + Mobile Integration Test  
  Implemented in `tests/integration/test_project_creation_flow.py`, supported by API, UI, and mobile test modules.

This structure ensures clear separation of concerns while demonstrating real-world QA automation practices.

## Scope of Testing

The automation approach in this repository covers:

- Web UI testing using Playwright
- API testing using pytest and requests
- End-to-end integration testing across API, Web UI, and Mobile
- Multi-tenant validation and tenant isolation checks
- Role-based access considerations (Admin, Manager, Employee)
- Cross-browser and cross-device testing concepts
- CI/CD and BrowserStack integration strategy
- The focus is on critical business flows rather than exhaustive UI coverage.

---

## Tech Stack

- Programming Language: Python
- Test Framework: pytest
- UI Automation: Playwright
- API Testing: requests
- Mobile Testing: BrowserStack (conceptual integration)
- Reporting: pytest-html
- CI/CD: Designed for pipeline execution (GitHub Actions / similar)

---

## Project Structure Overview

- `docs/`  
  Contains documentation explaining testing decisions, framework design, and analysis of flaky tests.

- `tests/`  
  Holds UI, API, mobile, and integration test scripts.

- `framework/`  
  Contains base classes and shared automation logic to support scalability and reuse.

- `utils/`  
  Utility modules for configuration management, authentication handling, and test data creation.

- `test_data/`  
  Sample test data for users and tenant configurations.

- `reports/`  
  Sample test execution reports and reporting artifacts.

---

## Test Execution (Conceptual)

1. Install dependencies:

pip install -r requirements.txt
playwright install

2. Execute tests:

3. Generate reports:

Note: The tests are designed to demonstrate structure and strategy. Some external integrations (2FA, BrowserStack, real tenants) are assumed or mocked.

---

## BrowserStack Integration (Conceptual)

- Web and mobile tests are designed to be executed on BrowserStack for cross-browser and cross-device coverage.
- Browser and device configurations are expected to be injected via environment variables.
- Parallel execution is supported to optimize execution time and cost.

---

## Assumptions and Limitations

- Authentication tokens and credentials are mocked or provided via environment variables.
- 2FA flows are assumed to be handled externally or bypassed in test environments.
- Test data cleanup is assumed to be handled via backend jobs or API hooks.
- This repository prioritizes clarity and structure over full execution readiness.

Detailed assumptions are documented in `docs/assumptions.md`.

---

## Purpose of This Repository

This repository is intended as a QA automation case study to demonstrate:
- Structured test automation thinking
- Handling of multi-tenant SaaS complexities
- Integration of API, UI, and mobile testing
- Maintainable and scalable automation design

It is not intended for production deployment.

