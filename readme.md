# Automated Test Suite with Python and Playwright

This repository contains an automated test suite built using Python and Playwright, utilizing Pytest and Allure for reporting. The test suite supports both Windows and Linux operating systems.

## Prerequisites

Before running the tests, ensure that you have the following installed on your machine:

- Python 3.8+ (recommended)
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Installation

### 1. Set up Virtual Environment (venv)

#### Windows:

Open the Command Prompt (CMD) or PowerShell. 
Navigate to your project directory.
Create a virtual environment:

    python -m venv venv

Activate the virtual environment:
For CMD:

    venv\Scripts\activate

For PowerShell:

    .\venv\Scripts\Activate.ps1

#### Linux:

Open a terminal.
Navigate to your project directory.
Create a virtual environment:

    python3 -m venv venv

Activate the virtual environment:

    source venv/bin/activate

### 2. Install Dependencies

With the virtual environment activated, install the necessary dependencies by running the following command:

    pip install -r requirements.txt

This will install all the required packages for the project, including Playwright, Pytest, and Allure.

### 3. Install Playwright Browsers

After installing the dependencies, you need to install the browsers required for Playwright. Run the following command:

    python -m playwright install

This will download and install the necessary browser binaries (Chromium, Firefox, and WebKit).

To run the tests, simply use the following Pytest command:

    pytest

This will automatically discover and execute all test files in the project.


### 4. Generate the Allure Report:

Once Allure is installed, you can generate the report by running:

    allure serve ./allure

This will generate an interactive Allure report in your browser.

Windows:

To serve the Allure report on Windows, ensure that the allure command is accessible by adding it to your system's PATH, or run it directly from the Allure installation folder.