year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} : Leap Year")
else:
    print(f"{year} : Not a Leap Year")