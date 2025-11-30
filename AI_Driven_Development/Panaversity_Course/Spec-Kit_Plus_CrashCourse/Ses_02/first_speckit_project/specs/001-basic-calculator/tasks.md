# Actionable Tasks: Basic Calculator Core Logic

This document breaks down the implementation of the **Basic Calculator Core Logic** feature into actionable, dependency-ordered tasks.

---

## Implementation Strategy

We will follow a strict Test-Driven Development (TDD) approach. Each phase is designed to be a small, verifiable step. The core logic will be developed first, driven by tests, ensuring correctness and robustness before any user interface is considered.

**MVP Scope:** The Minimum Viable Product for this feature is the completion of all tasks listed below, resulting in fully tested `calculate` and `parse_expression` functions.

---

## Phase 1: Project Setup

**Goal:** Create the necessary files and set up the development environment for the project.

- [x] `T001` Create and activate a `uv` virtual environment for the project.
- [x] `T002` Create the core logic file `calculator.py`.
- [x] `T003` Create the test file `test_calculator.py` and add necessary imports (`unittest`, and the `calculator` module).

---

## Phase 2: Core Calculation Function (US1)

**Goal:** Implement a `calculate` function that correctly performs all four basic arithmetic operations and handles rounding.

**Independent Test Criteria:** The `calculate` function must pass all unit tests for addition, subtraction, multiplication, division, and rounding.

- [x] `T004` [US1] In `test_calculator.py`, write a new test class `TestCalculate`. Add a failing unit test for addition (e.g., `self.assertEqual(calculate(10, '+', 5), 15.0)`).
- [x] `T005` [US1] In `calculator.py`, define the `calculate` function and implement the addition logic to pass the test.
- [x] `T006` [P] [US1] In `test_calculator.py`, add failing unit tests for subtraction, multiplication, and standard division.
- [x] `T007` [P] [US1] In `calculator.py`, implement the logic for subtraction, multiplication, and division within the `calculate` function to pass the tests.
- [x] `T008` [P] [US1] In `test_calculator.py`, add a failing unit test for a division that requires rounding (e.g., `1 / 3` should result in `0.3333`).
- [x] `T009` [P] [US1] In `calculator.py`, implement the rounding logic in the `calculate` function to ensure all results are rounded to 4 decimal places.

---

## Phase 3: Expression Parsing Function (US2)

**Goal:** Implement a `parse_expression` function that can correctly process a valid input string.

**Independent Test Criteria:** The `parse_expression` function must pass unit tests for valid expressions, including those with extra whitespace.

- [x] `T010` [US2] In `test_calculator.py`, write a new test class `TestParseExpression`. Add a failing unit test to check for correct parsing of a simple, valid expression (e.g., `"10.5 * 5"` should return `(10.5, '*', 5.0)`).
- [x] `T011` [US2] In `calculator.py`, define the `parse_expression` function and implement logic to pass the simple parsing test.
- [x] `T012` [P] [US2] In `test_calculator.py`, add a failing unit test to verify that expressions with extra leading, trailing, or internal whitespace are parsed correctly.
- [x] `T013` [P] [US2] In `calculator.py`, improve the `parse_expression` function to correctly handle variable whitespace.

---

## Phase 4: Error & Exception Handling (US3)

**Goal:** Make the `calculate` and `parse_expression` functions robust by ensuring they raise appropriate exceptions for invalid inputs.

**Independent Test Criteria:** All unit tests for error conditions must pass, verifying that the correct exceptions are raised.

- [x] `T014` [US3] In `test_calculator.py`, add a unit test to `TestCalculate` that verifies a `ValueError` is raised when attempting to divide by zero, using `with self.assertRaises(ValueError):`.
- [x] `T015` [US3] In `calculator.py`, add a check within the `calculate` function to raise a `ValueError` if division by zero is attempted.
- [x] `T016` [P] [US3] In `test_calculator.py`, add failing unit tests to `TestParseExpression` to verify a `ValueError` is raised for:
    - Malformed expressions (e.g., `"5 * * 5"`)
    - Incomplete expressions (e.g., `"5 +"`)
    - Non-numeric input (e.g., `"a + 5"`)
    - Empty or whitespace-only strings.
- [x] `T017` [P] [US3] In `calculator.py`, add validation logic to the `parse_expression` function to detect all invalid input conditions and raise a `ValueError`.

---

## Phase 5: Finalization

**Goal:** Ensure the code meets quality standards.

- [x] `T018` Review all code in `calculator.py` and `test_calculator.py` to ensure it meets PEP 8 standards and has complete type hinting and docstrings.

---

## Dependencies & Parallel Execution

- **Dependencies:** `Phase 1` → `Phase 2` & `Phase 3` → `Phase 4` → `Phase 5`.
- **Parallel Execution:**
  - Within Phase 2, tasks `T006` and `T008` can be worked on in parallel.
  - Within Phase 3, tasks can be done sequentially.
  - Within Phase 4, tasks `T014` and `T016` can be worked on in parallel.
  - Overall, `Phase 2 (Core Calculation)` and `Phase 3 (Expression Parsing)` can be developed in parallel after `Phase 1` is complete.
