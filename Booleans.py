# Create a program that evaluates a list of Boolean expressions and returns the count of True values.

def count_true_values(boolean_list):
    return boolean_list.count(True)

# Example Test Case
input_list = [True, False, True, True, False]
output = count_true_values(input_list)
print("Expected Output:", 3)
print("Returned Output:", output)


# Write a Python function to evaluate a complex Boolean expression represented as a string

def evaluate_boolean_expression(expression):
    return eval(expression)

# Example Test Case
input_expression = "True and False or True"
output = evaluate_boolean_expression(input_expression)
print("Expected Output:", True)
print("Returned Output:", output)
