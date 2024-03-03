a = float(input("Enter a number of units:"))
if(a <= 100 ):
    print(f"Your total electricity bill for {a} units is Rs.{a * 0}")
elif(a > 100 and a < 200):
    print(f"Your total electricity bill for {a} units is Rs.{a * 5}" )
else:
    print(f"Your total electricity bill for {a} units is Rs.{a * 10}")
    