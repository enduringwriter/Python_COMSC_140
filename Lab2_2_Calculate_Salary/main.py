def main():
    """
    Calculates and display an employee’s total wages for the week.
    Input is the employee's work hours for the week.
    The regular hours for the work week are 40 and any hours worked over 40 are considered overtime.
    The employee earns $18.25 per hour for regular hours and $27.78 per hour for overtime hours.
    """
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

    overtime = workhours - reg_hours
    overtime_wage = overtime * ov_rate
    regular_wage = reg_hours * reg_rate
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
