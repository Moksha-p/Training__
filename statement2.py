import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Equal roots: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Complex roots: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"

# Test case
print(solve_quadratic(1, -3, 2))  # Output: Real roots: 2.0, 1.0
