def perform_operation(num1: float, num2: float, operation: str):
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'DIVISION_BY_ZERO'
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")

print(perform_operation(5,6, 'add'))
