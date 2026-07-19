# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 95

if score < 60:
    print("F grade")
elif score < 70:
    print("D grade")
elif score < 80:
    print("C grade")
elif score < 90:
    print("B grade")
else:
    print("A grade")
