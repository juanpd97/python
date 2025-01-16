def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100 != 0:
            break

        leep = true
    
    return leap

year = int(input())
print(is_leap(year))