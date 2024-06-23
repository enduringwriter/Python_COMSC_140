def main():
    """
    Assign a letter grade to a score.
    """

    score = int(input('Enter your input: '))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f'Score: {score} \t Grade: {grade}')

    ########################################
    # Do not delete the return statement
    ########################################
    return grade

if __name__ == '__main__':
    main()