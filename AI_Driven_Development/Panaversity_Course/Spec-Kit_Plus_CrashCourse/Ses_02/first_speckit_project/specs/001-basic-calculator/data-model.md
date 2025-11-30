# Data Model: Basic CLI Calculator

This document describes the data structures used within the application. Given the stateless nature of the calculator, there is no persistent data model.

---

## 1. Core Data Structure

The application's logic revolves around a conceptual `Calculation` entity, which is represented as a transient data structure during runtime.

### `Calculation`

This structure holds the components of a single arithmetic expression provided by the user.

| Field | Type | Description | Rules |
| :--- | :--- | :--- | :--- |
| `operand1` | `float` | The first number in the expression. | Must be a valid floating-point number. |
| `operator` | `str` | The arithmetic operator. | Must be one of `+`, `-`, `*`, `/`. |
| `operand2` | `float` | The second number in the expression. | Must be a valid floating-point number. Cannot be `0` if the operator is `/`. |

## 2. State

The application has no persistent state. Each calculation is an independent, ephemeral transaction.
