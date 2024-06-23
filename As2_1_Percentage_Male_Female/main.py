def main():
    """
    This program calculates and displays the total number of students and the percentages of males and females.
    The user will input the number of males and females.
    """
    
    count_males = int(input('Enter the number of male students: '))
    count_females = int(input('Enter the number of female students: '))
    count_non_binary = int(input('Enter the number of non-binary students: '))
    
    total_students = count_males + count_females + count_non_binary
    
    m_perc = count_males/total_students * 100
    f_perc = count_females/total_students * 100
    nb_perc = count_non_binary/total_students * 100

    print(f'The percentage of males, females and non-binary \t {m_perc: .2f}% \t {f_perc: .2f}% \t {nb_perc: .2f}%')
    return m_perc, f_perc, nb_perc


if __name__ == '__main__':
    main()