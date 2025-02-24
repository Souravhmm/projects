class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def apply_operation(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b  # Use // for integer division
    return 0


def evaluate_expression(expression):
    # Remove all whitespace from the expression
    expression = expression.replace(" ", "")

    # Initialize stacks
    numbers = Stack()
    operators = Stack()

    i = 0
    while i < len(expression):
        if expression[i] == '(':
            operators.push(expression[i])
            i += 1
        elif expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            numbers.push(num)
        elif expression[i] == ')':
            while not operators.is_empty() and operators.peek() != '(':
                b = numbers.pop()
                a = numbers.pop()
                op = operators.pop()
                numbers.push(apply_operation(a, b, op))
            operators.pop()  # Remove the '(' from the stack
            i += 1
        else:
            # Current token is an operator
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(expression[i])):
                b = numbers.pop()
                a = numbers.pop()
                op = operators.pop()
                numbers.push(apply_operation(a, b, op))
            operators.push(expression[i])
            i += 1

    # Evaluate remaining operations
    while not operators.is_empty():
        b = numbers.pop()
        a = numbers.pop()
        op = operators.pop()
        numbers.push(apply_operation(a, b, op))

    return numbers.pop()


# Example usage
if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    result = evaluate_expression(expression)
    print("Result:", result)