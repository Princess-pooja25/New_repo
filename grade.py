marks = int(input("Enter student marks: "))
print("This program is used to calculate grades.")
if marks >= 95:
    print("Grade: A+")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
