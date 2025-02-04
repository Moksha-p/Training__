def classify_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Non-Leap Year"

print(classify_year(2020))  # Output: "Leap Year"
