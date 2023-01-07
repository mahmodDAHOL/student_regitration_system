# student_regitrayion_system

a registration system that tracks students’ records. The system keeps track of the following data:

• Student’s data: id, name, mobile, GPA.

• The courses that student finished: course no, course name, credits, and the grade in that
course.

When the program starts, it will display the following menu

Please select one of the following:
1- Add a new student

2- add a new course

3- add a new gradekz

4- Print a student's transcript

5- Exit

This menu will be displayed repeatedly after each task finished until the you selects option 5.
# Option 1
When you selects 1, the system asks for student’s data as follows:

Enter student ID:

Enter student name:

Enter student mobile:

The input data is saved to the file students.txt, the default GPA is 0.0 when a new student is added.

In this option, when you enters student’s ID, the system will ensure there is no student
already in the file with that ID.

# Option 2
When you select 2, the system asks for course’s data as following:

Enter course number:

Enter course name:

Enter course credits:

In this option, when you enters course number, the system should ensure there is no course
already in the system with that number. 

# Option 3
In this option, it is assumed that the student’s data and course data is already in the system. When
you selects 3, the system asks for a student id, if there is no student with that ID in the system,
it prints, “There is no student with this ID”.

If the student is already in the system, it displays his name and asks for the course number.

If the course number is not already in the system, it displays “There is no course with this number”. 

If both student and course already in the system, it asks for the grade (letter grade). The only
accepted grades are ‘A’, ‘B’, ‘C’, ‘D’, ‘F’. If you enters any other letters, it keeps asking for the
grade until you enters a valid grade. 

The input data (student’s ID, course number, grade) is saved to the file “grades.txt”.

Moreover, the GPA of that student should be updated in the file “students.txt”.
# Option 4

When you select 4, the system will ask for student’s ID, if there is no student in the system with
that ID, it displays “No students with this ID”. If the student is not in the system, it prints “No
student with this ID”, otherwise it prints student name, his/her GPA, followed by course number,
course name, grade for all courses.













