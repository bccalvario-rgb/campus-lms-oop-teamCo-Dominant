class CoursePortal:
    def __init__(self, course_name):
        self.course_name = course_name
        # Private attribute encapsulating the lock state
        self.__is_locked = False

    def lock_portal(self):
        self.__is_locked = True
        print("Deadline passed. Portal is locked.")

    def accept_submission(self, student_name):
        if self.__is_locked:
            raise ValueError("Error: Deadline has passed. Submission rejected")
        else:
            print(f"Submission accepted for {student_name}.")


# Example usage to test the functionality
if __name__ == "__main__":
    portal = CoursePortal("CS101")
    
    # Submission before deadline
    portal.accept_submission("Alice")
    
    # Simulate passed deadline
    portal.lock_portal()
    
    # Submission after deadline (raises ValueError)
    try:
        portal.accept_submission("Bob")
    except ValueError as e:
        print(e)
