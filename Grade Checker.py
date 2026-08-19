def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


def main():
    total_subjects = 5
    all_marks = []

    for i in range(total_subjects):
        marks = int(input(f"Subject {i+1} ke marks: "))
        all_marks.append(marks)
        grade = calculate_grade(marks)
        print(f"Subject {i+1} Grade: {grade}")

    total = sum(all_marks)
    percentage = total / total_subjects
    final_grade = calculate_grade(percentage)

    print(f"\nTotal Marks: {total}")
    print(f"Overall Percentage: {percentage}%")
    print(f"Final Grade: {final_grade}")


main()