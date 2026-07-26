class students:
    def __init__(self, name, major, code_score, project_score, exam_score):
        # Initialize student attributes
        self.name = name
        self.major = major
        self.code_score = code_score
        self.project_score = project_score
        self.exam_score = exam_score

    def calculate_pass(self):
        # Calculate average score and judge pass status
        average = (self.code_score + self.project_score + self.exam_score) / 3
        pass_status = average > 50
        return pass_status

    def print_info(self):
        # Print student details and pass result
        passed = self.calculate_pass()
        print(f"Name: {self.name}, Major: {self.major}, Pass: {passed}")

# Example instantiation
if __name__ == "__main__":
    student1 = students("Alice", "BMI", 60, 55, 52)
    student1.print_info()