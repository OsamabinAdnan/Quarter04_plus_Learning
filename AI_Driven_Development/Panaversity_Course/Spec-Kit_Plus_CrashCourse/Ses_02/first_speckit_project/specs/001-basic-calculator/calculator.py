def calculate(operand1: float, operator: str, operand2: float) -> float:
    """Performs a calculation based on two operands and an operator."""
    result = 0.0
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero is not allowed.")
        result = operand1 / operand2
    
    return round(result, 4)

def parse_expression(expression: str) -> tuple[float, str, float]:
    """
    Parses a simple arithmetic expression string into its components.
    Expected format: "operand1 operator operand2"
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Invalid expression format. Expected 'operand1 operator operand2'.")
    
    operand1 = float(parts[0])
    operator = parts[1]
    operand2 = float(parts[2])
    
    return (operand1, operator, operand2)
