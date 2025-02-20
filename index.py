class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.allocated = False

    def allocate(self):
        if not self.allocated:
            self.allocated = True
            return f"Classroom {self.room_number} allocated."
        else:
            return f"Classroom {self.room_number} is already allocated."


class Course:
    def __init__(self, course_name, num_students, duration):
        self.course_name = course_name
        self.num_students = num_students
        self.duration = duration
        self.classroom = None

    def assign_classroom(self, classroom):
        if self.num_students <= classroom.capacity:
            self.classroom = classroom
            return classroom.allocate()
        else:
            return f"Not enough capacity in classroom {classroom.room_number} for course {self.course_name}."


classroom_list = [
    Classroom("A101", 30),
    Classroom("B202", 50),
    Classroom("C303", 40),
    Classroom("D404", 20)
]

course_list = [
    Course("Mathematics", 25, 60),
    Course("Science", 45, 90),
    Course("History", 35, 50),
    Course("Literature", 15, 40)
]

# Classroom allocation logic
for course in course_list:
    allocated = False
    for classroom in classroom_list:
        if not classroom.allocated and course.num_students <= classroom.capacity:
            print(f"{course.course_name}: {course.assign_classroom(classroom)}")
            allocated = True
            break
    if not allocated:
        print(f"{course.course_name}: No suitable classroom available.")
