# Examples of using the conditional functions in practical scenarios

from conditional_functions import match_condition, switch_case

def grade_student(score):
    """Grade a student based on their score using match_condition"""
    return match_condition([
        (lambda: score >= 90, lambda: "A"),
        (lambda: score >= 80, lambda: "B"),
        (lambda: score >= 70, lambda: "C"),
        (lambda: score >= 60, lambda: "D"),
        (lambda: score < 60, lambda: "F")
    ])

def describe_day(day_of_week):
    """Describe a day of the week using switch_case"""
    return switch_case(
        day_of_week,
        {
            "Monday": lambda: "Start of the work week",
            "Tuesday": lambda: "Second day of the work week",
            "Wednesday": lambda: "Midweek day",
            "Thursday": lambda: "Almost Friday",
            "Friday": lambda: "Last day of the work week",
            "Saturday": lambda: "Weekend - time to relax",
            "Sunday": lambda: "Weekend - prepare for Monday"
        },
        default=lambda: "Invalid day"
    )

def categorize_age(age):
    """Categorize a person based on their age using match_condition"""
    return match_condition([
        (lambda: age < 0, lambda: "Invalid age"),
        (lambda: age <= 2, lambda: "Infant"),
        (lambda: age <= 12, lambda: "Child"),
        (lambda: age <= 19, lambda: "Teenager"),
        (lambda: age <= 59, lambda: "Adult"),
        (lambda: age >= 60, lambda: "Senior")
    ])

# Example usage
if __name__ == "__main__":
    # Grade student example
    student_score = 85
    grade = grade_student(student_score)
    print(f"Student with score {student_score} receives grade: {grade}")
    
    # Describe day example
    today = "Wednesday"
    description = describe_day(today)
    print(f"{today} is: {description}")
    
    # Categorize age example
    person_age = 25
    age_category = categorize_age(person_age)
    print(f"A person aged {person_age} is categorized as: {age_category}")