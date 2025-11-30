# Research & Decisions: Basic CLI Calculator

This document records the key technical decisions made during the planning phase.

---

### Decision 1: Application Structure

- **Decision:** The application will be structured around a `main()` function containing a `while True` loop. This loop will handle user input, call processing functions, and print results. The entire application will be initiated by a standard `if __name__ == "__main__":` block.
- **Rationale:** This is the canonical, most widely understood, and robust pattern for structuring a simple, interactive command-line application in Python. It clearly separates the application's entry point and main loop from its core logic.
- **Alternatives Considered:**
    - A single top-level script without a `main` function: Rejected as it's less modular and makes testing and potential future reuse more difficult.
    - Recursive function calls for the loop: Rejected as it's not idiomatic for this use case and risks stack overflow on very high numbers of interactions.

### Decision 2: Expression Parsing Method

- **Decision:** Expressions will be parsed manually. The input string will be split, and the components will be individually validated and converted to their correct types (float, str).
- **Rationale:** For the feature's limited scope (`number operator number`), manual parsing is the safest, most transparent, and most performant option. It gives us full control over validation and error handling, directly addressing the clarified spec requirements. It also avoids the significant security risks associated with using `eval()`.
- **Alternatives Considered:**
    - **`eval()` function:** Rejected due to major security vulnerabilities. `eval()` can execute arbitrary code, and sanitizing input sufficiently to make it safe is complex and brittle.
    - **Regular Expressions:** Rejected as being overly complex for the current scope. While powerful, a regex to correctly validate and capture all valid/invalid states would be less readable and harder to maintain than a direct string-splitting approach.

### Decision 3: Code Modularity

- **Decision:** The core logic will be broken into at least three distinct functions:
    1.  `parse_expression(input_str: str) -> tuple`: Takes raw user input, returns a structured tuple `(operand1, operator, operand2)`.
    2.  `calculate(operand1: float, operator: str, operand2: float) -> float`: Takes parsed components, returns a result.
    3.  `main()`: Contains the application's primary run loop.
- **Rationale:** This separation of concerns is fundamental to Test-Driven Development (TDD). It allows each unit of logic (parsing, calculation, user interaction) to be tested independently, leading to more reliable code that is easier to debug and maintain.
- **Alternatives Considered:**
    - **A single monolithic function:** Rejected as it would be difficult to test, hard to read, and would violate the single-responsibility principle.
