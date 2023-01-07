
def create_student_file():
    file = open("students.txt", "w+")
    lines = ["123,Sara,512345,4\n", "456,Ahmed,601200,3\n"]
    file.writelines(lines)
    file.close()


def create_course_file():
    file = open("courses.txt", "w+")
    lines = ["CMPS151,Programming Concepts,3\n",
             "CMPS303,Data Structures,4\n",
             "CMPS251,Object oritebd,4\n"]
    file.writelines(lines)
    file.close()


def create_grade_file():
    file = open("grades.txt", "w+")
    lines = ["123,CMPS151,A\n", "456,CMPS151,B\n"]
    file.writelines(lines)
    file.close()


def get_data_file(file_name):
    file = open(file_name, "r")
    file_content = file.readlines()
    file.close()
    file_content = [line.strip("\n").split(",") for line in file_content]
    return file_content


def add_student():
    adding = True
    print(f"Your choice: 1")
    file_content = get_data_file("students.txt")
    student_id = input("Enter student ID:")
    studen_name = input("Enter student name:")
    studen_mobile = input("Enter student mobile:")

    for line in file_content:
        if student_id == line[0]:
            adding = False
            print("ERROR: this id already exist")
    if adding:
        write_file = open("students.txt", "a")
        write_file.write(f"{student_id},{studen_name},{studen_mobile} \n")
        write_file.close()
        print("Student is added")


def add_course():
    adding = True
    print(f"Your choice: 2")
    file_content = get_data_file("courses.txt")
    course_number = input("Enter course number:")
    course_name = input("Enter course name:")
    credits = input("Enter course credits:")

    for line in file_content:
        if course_number == line[0]:
            adding = False
            print("ERROR: this course already exist")
    if adding:
        write_file = open("courses.txt", "a")
        write_file.write(f"{course_number},{course_name},{credits} \n")
        write_file.close()
        print("Course is added")


def check_if_student_exist_and_return(student_id):
    student_file_content = get_data_file("students.txt")
    student_exist = False
    for line in student_file_content:
        if student_id == line[0]:
            student_exist = True
            student_name = line[1]
    if not student_exist:
        print("There is no student with this ID")
        return None
    else:
        print(f"Student name : {student_name}")
    return line


def check_if_course_exist_and_return(course_number):
    course_file_content = get_data_file("courses.txt")

    course_exist = False

    for line in course_file_content:
        if course_number == line[0]:
            course_exist = True
            course_name = line[1]
    if not course_exist:
        print("There is no course with this number")
        return None
    else:
        print(f"course name : {course_name}")
    return course_number


def get_gpa_and_add(grade_list, course_credits, student_id):
    result = 0
    for i in range(len(grade_list)):
        result += int(grade_list[i]) * int(course_credits[i])
    gpa = int(result) / sum(course_credits)
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()
    for i, line in enumerate(lines):
        if line[0] == student_id:
            lines[i] = str(",".join(line[i])) + ","+str(gpa)
    file = open("students.txt", "w")
    file.writelines(lines)
    file.close()

    return gpa


def add_grade_interface():
    student_id = input("Enter student ID:")
    _ = check_if_student_exist_and_return(student_id)
    course_number = input("Enter course No:")

    _ = check_if_course_exist_and_return(course_number)
    grade = input("Enter student grade:")
    while grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid input!")
        grade = input("Enter student grade:")

    file = open("grades.txt", "w")
    file.write(f"{student_id},{course_number},{grade} \n")
    file.close()


def get_student_courses(student_id):
    courses_grades = []
    grades_symbols = ["F", "D", "C", "B", "A"]
    grades = get_data_file("grades.txt")
    for grade in grades:
        if student_id == grade[0]:
            courses_grades.append(
                [grade[1], grades_symbols.index(grade[2].strip())])
    courses = get_data_file("courses.txt")
    course_named_grades = []
    for courses_grade in courses_grades:
        for course in courses:
            if courses_grade[0] == course[0]:

                course_named_grades.append(
                    [*courses_grade, course[1], int(course[2])])
    return course_named_grades


def print_student_info():
    student_id = input("Enter student ID:")

    grades_symbols = ["F", "D", "C", "B", "A"]
    student_data = check_if_student_exist_and_return(student_id)
    if student_data:

        course_named_grades = get_student_courses(student_id)
        course_numbers_list = [course_named_grade[0]
                               for course_named_grade in course_named_grades]
        grade_list = [course_named_grade[1]
                      for course_named_grade in course_named_grades]
        course_names_list = [course_named_grade[2]
                             for course_named_grade in course_named_grades]
        course_credits_list = [course_named_grade[3]
                               for course_named_grade in course_named_grades]
        print(
            f"GPA: {get_gpa_and_add(grade_list, course_credits_list, student_id)}")
        for i in range(len(course_credits_list)):
            print(
                f"{course_numbers_list[i]} {course_names_list[i]} {grades_symbols[grade_list[i]]} \n")


def main():

    menu = """
    Please select one of the following:
    1- Add a new student 
    2- add a new course
    3- add a new gradekz
    4- Print a student's transcript
    5- Exit
    Your choice:
    """
    create_student_file()
    create_course_file()
    create_grade_file()
    while True:
        choice = int(input(menu))
        if choice == 1:
            add_student()
        elif choice == 2:
            add_course()
        elif choice == 3:
            add_grade_interface()
        elif choice == 4:
            print_student_info()
        elif choice == 5:
            exit()


main()
