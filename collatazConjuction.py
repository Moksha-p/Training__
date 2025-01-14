def collataz(a):
        if a <= 0:
            print("Enter Positive Integer")
        sq = [a]
        while a != 1 :
            if a % 2 == 0:
              a //= 2 
            else :
                a = (a * 3) + 1
            sq.append(a)
        return sq
print(collataz(13))
        