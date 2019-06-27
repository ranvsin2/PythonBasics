a=float(input("Enter 1st side :"))
b=float(input("Enter 2nd Side :"))
c=float(input("Enter 3rd side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The Area of triangle with 3 side is %0.2f"%area)