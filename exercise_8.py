year=int(input('enter the year:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("the entered year is leap year.")
        else:
            print("the entered year is not leap year.")
    else:
        print("the entered year is leap year.")
else:
    print("the entered year is not leap year")