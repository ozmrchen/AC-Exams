def get_grade(score):
    """
    Convert a numerical score to a letter grade.
    Uses match/case to determine the grade.
    """
    match score:
        case score if score >= 90:
            return "A+"
        case score if score >= 80:
            return "A"
        case score if score >= 75:
            return "B+"
        case score if score >= 70:
            return "B"
        case score if score >= 65:
            return "C+"
        case score if score >= 60:
            return "C"
        case score if score >= 55:
            return "D+"
        case score if score >= 50:
            return "D"
        case score if score >= 45:
            return "E+"
        case score if score >= 40:
            return "E"
        case _:
            return "UG"

# Show grade boundaries
print("=== Grade Boundaries ===")
print("A+ : 90 or above")
print("A  : 80-89")
print("B+ : 75-79")
print("B  : 70-74")
print("C+ : 65-69")
print("C  : 60-64")
print("D+ : 55-59")
print("D  : 50-54")
print("E+ : 45-49")
print("E  : 40-44")
print("UG : below 40")

# Demonstrateion
score = float(input("Enter your score (0-100): "))
grade = get_grade(score)
print(f"Score: {score:3.2f} → Grade: {grade}")
