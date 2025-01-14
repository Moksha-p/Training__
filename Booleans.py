# Count the number of True values in a list
def count_true(lst):
    return lst.count(True)

print(count_true([True, False, True, True, False, True, False]))  


# Evaluate a complex Boolean expression represented as a string
def evaluate_expression(expr):
    return eval(expr)

print(evaluate_expression("True and False or True"))  
