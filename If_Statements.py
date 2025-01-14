
# Classify a given year as a leap year or a non-leap year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Non-Leap Year"

print(leap_year(2025))  

# Solve a quadratic equation and classify the roots
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f"Real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Equal roots: {root}"
    else:
        return "Complex roots"

print(solve_quadratic(1, -3, 2))  

