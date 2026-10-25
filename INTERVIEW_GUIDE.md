# Browser Automation Project: Interview Guide

## 1. Project summary

This repository is a Python browser-automation portfolio for checking the Microsoft Teams sign-in experience. It demonstrates three complementary test layers:

- **HTTP check:** `requests` checks that the public sign-in page responds with successful HTML.
- **Browser automation:** Playwright and Selenium interact with the sign-in page and Teams navigation using browser-visible controls.
- **Readable acceptance tests:** Gherkin BDD examples and a Robot Framework smoke test express behavior in Given–When–Then form.

GitHub Actions runs a credential-free Playwright public-page check. Jenkins runs a credential-free Robot Framework/Selenium public-page check on a Windows Chrome agent. The interactive account sign-in examples are separate and need credentials; the pipelines do not sign in to a user account.

## 2. Concepts to explain

### Browser automation and end-to-end testing

Browser automation drives a real browser to exercise a user-visible workflow. An end-to-end (E2E) test can cover multiple layers at once: page rendering, browser behavior, and interaction with a remote service. That makes it valuable for confidence in a user journey, but usually slower and more sensitive to network, authentication, and UI changes than unit tests.

**In this project:** Playwright and Selenium open the Teams sign-in entry point, interact with controls, and check navigation elements. The public-page CI check avoids account credentials and MFA.

### Playwright and Selenium

Both are browser automation tools. Playwright provides browser contexts, pages, role/label-based locators, and auto-waiting assertions. Selenium WebDriver controls browsers through the WebDriver interface and offers explicit waits through `WebDriverWait` and expected conditions. The project demonstrates both approaches against the same general application.

**Trade-off:** Playwright's locator and assertion model can reduce synchronization boilerplate. Selenium is broadly supported and common in existing test stacks. Either tool still needs resilient locators, good waits, isolation, and meaningful assertions.

### Page Object Model (POM)

POM keeps page-specific locators and interactions behind a page class. Tests then call meaningful operations instead of repeating selectors and low-level browser commands. This improves reuse and makes UI changes easier to localize.

**In this project:** `TeamsSign` contains browser actions, while `TeamsSignLocators` holds selectors. A useful improvement to discuss: keep assertions about expected outcomes in tests where practical, and keep page methods focused on page behavior rather than long fixed sequences.

### Locators and accessibility semantics

A locator identifies an element to interact with. Text, role, accessible name, and label selectors describe user-facing semantics and are often more robust than deeply nested CSS/XPath paths. Stable test IDs can be useful when user-facing semantics are unavailable. Locators should be specific enough to avoid selecting the wrong matching element.

**In this project:** Playwright uses `get_by_role` and placeholders in login flows, alongside CSS locators; Selenium uses ID, CSS, and XPath strategies. The Selenium locator module centralizes them.

### Synchronization: explicit waits vs fixed sleeps

Modern sites render asynchronously. A test should wait for the condition it needs—such as an element becoming visible or clickable—instead of assuming a fixed amount of time will be enough. Fixed sleeps make tests slower when the app is fast and flaky when it is slower than expected. Use an overall timeout and report which expected condition failed.

**In this project:** both browser implementations use explicit waits in places, but also contain long `time.sleep()` calls. That is a clear improvement area: replace sleeps with waits for the next meaningful page state, and remove redundant waits.

### Assertions and test oracles

An assertion is the test's pass/fail criterion; the expected result is the test oracle. A test that only clicks through a flow can pass even when the application is wrong. Assert observable outcomes such as a destination heading, a visible navigation item, or a response status and content type.

**In this project:** the HTTP check asserts status, HTML content type, and expected page text. Playwright tests assert that navigation controls are visible. The Selenium pytest script mainly performs actions and prints a success message, so adding outcome assertions would make its result stronger.

### pytest fixtures and lifecycle

Fixtures provide dependencies and manage setup/teardown. Fixture scope controls how often setup runs: function scope gives each test fresh state; session scope shares state for the whole run. `yield` fixtures can clean up after tests even when execution fails.

**In this project:** Playwright defines a session-scoped credential fixture and a session-scoped `teams` fixture that starts the browser and closes it after the suite. Shared authenticated browser state is faster, but can cause order dependence and shared state between tests. Per-test contexts or function-scoped fixtures improve isolation when reliability matters.

### BDD and Gherkin

Behavior-Driven Development (BDD) describes system behavior using domain-readable scenarios. Gherkin uses `Given` for context, `When` for an action, and `Then` for an observable outcome. Step definitions connect those phrases to executable code. BDD works best when examples communicate behavior to product, QA, and engineering—not when they merely restate implementation details.

**In this project:** there are examples using Behave, pytest-bdd, Radish, and Cucumber-style Gherkin executed by Behave. Robot Framework also uses keyword-driven Given–When–Then steps. These are examples of alternative runners/styles, not evidence that every framework is required in one production suite.

### HTTP/API-level checks vs UI checks

An HTTP check verifies a server response directly without opening a browser. It is usually faster and more focused than a UI check, but cannot prove that a browser rendered the page or that controls work. UI tests validate a more realistic interaction path but cost more to run and maintain. A balanced test strategy uses the lowest layer that can prove each requirement, with a smaller number of high-value browser journeys.

**In this project:** `requests` verifies the public page's response; Playwright and Selenium verify browser-level behavior. The `api` folder is an HTTP page check, not a test of a Teams JSON API.

### Credentials and secrets

Credentials should not be committed to source control. They can be supplied via protected CI secret storage or local environment configuration. Avoid printing secrets, and use masked input for interactive password prompts. Tests involving real account authentication may also encounter MFA, consent screens, rate limits, and policy changes; these make them less suitable for routine public CI.

**In this project:** interactive Playwright flows read `TEAMS_EMAIL` and `TEAMS_PASSWORD` from environment variables or a local `.env`, with prompts as a fallback. Keep `.env` out of version control and use CI secrets only if a secure authenticated CI run is deliberately configured.

### Continuous Integration (CI)

CI runs checks automatically on changes so failures are found before integration. A pipeline typically checks out code, sets up the runtime, installs dependencies/browser binaries, runs tests, and retains reports. Reproducibility comes from pinned/runtime-controlled dependencies, explicit browser setup, and consistent configuration.

**In this project:** GitHub Actions runs the public Playwright check on pushes and pull requests to `main`; Jenkins runs the public Robot Framework check on a configured Windows Chrome agent and archives its output. They validate the public entry point, not authenticated account workflows.

## 3. A concise interview pitch

> “I built a Python browser-automation project around the Microsoft Teams public sign-in experience. It combines a lightweight `requests` smoke check with browser checks implemented in Playwright and Selenium, and includes readable BDD examples using Gherkin plus a Robot Framework smoke test. I used page objects to centralize UI interactions and locators, pytest fixtures for browser lifecycle and credentials, and explicit waits for asynchronous UI behavior. GitHub Actions and Jenkins run credential-free checks of the public sign-in page. The main improvements I would make next are replacing fixed sleeps with state-based waits, strengthening outcome assertions, and isolating browser state per test.”

## 4. Likely interview questions and answer points

1. **Why use both API-level and UI tests?**  HTTP checks are quick and isolate reachability/content; browser tests cover rendering and interaction. Use each at the lowest layer that proves the requirement.
2. **How do you reduce flaky browser tests?**  Prefer stable semantic locators, wait for specific conditions, isolate test state, control test data, keep assertions observable, and capture useful logs/screenshots on failure.
3. **Why use a page object?**  It encapsulates selectors and page behavior, reduces duplication, and limits the effect of UI changes. Avoid making it a giant class that hides the test's purpose.
4. **What is the risk of a session-scoped browser fixture?**  It saves startup time, but tests can share cookies and UI state or depend on execution order. Choose scope based on the required isolation; use separate contexts when tests must be independent.
5. **What is the difference between an explicit wait and `sleep`?**  An explicit wait polls for a condition and proceeds as soon as it is met; `sleep` always waits a fixed duration and does not establish that the page is ready.
6. **What makes a good locator?**  It is unique, stable, readable, and tied to a user-visible role/name or a deliberately maintained test ID rather than fragile layout structure.
7. **What does Given–When–Then mean?**  Given establishes context, When performs the behavior, and Then checks its observable result. Gherkin is the scenario language; a runner and step definitions execute it.
8. **How do you handle secrets in automation?**  Never commit credentials; use environment variables locally and protected secret storage in CI; mask prompts and logs; avoid authenticated CI unless the account and MFA flow are intentionally supported.
9. **What does the current CI prove?**  It proves the public sign-in page can be reached and checked using the configured browser/test stack. It does not prove that a user can authenticate or that all Teams features work.
10. **What would you improve first?**  Replace long fixed sleeps with waits for precise states, strengthen Selenium assertions, and avoid sharing mutable authenticated state across unrelated tests.

## 5. Be precise about project claims

- The repository contains multiple frameworks as learning/comparison examples; do not imply they are all part of one production-grade suite.
- CI runs credential-free public-page checks. The interactive login paths need a real account and may involve MFA.
- The `api` check uses HTTP requests against a web page; it does not call a documented Teams service API.
- Some browser scripts use long fixed sleeps and session-shared browser state. Describe these as current limitations and explain how you would improve them.
- The Playwright fixture navigates across Teams sections; review the specific test and current behavior before claiming exactly which actions are covered.

## 6. Terms at a glance

| Term | Plain-language meaning |
|---|---|
| E2E test | Checks a user journey across multiple parts of a system |
| POM | Organizes page selectors and actions into page-specific classes |
| Locator | A rule for finding an element in a page |
| Explicit wait | Waits until a particular condition becomes true |
| Fixture | Reusable test setup/cleanup or a supplied test dependency |
| BDD | Describes behavior with examples understandable to stakeholders |
| Gherkin | Given–When–Then syntax for writing scenarios |
| Smoke test | A small, fast check that a key path is basically available |
| CI | Automated checks that run when code changes |
| Flaky test | A test whose result varies despite no relevant code change |
