def gcd(a,b):
    result = min(a,b)
    while result:
        if a% result == 0 and b % result == 0:
            break
        result -=1
    return result
print(gcd(48,18))