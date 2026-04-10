# Quickstart Guide: Basic Calculator Core Logic (Tests)

This guide provides instructions on how to set up the project and run the tests for the core calculator logic.

---

## 1. Prerequisites

- Python 3.12 or newer.

## 2. Setup

1.  Navigate to the project's root directory.
2.  Ensure you have the core `calculator.py` and `test_calculator.py` files in your project.

## 3. Running Tests

To verify the core calculation logic:

1.  Open your terminal or command prompt.
2.  Navigate to the directory containing `test_calculator.py`.
3.  Run the tests using Python's `unittest` module:

    ```bash
    python -m unittest test_calculator.py
    ```

    Alternatively, if you are in the project root:

    ```bash
    python -m unittest specs/001-basic-calculator/test_calculator.py
    ```

    (Note: The exact path to `test_calculator.py` might vary depending on how the files are organized after implementation.)

## 4. Core Functionality

The core logic provides functions such as:
- `parse_expression(expression: str) -> Tuple[float, str, float]`
- `calculate(operand1: float, operator: str, operand2: float) -> float`

These functions are designed to be integrated into other applications. There is no direct command-line interface provided at this stage.
