def if_prime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def first_n_prime(n):
  result = []
  num = 2
  while len(result) < n:
    if if_prime(num):
      result.append(num)
    num += 1
  return result

print(first_n_prime(10))
   