
subjects = int(input("Enter number of subjects: "))

totalMarks = 0
maxMarks = subjects * 100
failed = False

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for subject {i} (0-100): "))
    
    if marks < 40:
        failed = True
    
    totalMarks += marks

percentage = (totalMarks / maxMarks) * 100

if failed:
    grade = "F"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print(f"Total Marks: {totalMarks}/{maxMarks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print("Result: Pass" if grade != "F" else "Result: Fail")
