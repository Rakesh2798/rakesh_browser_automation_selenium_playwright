# Selenium-TeamsMeetingAutomation

This project automates Microsoft Teams interactions using Selenium WebDriver. It is structured based on the Page Object Model (POM) design pattern for maintainability and scalability.

## Project Structure

- `pages/`: Contains the Page Object classes and locators.
  - `locators.py`: Centralized file containing all web element locators (XPath, CSS Selectors, ID).
  - `teams_page.py`: Contains the `TeamsSign` class which implements the interaction logic (e.g., login, click chat, meet) for the Microsoft Teams interface.
- `tests/`: Contains test execution scripts.
  - `test_teams.py`: The main test runner script that executes a sequence of automated Teams interactions.

## Prerequisites

- Python 3.x
- Selenium
- Google Chrome browser

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have the necessary dependencies installed. You can install Selenium using `pip`:

   ```bash
   pip install selenium
   ```

## Running the Tests

To run the automated Microsoft Teams test, execute the following command from the project root directory:

```bash
python tests/test_teams.py
```

When started, the script will prompt you for your Microsoft Teams email ID and password before launching the browser. Password entry is masked in the terminal for security.