class CoursePortal:
    def __init__(self, course_name):
        self.course_name = course_name
        self.__is_locked = False

    def lock_portal(self):
        if not self.__is_locked:
            self.__is_locked = True
            print("Deadline passed. Portal locked.")

    def accept_submission(self, student_name):
        if self.__is_locked:
            raise ValueError("Error: Deadline has passed. Submission rejected.")
        
        if not student_name.strip():
            raise ValueError("Error: Student name cannot be blank.")

        print(f"Submission accepted for {student_name}.")

p = CoursePortal("Computer Science")
p.accept_submission("Thirdy")
p.lock_portal()
p.accept_submission("Late Student")   # should raise ValueError
