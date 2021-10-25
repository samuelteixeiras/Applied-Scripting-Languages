
mark = int(input("Enter the overall mark: "))

if mark > 100 or mark < 0:
    print("Invalid input")
elif  mark >=70:
    print("First Class Honours")
elif 50 <=  mark <= 69:
    print("Second Class Honours")
elif 40 <=  mark <= 49:
    print("Pass")
else:
    print("No award")