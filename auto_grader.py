class BatchGrader:
    def process_grades(self, assignment_list, student_profile):
        print(f"Starting Auto-Grader for {student_profile.student_name}...")

        for assignment in assignment_list:
            assignment.get_details()
            score = assignment.grade_work()
            student_profile.add_points(score)

        print(f"\nFinal Grade Processed! Total Score: {student_profile.get_current_score()}")


if __name__ == "__main__":
    class SampleTask:
        def __init__(self, title, points):
            self.title = title
            self.points = points

        def get_details(self):
            print(f"[TASK] {self.title} - Max Points: {self.points}")

        def grade_work(self):
            return self.points

    class SampleStudent:
        def __init__(self, name):
            self.student_name = name
            self.total = 0

        def add_points(self, points):
            self.total += points

        def get_current_score(self):
            return self.total